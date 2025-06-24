from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from book.models import Book
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets
from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')  # для вложенного роутинга
        if user_id:
            return Order.objects.filter(user_id=user_id)
        return Order.objects.all()

def is_librarian(user):
    return user.is_authenticated and user.role == 1

@login_required
@user_passes_test(is_librarian)
def all_orders_view(request):
    orders = Order.objects.select_related('book', 'user').all()
    return render(request, 'librarian/order_list.html', {'orders': orders})

@login_required
def my_orders_view(request):
    orders = Order.objects.filter(user=request.user).select_related('book')
    return render(request, 'user/order_list.html', {'orders': orders})

@login_required
def create_order_view(request):
    books = Book.objects.all()
    error = None

    if request.method == 'POST':
        book_id = request.POST.get('book')
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            error = "Book not found."
        else:
            if book.count < 1:
                error = "Book is not available."
            else:
                plated_end_at = timezone.now() + timedelta(weeks=2)
                order = Order.create(user=request.user, book=book, plated_end_at=plated_end_at)
                book.count -= 1
                book.save()
                return redirect('my_orders')

    return render(request, 'user/create_order.html', {'books': books, 'error': error})

@login_required
@user_passes_test(is_librarian)
def close_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.end_at is None:
        order.update(end_at=timezone.now())
        order.save()
        order.book.count += 1
        order.book.save()
    return redirect('all_orders')
