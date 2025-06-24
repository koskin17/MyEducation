from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Author
from .forms import AuthorForm
from rest_framework import viewsets
from author.models import Author
from author.serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def is_librarian(user):
    return user.is_authenticated and user.role == 1

@login_required
@user_passes_test(is_librarian)
def author_list_view(request):
    authors = Author.get_all()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        surname = request.POST.get('surname', '').strip()
        patronymic = request.POST.get('patronymic', '').strip()

        if name and surname and patronymic:
            Author.create(name=name, surname=surname, patronymic=patronymic)
            return redirect('author_list')

    return render(request, 'author_list.html', {'authors': authors})

@login_required
@user_passes_test(is_librarian)
def create_author_view(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('author_list')
        else:
            form = AuthorForm()
        return render(request, 'author/create_author.html', {'form': form})
    return render(request, 'create_author.html')

@login_required
@user_passes_test(is_librarian)
def delete_author_view(request, author_id):
    author = Author.get_by_id(author_id)
    if author and not author.books.exists():
        Author.delete_by_id(author_id)
    return redirect('author_list')
