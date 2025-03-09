from application import db, create_app

app = create_app()

with app.app_context():
    db.create_all()  # Ensure this line runs inside the context

if __name__ == '__main__':
    app.run(debug=True)



