# 💰 Money Sharing App (Flask Project)

A modern **money sharing web application** built using **Flask**, designed for sending, receiving, and tracking transactions between users. This project is fully functional with authentication, profiles, transaction history, and more—all coded using Python and SQLAlchemy for database management.  

> ⚠️ Note: This app uses **dummy currency (numbers only)** for demonstration purposes. No real money transactions are involved.

---

## Features

### ✅ Core Features
- **User Authentication:** Secure signup and login system.  
- **Default Balance:** Every new user starts with **₹1000** in their account.  
- **Send & Receive Money:** Users can transfer funds to other users.  
- **Transaction History:** Each user can view detailed transaction history on their **profile page**.  
- **Success Alerts:** Transactions display **success messages** using alert-style notifications.  
- **Profile Search:** Built-in search bar to look up other users’ profiles.  
- **Unique Account Numbers:** Each user gets a **new, unique account number** upon signup.  

### 🌐 Web Pages
- **Home:** Main landing page.  
- **About / Services / Contact:** Pages included for a professional look, currently placeholders.  
- **Profile:** Displays user information, transaction history, and balance.  
- **Signup/Login:** Fully functional authentication pages.  

### 🎨 Frontend
- **HTML & CSS:** Modern and responsive layouts, created with the help of **ChatGPT** to save development time.  
- **No JavaScript:** Entirely built with Python, Flask, and HTML/CSS for simplicity.  

### 🔮 Future Plans
- **QR Code Integration:** Send and receive money via QR codes.  
- **QR Scanner:** Scan and pay directly from other users’ codes.  
- **Enhanced Services Pages:** Fully functional About, Services, and Contact pages.  
- **Additional Security Features:** Two-factor authentication, better transaction verification, etc.  

---

## Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLAlchemy (SQLite or other supported DB)  
- **Frontend:** HTML, CSS  
- **Environment:** Virtualenv recommended  

---

## Installation

1. **Clone the repository:**

   git clone https://github.com/yourusername/money-sharing-app.git
   cd money-sharing-app

2. **Create a virtual environment:**

   python -m venv venv<br>
   source venv/bin/activate   # Linux/Mac<br>
   venv\Scripts\activate      # Windows<br>

3. **Install dependencies:**

   pip install -r requirements.txt

4. **Run the app:**

   python app.py

5. **Open in browser:**

   Go to http://127.0.0.1:5000

---

## Usage

1. **Signup**: Create a new account and get a default ₹1000 balance.

2. **Login**: Access your dashboard and profile.

3. **Send Money**: Enter recipient details, amount, and confirm.

4. **Transaction Alerts**: See real-time confirmation messages.

5. **Profile Search**: Search for other users using the search bar.

6. **Transaction History**: Track all past transactions in your profile page.
   
---

## Project Structure
money-sharing-app/
│
├── templates/           # HTML templates<br>
│   ├── home.html<br>
│   ├── login.html<br>
│   ├── signup.html<br>
│   ├── profile.html<br>
│   ├── about.html<br>
│   ├── services.html<br>
│   └── contact.html<br>
│
├── static/              # CSS, images<br>
│   └── style.css<br>
├── app.py               # Flask application<br>           
└── README.md<br>

---

## Notes

- **Dummy Currency**: This project is for learning purposes only, using fake balances.

- **No JavaScript**: Entire functionality is handled with Python & Flask.

- **Alerts**: Transaction alerts are implemented using HTML/CSS styles.
  
---

This project is **beginner-friendly**, designed to help learners explore **Python, Flask, and web development** through a hands-on, practical experience.
