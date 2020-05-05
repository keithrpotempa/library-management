import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


# Just don't need this? Copied over from books/form.py
# def get_libraries():
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = model_factory(Library)
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         select
#             l.id,
#             l.title,
#             l.address
#         from libraryapp_library l
#         """)

#         return db_cursor.fetchall()


#FIXME: Something missing here?
@login_required
def library_form(request):
    if request.method == 'GET':
        template = 'libraries/form.html'
        context = {
        }

        return render(request, template, context)