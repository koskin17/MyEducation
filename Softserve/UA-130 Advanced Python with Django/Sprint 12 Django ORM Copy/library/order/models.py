from django.db import models
from book.models import Book
from authentication.models import CustomUser
from datetime import datetime
from django.db import transaction


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(null=True, blank=True)
    plated_end_at = models.DateTimeField()

    def __str__(self):
        """
        Magic method is redefined to show all information about Order.
        :return: book id, book name, book description, book count, book authors
        """

        def format_dt(dt):
            return dt.strftime('%Y-%m-%d %H:%M:%S%z')[:-2] + ':' + dt.strftime('%Y-%m-%d %H:%M:%S%z')[-2:]
    
        created_at = format_dt(self.created_at)
        plated_end_at = format_dt(self.plated_end_at)
        end_at = format_dt(self.end_at) if self.end_at else None
        return (
            f"'id': {self.id}, "
            f"'user': CustomUser(id={self.user.id}), "
            f"'book': Book(id={self.book.id}), "
            f"'created_at': '{created_at}', "
            f"'end_at': {f'\'{end_at}\'' if end_at else 'None'}, "
            f"'plated_end_at': '{plated_end_at}'"
        )
    
    def __repr__(self):
        """
        This magic method is redefined to show class and id of Order object.
        :return: class, id
        """
        return f"{self.__class__.__name__}(id={self.id})"

    def to_dict(self):
        """
        :return: dict contains order id, book id, user id, order created_at, order end_at, order plated_end_at
        :Example:
        | {
        |   'id': 8,
        |   'book': 8,
        |   'user': 8',
        |   'created_at': 1509393504,
        |   'end_at': 1509393504,
        |   'plated_end_at': 1509402866,
        | }
        """
        return {
            'id': self.id,
            'book': self.book.id,
            'user': self.user.id,
            'created_at': int(self.created_at.timestamp()),
            'end_at': int(self.end_at.timestamp()) if self.end_at else None,
            'plated_end_at': int(self.plated_end_at.timestamp()),
        }

    @staticmethod
    def create(user, book, plated_end_at):
        """
        :param user: the user who took the book
        :type user: CustomUser
        :param book: the book they took
        :type book: Book
        :param plated_end_at: planned return of data
        :type plated_end_at: int (timestamp)
        :return: a new order object which is also written into the DB
        """
        
        if not user.pk or not book.pk:
            return None
        
        try:
            fresh_book = Book.objects.get(pk=book.pk)
        except Book.DoesNotExist:
            return None

        if fresh_book.count <= 0:
            return None
        
        # Перевірка фактичної кількості доступних книг
        active_orders = Order.objects.filter(book=book, end_at__isnull=True).count()
        available_count = book.count - active_orders

        if available_count <= 0:
            return None

        if isinstance(plated_end_at, int):
            plated_end_at = datetime.fromtimestamp(plated_end_at)

        return Order.objects.create(user=user, book=fresh_book, plated_end_at=plated_end_at)

    @staticmethod
    def get_by_id(order_id):
        """
        :param order_id:
        :type order_id: int
        :return:  the object of the order, according to the specified id or null in case of its absence
        """
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    def update(self, plated_end_at=None, end_at=None):
        """
        Updates order in the database with the specified parameters.\n
        :param plated_end_at: new plated_end_at
        :type plated_end_at: int (timestamp)
        :param end_at: new end_at
        :type plated_end_at: int (timestamp)
        :return: None
        """
        if plated_end_at:
            if isinstance(plated_end_at, int):
                self.plated_end_at = datetime.fromtimestamp(plated_end_at)
            else:
                self.plated_end_at = plated_end_at
        if end_at:
            if isinstance(end_at, int):
                self.end_at = datetime.fromtimestamp(end_at)
            else:
                self.end_at = end_at
        self.save()

    @staticmethod
    def get_all():
        """
        :return: all orders
        """
        return list(Order.objects.all())

    @staticmethod
    def get_not_returned_books():
        """
        :return:  all orders that do not have a return date (end_at)
        """
        return list(Order.objects.filter(end_at__isnull=True))

    @staticmethod
    def delete_by_id(order_id):
        """
        :param order_id: an id of a user to be deleted
        :type order_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        order = Order.get_by_id(order_id)
        if order:
            order.delete()
            return True
        return False
