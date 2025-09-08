from flask import Flask, request, session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import random
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'super_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    account_number = db.Column(db.String(100))
    balance = db.Column(db.Float, default = 1000)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(50))
    receiver = db.Column(db.String(50))
    amount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if 'name' not in session:
        return redirect(url_for('login'))
    return render_template('home.html',name = session.get('name'),account_number = session.get('account_number'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error_message = None
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name = name).first()
        if user:
            error_message = '*Username is already exists*'
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            account_number = str(random.randint(10000,99999))

            new_user = User(
                name=name,
                password=hashed_password.decode('utf-8'),
                account_number = account_number
            )

            db.session.add(new_user)
            db.session.commit()

            session['name'] = name
            session['account_number'] = account_number
            return redirect(url_for('home')) 

    return render_template('signup.html',error_message = error_message)

@app.route('/dashboard')
def dashboard():
    all_users = User.query.all()
    return render_template('dashboard.html', all_users = all_users)

@app.route('/delete/<sno>', methods = ['GET','POST'])
def delete(sno):
    user = User.query.filter_by(sno = sno).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/login', methods = ['GET','POST'])
def login():
    error_message = None
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name = name).first()
        
        if user:  
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):  
                session['name'] = user.name
                session['account_number'] = user.account_number
                return redirect(url_for('home'))
            else:
                error_message = '*Password is Incorrect*'
        else:
            error_message = '*Username does not exist. Signup first*'
    return render_template('login.html', error_message = error_message)

@app.route('/send_money',methods = ['GET','POST'])
def send_money():
    if 'account_number' not in session:   
        return redirect(url_for('login'))
    success_message = None
    error_message = None
    
    if request.method == 'POST':
        recipient_name = request.form.get('name')
        account_number = request.form.get('account')
        amount = float(request.form.get('amount'))

        sender = User.query.filter_by(account_number = session['account_number']).first()
        reciever = User.query.filter_by(account_number = account_number).first()

        if not reciever:
            error_message = "*Receiver account not found!*"
        elif amount <= 0:
            error_message = "*Invalid amount!*"
        elif sender.balance < amount:
            error_message = "*Insufficient balance!*"
        else:
            sender.balance -= amount
            reciever.balance += amount
            db.session.commit()
            success_message = '✅Amount successfully transfered🎉'

            txn = Transaction(
                sender = sender.name,
                receiver = reciever.name,
                amount = amount
            )

            db.session.add(txn)
            db.session.commit()

    return render_template('send_money_page.html',user = user ,error_message = error_message, success_message = success_message)

@app.route('/profile/<name>')
def profile(name):
    # session check kar sakte ho sirf login ke liye
    if 'account_number' not in session:
        return redirect(url_for('login'))

    # URL se user fetch karo
    user = User.query.filter_by(name=name).first()
    if not user:
        return 'Username not found'

    # Sent and received transactions of that user
    sent_txns = Transaction.query.filter_by(sender=user.name).all()
    received_txns = Transaction.query.filter_by(receiver=user.name).all()

    return render_template('profile.html', user=user, sent_txns=sent_txns, received_txns=received_txns)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/search_profile', methods=['GET'])
def search_profile():
    query = request.args.get('query')
    if not query:
        return redirect(url_for('home'))

    user = User.query.filter_by(name=query).first()
    if not user:
        return 'User not found'

    #sent_txns = Transaction.query.filter_by(sender=user.name).all()
    #received_txns = Transaction.query.filter_by(receiver=user.name).all()

    return render_template('profile.html', user=user, hide_transactions=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)