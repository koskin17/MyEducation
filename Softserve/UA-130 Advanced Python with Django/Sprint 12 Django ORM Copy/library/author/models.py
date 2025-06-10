from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)

    def __str__(self):
        return f"'id': {self.id}, 'name': '{self.name}', 'surname': '{self.surname}', 'patronymic': '{self.patronymic}'"

    def __repr__(self):
        return f"Author(id={self.id})"

    @staticmethod
    def get_by_id(author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(author_id):
        author = Author.get_by_id(author_id)
        if author:
            author.delete()
            return True
        return False

    @staticmethod
    def create(name, surname, patronymic):
        if len(name) > 20 or len(surname) > 20 or len(patronymic) > 20:
            return None
        author = Author(name=name, surname=surname, patronymic=patronymic)
        author.save()
        return author

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
        }

    def update(self, name=None, surname=None, patronymic=None):
        if name is not None:
            if len(name) <= 20:
                self.name = name
        if surname is not None:
            if len(surname) <= 20:
                self.surname = surname
        if patronymic is not None:
            if len(patronymic) <= 20:
                self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        return Author.objects.all()
