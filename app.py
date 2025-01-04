from flask import Flask, request, json, jsonify, Response
import requests


app = Flask(__name__)


posts = [
    {"id": 1, "content": "That's my first post"},
    {"id": 2, "content": "That's my second post"}
]


# Главная страница
@app.route('/')
def send_readme():
    readme_url = "https://raw.githubusercontent.com/Fishhma/starpost/refs/heads/main/README.md"

    try:
        response = requests.get(readme_url)
        if response.status_code == 200:
            return Response(response.text, content_type='text/markdown')
        else:
            return "Couldn't get the README.md file", 404
    except Exception as ex:
        return f"There was a misatke with README.md: {ex}", 500

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = None

    for p in posts:
        if p["id"] == post_id:
            post = p
            break
    if post:
        return jsonify(post)
    else:
        return jsonify({"message": "Post not found"}), 404

@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post["id"] = len(posts) + 1
    posts.append(new_post)

    return jsonify(new_post), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    updated_data = request.get_json()

    for index, post in enumerate(posts):

        if post["id"] == post_id:
            posts[index].update(updated_data)
            return jsonify({"message": "Post updated"}), 200
        
    return jsonify({"message": "Post not found"}), 404
    
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts

    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            return jsonify({"message": "Post deleted"}), 200
        
    return jsonify({"message": "Post not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)