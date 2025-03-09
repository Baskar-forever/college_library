from flask import Blueprint, render_template, request, redirect, url_for, session
from application import db
from application.models import User,Book,Borrow

# Create a Blueprint for routes
routes = Blueprint('routes', __name__)

# Home Page
@routes.route('/')
def home():
    return render_template('home.html')

# Login Page
@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print("email:",email+" password: ",password)
        user = User.query.filter_by(email=email, password=password).first()
        print(user)
        if user:
            session['user_id'] = user.id
            session['role'] = user.role
            if user.role == 'admin':  # Librarian
                return redirect(url_for('routes.dashboard_admin'))
            elif user.role == 'staff':
                return redirect(url_for('routes.dashboard_staff'))
            elif user.role == 'student':
                return redirect(url_for('routes.dashboard_student'))
        return "Invalid email or password!"
    return render_template('login.html')

# Admin (Librarian) Dashboard
@routes.route('/dashboard/admin')
def dashboard_admin():
    return render_template('dashboard_admin.html')

# Staff Dashboard
@routes.route('/dashboard/staff')
def dashboard_staff():
    return render_template('dashboard_staff.html')

# Student Dashboard
@routes.route('/dashboard/student')
def dashboard_student():
    return render_template('dashboard_student.html')

# Logout
@routes.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    return redirect(url_for('routes.login'))

@routes.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        address = request.form.get('address')  # Get address from form
        role = request.form.get('role')

        print(f"Received: Name={name}, Email={email}, Password={password}, Role={role}, Phone={phone}, Address={address}")

        if not address:  # Ensure address is provided
            return "Address is required!", 400

        new_user = User(name=name, email=email, password=password, role=role, phone=phone, address=address)
        db.session.add(new_user)
        db.session.commit()
        return "User added successfully!"
    
    return render_template('add_user.html')


@routes.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        quantity = request.form['quantity']

        new_book = Book(title=title, author=author, quantity=int(quantity))
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('routes.dashboard_admin'))

    return render_template('add_book.html')

@routes.route('/manage_books')
def manage_books():
    books = Book.query.all()  # Fetch all books from the database
    return render_template('manage_books.html', books=books)

@routes.route('/view_books')
def view_books():
    books = Book.query.all()  # Fetch all books from the database
    return render_template('view_books.html', books=books)


@routes.route('/borrow_book/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    if 'user_id' not in session:
        return "Unauthorized access. Please login first.", 403  # User must be logged in

    user_id = session['user_id']
    user = User.query.get(user_id)
    book = Book.query.get(book_id)

    if not book:
        return "Book not found.", 404  # Handle invalid book IDs

    if book.quantity <= 0:  # Use `quantity` instead of `copies`
        return "No copies available for borrowing.", 400  # No books left

    # Reduce available copies
    book.quantity -= 1  # Use `quantity`
    db.session.commit()

    # Create a borrow record
    borrow_entry = Borrow(user_id=user.id, book_id=book.id)
    db.session.add(borrow_entry)
    db.session.commit()

    return redirect(url_for('routes.view_books'))  # Redirect to books list

