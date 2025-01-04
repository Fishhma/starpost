from models.user import User

class Post:

    def __init__(self, id: int, content: str, username: User):
        self.id = id
        self.content = content
        self.username = username

    def to_dict(self):
        """Метод для преобразования объекта в словарь."""
        return {'id': self.id, 'content': self.content, 'username': self.username}