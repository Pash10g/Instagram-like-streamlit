# Instagram like streamlit

This project was aimed to messure how fast can my new GPT called [MDB Schema Builder](https://chat.openai.com/g/g-J3KcWl0wj-mdb-schemabuilder) build a demo app for an "Instagram" like application.

Tech stack:
- MongoDB Atlas
- Pymongo
- Streamlit

## Demo app:
https://kj5hq7hrgaooq9kzymhvmt.streamlit.app/


## Database schema

### Users Collection Schema

| Field Name    | Type        | Description                         |
|---------------|-------------|-------------------------------------|
| `_id.$oid`    | String      | Unique identifier for the document  |
| `id`          | String      | User's unique ID                    |
| `email`       | String      | User's email address                |
| `firstName`   | String      | User's first name                   |
| `lastName`    | String      | User's last name                    |
| `phone`       | String      | User's phone number                 |
| `img`         | String      | URL to user's profile image         |
| `username`    | String      | User's username                     |
| `address`     | Object      | User's address information          |
| `address.street` | String  | Street part of the address          |
| `address.city`   | String  | City part of the address            |
| `address.zipCode` | String  | Zip code part of the address        |
| `address.county`  | String  | County part of the address          |
| `address.country` | String  | Country part of the address         |
| `followers`   | Integer     | Number of users following this user |
| `following`   | Integer     | Number of users this user follows   |
| `postsCount`  | Integer     | Number of posts the user has made   |
```
 {
  "_id": {
    "$oid": "6603ef7de87fefc14d7e9360"
  },
  "id": "01cc8ed1-73c3-46ad-8471-ae3ad3d2db52",
  "email": "christineclark@frontiernet.com",
  "firstName": "Christine",
  "lastName": "Clark",
  "phone": "+250(199)452 218",
  "img": "https://i.pravatar.cc/100",
  "username": "Christine_Clark76",
  "address": {
    "street": "181 Reynold Crossing",
    "city": "North Celia",
    "zipCode": "55999-2988",
    "county": "Cornwall",
    "country": "Moldova"
  },
  "followers": 3494,
  "following": 3497,
  "postsCount": 17
}
```
### Posts Collection Schema

| Field Name       | Type          | Description                           |
|------------------|---------------|---------------------------------------|
| `_id.$oid`       | String        | Unique identifier for the post        |
| `userId.$oid`    | String        | Reference to the user who created the post |
| `image`          | String        | URL of the post's image               |
| `caption`        | String        | Caption of the post                   |
| `location`       | String        | Location where the post was made      |
| `likesCount`     | Integer       | Number of likes on the post           |
| `comments`       | Array         | List of comments on the post          |
| `comments[].user.id` | String    | ID of the user who commented          |
| `comments[].user.email` | String | Email of the user who commented       |
| `comments[].user.firstName` | String | First name of the user who commented |
| `comments[].user.lastName` | String | Last name of the user who commented  |
| `comments[].user.phone` | String | Phone number of the user who commented |
| `comments[].user.img` | String  | Profile image URL of the user who commented |
| `comments[].user.username` | String | Username of the user who commented   |
| `comments[].user.address.street` | String | Street of the user's address        |
| `comments[].user.address.city` | String | City of the user's address          |
| `comments[].user.address.zipCode` | String | Zip code of the user's address     |
| `comments[].user.address.county` | String | County of the user's address        |
| `comments[].user.address.country` | String | Country of the user's address      |
| `comments[].text` | String       | Text of the comment                   |
| `comments[].timestamp.$date` | String | Timestamp when the comment was made |
| `timestamp.$date`| String        | Timestamp when the post was created   |


```
{
  "_id": {
    "$oid": "6603ef7de87fefc14d7e9361"
  },
  "userId": {
    "$oid": "6603ef7de87fefc14d7e9360"
  },
  "image": "https://picsum.photos/500/500",
  "caption": "Caption for post 0",
  "location": "Location 0",
  "likesCount": 4690,
  "comments": [
    {
      "user": {
        "id": "b6799dda-b243-4c66-ae3c-029aaf5238a1",
        "email": "johanna.arnarson@freenet.name",
        "firstName": "Johanna",
        "lastName": "Arnarson",
        "phone": "+371 82 394 722",
        "img": "https://i.pravatar.cc/100",
        "username": "Johanna.Arnarson44",
        "address": {
          "street": "646 Curt Locks",
          "city": "Borerville",
          "zipCode": "49638-7077",
          "county": "Suffolk",
          "country": "Namibia"
        }
      },
      "text": "Comment 0",
      "timestamp": {
        "$date": "2024-03-27T10:05:49.543Z"
      }
    },
    {
      "user": {
        "id": "3f099434-ea13-427f-ac34-12d35a64041e",
        "email": "sabine_moore454@aim.com",
        "firstName": "Sabine",
        "lastName": "Moore",
        "phone": "+291 2 648 937",
        "img": "https://i.pravatar.cc/100",
        "username": "Sabine.Moore45",
        "address": {
          "street": "392 Esteban Inlet",
          "city": "East Providence",
          "zipCode": "80108",
          "county": "Isle of Wight",
          "country": "Brazil"
        }
      },
      "text": "Comment 1",
      "timestamp": {
        "$date": "2024-03-27T10:05:49.543Z"
      }
    },
   ...
  ],
  "timestamp": {
    "$date": "2024-03-27T10:05:49.550Z"
  }
}
```

## How to setup

Create a MongoDB Atlas cluster:
- https://www.mongodb.com/docs/atlas/getting-started/
- Clone the repo
- Setup a streamlit env with mymongo:
  ```
  pip install -r requirements.txt
  ```

Create the database schema with the mongosh script
```
npm i @ngneat/falso
mognosh <your_atlas_cluster>
```

```
use('instagram_app');
const falso = require('@ngneat/falso');

// Generate and insert users and their posts
for (let i = 0; i < 100; i++) {
    // Generate a user
    let falsoUser = falso.randUser();
    const user = {
        ...falsoUser,
        followers: Math.floor(Math.random() * 10000),
        following: Math.floor(Math.random() * 5000),
        postsCount: Math.floor(Math.random() * 100)
    };

    // Insert the user into the Users collection
    const userId = db.users.insertOne(user).insertedId;

    // Generate and insert posts for this user
    for (let j = 0; j < user.postsCount; j++) {
        const post = {
            userId: userId,
            image: falso.randImg(),
            caption: `Caption for post ${j}`,
            location: `Location ${j}`,
            likesCount: Math.floor(Math.random() * 5000),
            comments: Array.from({ length: Math.floor(Math.random() * 100) }, (_, i) => ({
                user: falso.randUser(),
                text: `Comment ${i}`,
                timestamp: new Date()
            })),
            timestamp: new Date()
        };

        // Insert the post into the Posts collection
        db.posts.insertOne(post);
    }
}
```

## Run
```
export MONGODB_ATLAS_URI=<your_atlas_uri>
streamlit run app.py
```
