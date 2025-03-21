### Documentation


This is a simple API for using posts. It supports basic CRUD operations


**How to install on Windows**
	
										
1. ```
   git clone https://github.com/Fishhma/starpost.git
   ```
   
2. ```
   cd starpost
   ```

3. ```
   pip install -r requirements.txt
   ```

4. ```
   python app.py
   ```


		
**Available Routes:**

1. Get All Posts
   - Method: GET
   - URL: /posts
   - Description: Returns a list of all posts

2. Get Post by ID
   - Method: GET
   - URL: /posts/id
   - Description: Returns the post with the given ID

3. Create a New Post
   - Method: POST
   - URL: /posts
   - Description: Creates a new post
   - Request Body (JSON):
   ```
     {
       "content": "Write content here"
       "username": "@fishma"
     }
   ```

4. Update Post by ID
   - Method: PUT
   - URL: /posts/id
   - Description: Updates the post with the given ID
   - Request Body (JSON):
   ```
     {
       "content": "Updated content"
       "username": "@fishma"
     }
   ```

5. Delete Post by ID
   - Method: DELETE
   - URL: /posts/id
   - Description: Deletes the post with the given ID



**Example Usage with curl:**
   **For Windows shell**

### Within a JSON parameter string, double quotes must be escaped with a backslash so that they are properly treated as part of the data, not as string termination.  

1. Get all posts:
   ```
   curl -X GET http://127.0.0.1:5000/posts
   ```

2. Get a certain post:
   ```
   curl -X GET http://127.0.0.1:5000/posts/id
   ```

3. Create a new post:
   ```
   curl -X POST -H "Content-Type: application/json" -d "{\"content\": \"Test post content\", \"username\": \"@fishma\"}" http://127.0.0.1:5000/posts
   ```

4. Update a post:
   ```
   curl -X PUT -H "Content-Type: application/json" -d "{\"content\": \"Updated post content\", \"username\": \"@fishma\"}" http://127.0.0.1:5000/posts/id
   ```

5. Delete a post:
   ```
   curl -X DELETE http://127.0.0.1:5000/posts/id
   ```



Accessing the README:
To view this documentation in full, visit the following link: 
https://github.com/Fishhma/starpost/blob/main/README.md
