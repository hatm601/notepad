# 📝 Flask Notepad App

A simple web-based notepad application built with Flask. This app allows users to log in and edit notes through a user-friendly interface styled with SCSS.

## Features

- 🔐 Login system  
- 📝 Create, view, and edit notes  
- 🎨 Clean UI styled with SCSS  
- 💾 Data saved using SQLite  
- 📱 Responsive layout  

## Project Structure

```
notepad-app/
├── static/
│   └── scss/
│       └── style.scss
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   └── edit.html
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/notepad-app.git
cd notepad-app
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
flask run
```

Open your browser and visit:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Default Login Credentials

*(You can customize these in `main.py`)*

- Username: `admin`  
- Password: `secret`  

## Built With

- Python  
- Flask  
- HTML & Jinja2  
- SCSS  
- SQLite  

## License

This project is licensed under the MIT License.