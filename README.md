Star Posts API
A simple API for managing posts with basic CRUD operations.

Installation on Windows
Clone the repository:
git clone https://github.com/Fishhma/starpost.git

Navigate to the project directory:
cd starpost

Install the required dependencies:
pip install -r requirements.txt

Start the application:
python app.py

Available Routes
Get All Posts
Method: GET
URL: /posts
Description: Returns a list of all posts

Get Post by ID
Method: GET
URL: /posts/<id>
(Replace <id> with the desired post ID)
Description: Returns the post with the specified ID

Create a New Post
Method: POST
URL: /posts
Description: Creates a new post
Request Body (JSON):
{
"content": "Write content here",
"username": "@fishma"
}

Update Post by ID
Method: PUT
URL: /posts/<id>
(Replace <id> with the desired post ID)
Description: Updates the post with the specified ID
Request Body (JSON):
{
"content": "Updated content",
"username": "@fishma"
}

Delete Post by ID
Method: DELETE
URL: /posts/<id>
(Replace <id> with the desired post ID)
Description: Deletes the post with the specified ID

Example Usage with curl
Get all posts:
curl -X GET http://127.0.0.1:5000/posts

Get a specific post:
curl -X GET http://127.0.0.1:5000/posts/<id>

Create a new post:
curl -X POST -H "Content-Type: application/json" -d "{"content": "Test post content", "username": "@fishma"}" http://127.0.0.1:5000/posts

Update a post:
curl -X PUT -H "Content-Type: application/json" -d "{"content": "Updated post content", "username": "@fishma"}" http://127.0.0.1:5000/posts/<id>

Delete a post:
curl -X DELETE http://127.0.0.1:5000/posts/<id>
