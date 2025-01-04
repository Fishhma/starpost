class User:

    def __init__(self, username: str):
        self.username = username

###если что закоментить ниже

    def to_dict(self):
        """Метод для преобразования объекта в словарь."""
        return {'author': self.username}