import streamlit as st
import os
from pymongo import MongoClient

# MongoDB connection setup
def get_db():
    uri = os.getenv("MONGODB_ATLAS_URI")
    client = MongoClient(uri)
    db = client.instagram_app
    return db

def get_users(db):
    return list(db.users.find({}, {'username': 1}))

def get_user_posts(db, user_id, page_size=10, page_number=1):
    skip_count = (page_number - 1) * page_size
    return list(db.posts.find({"userId": user_id}).skip(skip_count).limit(page_size))

def main():
    st.title('Instagram-like App Schema Showcase')

    db = get_db()

    # User login simulation
    users = get_users(db)
    user_names = [user['username'] for user in users]
    selected_user_name = st.selectbox('Select User', user_names)

    # Pagination setup
    page_number = st.number_input('Page Number', min_value=1, value=1)
    page_size = 5  # Number of posts per page

    # Fetch and display posts for the selected user
    if selected_user_name:
        user = db.users.find_one({"username": selected_user_name})
        if user:
            posts = get_user_posts(db, user['_id'], page_size=page_size, page_number=page_number)
            st.write(f"Posts for {selected_user_name}:")
            st.image(user['img'], caption='Profile Picture')
            for post in posts:
                st.divider()
                st.header(post['location'], anchor=str(post['_id']), divider='rainbow')
                st.image(post['image'], caption=post['caption'])
                st.text(f"Likes: {post.get('likesCount', 0)}")
                st.text(f"Timestamp: {post.get('timestamp', 'N/A')}")
                st.text("Comments:")
                for comment in post.get('comments', []):
                    st.divider()
                    st.text(f"{comment['user']['username']}: {comment['text']}")

if __name__ == "__main__":
    main()
