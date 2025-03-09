# 📚 Library Management System  

A Flask-based library management system with MySQL and SQLAlchemy.  

## 🚀 Features  
- 📖 Add, view, borrow, and return books  
- 👤 User authentication (Admin, Staff, Students)  
- 🎨 Modern UI with a glassmorphic design  
- 🗄️ MySQL database integration using SQLAlchemy  
- 🔐 Secure credentials using `.env` file  

---

## 📌 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/college_library.git
cd college_library
```

### 2️⃣ Create & Activate Virtual Environment  
#### Windows  
```bash
python -m venv venv
venv\Scripts\activate
```
#### macOS/Linux  
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables  
1. Copy `.env.sample` and rename it as `.env`  
   ```bash
   cp env.sample .env
   ```
2. Open `.env` and update the values:  
   ```ini
   DATABASE_URI=mysql+pymysql://your_user:your_password@localhost:3306/library_management
   SECRET_KEY=your_secret_key
   ```

### 5️⃣ Setup Database  
Ensure MySQL is running, then create the database:  
```sql
CREATE DATABASE library_management;
```

### 6️⃣ Run the Application  
```bash
flask run
```
The app will be available at: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

## 🛠️ Project Structure  
```bash
college_library/
│── application/
│   ├── models.py          # Database models
│   ├── routes.py          # Application routes
│   ├── __init__.py        # App factory function
│── static/                # CSS, JS, Images
│── templates/             # HTML files
│── .env.sample            # Example environment variables
│── .gitignore             # Ignore sensitive files
│── README.md              # Project Documentation
│── requirements.txt       # Python dependencies
│── run.py                 # Entry point of the app
```

## 📝 Contribution  
Want to contribute? Follow these steps:  

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes  
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to GitHub and create a PR  
   ```bash
   git push origin feature-name
   ```

## 📜 License  
This project is licensed under the MIT License.
