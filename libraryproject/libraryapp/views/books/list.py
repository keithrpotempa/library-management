import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, model_factory
from ..connection import Connection

@login_required
def book_list(request):
    if request.method == 'GET':
        ## SQL METHOD 
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = model_factory(Book)
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     select
        #         b.id,
        #         b.title,
        #         b.isbn,
        #         b.author,
        #         b.year_published,
        #         b.librarian_id,
        #         b.location_id
        #     from libraryapp_book b
        #     """)

        #     all_books = db_cursor.fetchall()

        # ORM Method
        all_books = Book.objects.all()

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        ## SQL METHOD
        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT INTO libraryapp_book
        #     (
        #         title, author, isbn,
        #         year_published, location_id, librarian_id
        #     )
        #     VALUES (?, ?, ?, ?, ?, ?)
        #     """,
        #     (form_data['title'], form_data['author'],
        #         form_data['isbn'], form_data['year_published'],
        #         request.user.librarian.id, form_data["location"]))

        # ORM METHOD
        new_book = Book(
            title = form_data['title'],
            author = form_data['author'],
            isbn = form_data['isbn'], 
            year_published = form_data['year_published'],
            librarian_id = request.user.librarian.id, 
            location_id = form_data["location"]
        )
        new_book.save()
        

        return redirect(reverse('libraryapp:books'))