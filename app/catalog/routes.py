from flask import render_template

from app.catalog import main
from app.catalog.models import Book, Publisher


@main.route('/')
def display_books():
    book_list = Book.query.all()
    return render_template('home.html', books=book_list)


@main.route('/display/publisher/<int:publisher_id>')
def display_publisher(publisher_id: int):
    publisher = Publisher.query.get(publisher_id)
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)
