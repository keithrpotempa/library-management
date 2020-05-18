import sqlite3
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from ..connection import Connection

@login_required
def librarian_list(request):
    # # SQL METHOD
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = sqlite3.Row
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #       SELECT
    #           l.id,
    #           l.location_id,
    #           l.user_id,
    #           u.first_name,
    #           u.last_name,
    #           u.email
    #       FROM libraryapp_librarian l
    #       JOIN auth_user u ON l.user_id = u.id
    #     """)

    #     all_librarians = []
    #     dataset = db_cursor.fetchall()

    #     for row in dataset:
    #         lib = Librarian()
    #         lib.id = row["id"]
    #         lib.location_id = row["location_id"]
    #         lib.user_id = row["user_id"]
    #         lib.first_name = row["first_name"]
    #         lib.last_name = row["last_name"]
    #         lib.email = row["email"]

    #         all_librarians.append(lib)
    
    # # ORM METHOD
    all_librarians = Librarian.objects.all()
    
    for librarian in all_librarians:
        librarian.first_name = User.objects.get(pk=librarian.user_id).first_name
        librarian.last_name = User.objects.get(pk=librarian.user_id).last_name

    template_name = 'librarians/list.html'

    context = {
        'all_librarians': all_librarians
    }

    return render(request, template_name, context)