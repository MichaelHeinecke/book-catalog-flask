from flask import render_template

from app.catalog import main
from app import db
from app.catalog.models import Book, Publisher


@main.route('/')
def display_books():
    book_list = Book.query.all()
    return render_template('home.html', books=book_list)
