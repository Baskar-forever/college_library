from application import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)  # Add this line


    def __repr__(self):
        return f"<User {self.name} ({self.role})>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)  # ✅ Changed to "quantity"



    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)  # Null until returned

    user = db.relationship('User', backref=db.backref('borrowed_books', lazy=True))
    book = db.relationship('Book', backref=db.backref('borrowed_by', lazy=True))

    def __repr__(self):
        return f"<Borrow {self.user_id} borrowed {self.book_id} on {self.borrow_date}>"
