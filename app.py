#Run using 'python app.py'(to run whats in if __name__ == "__main__":) OR 'flask run'(to run whats outside of that)

import bcrypt
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_mysqldb import MySQL,MySQLdb
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
load_dotenv
import os

app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = os.getenv('SECRET_KEY')

app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DATABASE')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/reservation',  methods=['GET', 'POST'])
def reservation():

  today = date.today().strftime("%Y-%m-%d")
  tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

  if request.method == "POST":
      
      userDetails = request.form
      check_in_date = userDetails['check-in']
      check_out_date = userDetails['check-out']
      check_in_dates = userDetails['check-in'].split('-')
      check_out_dates = userDetails['check-out'].split('-')
      check_in = date(int(check_in_dates[0]), int(check_in_dates[1]), int(check_in_dates[2]))
      check_out = date(int(check_out_dates[0]), int(check_out_dates[1]), int(check_out_dates[2]))
      delta = check_out - check_in
      res_fname = userDetails['f_name']
      res_lname = userDetails['l_name']
      res_email = userDetails['e_mail']
      no_of_guests = userDetails['no_of_guests']
      room_type = userDetails['room_type']
      todays_date = datetime.today().strftime('%Y-%m-%d')

      if (delta.days < 1):
          flash("Check-in date must be before Check-out date")
          return redirect(url_for('reservation'))

      cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      
      cur.execute("SELECT Room_id, Room_type, Check_in_date, Check_out_date FROM reservations WHERE %s = Room_type AND ((%s BETWEEN Check_in_date AND Check_out_date)\
      OR (%s BETWEEN Check_in_date AND Check_out_date) OR (Check_in_date BETWEEN %s AND %s) OR (Check_out_date BETWEEN %s AND %s))",\
      (room_type, check_in_date, check_out_date, check_in_date, check_out_date, check_in_date, check_out_date,))

      result = cur.fetchall()
      
      cur.execute("SELECT * FROM users WHERE email=%s",(res_email,))
      
      email_result = cur.fetchone()

      if len(result) < 5:

          rooms_reserved = [] 
          
          for row in result:
              rooms_reserved = [row['Room_id']]
          
          if len(rooms_reserved) == 0:
              max_value = 0
          else:
              max_value = max(rooms_reserved)

          if 'user_id' in session:
              user_id = session['user_id'] 
          elif email_result:
              user_id = email_result['User_id']
          else:
              user_id = 0

          if room_type == 'King':
              room_price = 300
          elif room_type == 'Queen':
              room_price = 200
          elif room_type == 'Full':
              room_price = 100

          if 'offer_type' in session:
              if session['offer_type'] == "offer50":
                  room_price = room_price*0.5

              elif session['offer_type'] == "offer25":
                  room_price = room_price*0.75

              elif session['offer_type'] == "offer10":
                  room_price = room_price*0.90 

          reservation_price = room_price * delta.days

          session['user_info'] = [room_type, max_value, user_id, res_fname, res_lname, res_email, check_in_date, check_out_date, no_of_guests, todays_date, room_price, reservation_price]

          return redirect(url_for('checkout'))

      else:
          flash('All rooms reserved on these dates, please choose different dates')
          return redirect(url_for('reservation'))

  return render_template('reservation.html', today=today, tomorrow=tomorrow)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
            
    session_data = session.get('user_info', [])

    room_type = session_data[0]
    max_value = session_data[1]
    user_id = session_data[2]
    res_fname = session_data[3]
    res_lname = session_data[4]
    res_email = session_data[5]
    check_in_date = session_data[6]
    check_out_date = session_data[7]
    no_of_guests = session_data[8]
    todays_date = session_data[9]
    room_price = session_data[10]
    reservation_price = session_data[11]

    if request.method == "POST":

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO reservations(Room_type, Room_id, User_id, First_name, Last_name, Email, Check_in_date, Check_out_date, Guests, Reservation_date, Room_price, Reservation_price)\
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(room_type, max_value + 1, user_id, res_fname, res_lname, res_email, check_in_date, check_out_date, no_of_guests, todays_date, room_price, reservation_price))         
        mysql.connection.commit()
        return redirect(url_for('confirmation'))

    return render_template('checkout.html')

@app.route('/confirmation')
def confirmation():
        
    res_email = session.get('user_info', [])[5]

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM reservations WHERE email=%s AND Reservation_id = (SELECT MAX(Reservation_id) FROM reservations WHERE email=%s);",(res_email, res_email,))

    confirmation = cur.fetchall()       
    session['my_list'] = confirmation
    session.modified = True
    return render_template('confirmation.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
   
    if request.method == "POST":
      
        userDetails = request.form           
        feedback_fname = userDetails['fname']
        feedback_lname = userDetails['lname']
        feedback_email = userDetails['email']
        feedback_text = userDetails['feedback']     

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users WHERE email=%s",(feedback_email,))   
        email_result = cur.fetchone()

        if 'user_id' in session:
            user_id = session['user_id'] 
        elif email_result:
            user_id = email_result['User_id']
        else:
            user_id = 0

        cur.execute("INSERT INTO feedback(User_id, First_name, Last_name, Email, Feedback)\
        VALUES(%s, %s, %s, %s, %s)",(user_id, feedback_fname, feedback_lname, feedback_email, feedback_text))         
        mysql.connection.commit()

        flash("Thank you for leaving feedback, you may view it below.")
        return redirect(url_for('feedback'))      

    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM feedback")
    results = cur.fetchall()
    return render_template('feedback.html',results=results)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == "POST":
        # Fetch form data
        userDetails = request.form
        first_name = userDetails['fname']
        last_name = userDetails['lname']
        email = userDetails['email']
        password = userDetails['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        cur = mysql.connection.cursor()
        
        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        result = cur.fetchone()
            
        if result == None:  
            cur.execute("INSERT INTO users (Role, First_name, Last_name, Email, Password) VALUES(%s, %s, %s, %s, %s)",('user', first_name, last_name, email, hash_password))
            mysql.connection.commit()
            flash('Successfully created account. You may now login.')
            return redirect(url_for('create_account'))
        else:
            flash('Email already in use')
            return redirect(url_for('create_account'))

    return render_template('create_account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

  if 'role' in session: 
    return render_template('isLoggedIn.html')

  if request.method == "POST":
    # Fetch form data
    userDetails = request.form
    email = userDetails['email']
    password = userDetails['password'].encode('utf-8')

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM users WHERE email=%s",(email,))
    user = cur.fetchone()

    cur.close()

    if user == None:
      flash('Invalid Login Credentials. Please enter your details again.')
      return redirect(url_for('login'))
    
    elif len(user) > 0:
      role = (user['Role'])
      name = (user['First_name'])
      user_id = (user['User_id'])

      if bcrypt.hashpw(password, user['Password'].encode('utf-8')) == user['Password'].encode('utf-8'):
        session['user_id'] = user_id
        session['email'] = email 
        session['role'] = role
        session['name'] = name
        return redirect(url_for('reservation'))
      else:          
          flash('Invalid Login Credentials. Please enter your details again.')
          return redirect(url_for('login'))              

  return render_template('login.html')

@app.route('/logout')
def logout():

  if 'user_id' in session:
    session.pop('user_id')
    session.pop('email')
    session.pop('role') 
    flash('Bye ' + session.pop('name') + ', See you soon!')

  return redirect(url_for('login'))

@app.route('/my_reservations', methods=['GET', 'POST'])
def my_reservations():

  if session and 'user_id' in session:
    user_id = session['user_id'] 
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM reservations WHERE User_id = %s",(user_id,))
    results = cur.fetchall()
    return render_template('my_reservations.html', results=results)
    
  return render_template('notLoggedIn.html')

@app.route('/my_feedback')
def my_feedback():
        
  if session and 'user_id' in session:
    user_id = session['user_id'] 
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM feedback WHERE User_id = %s",(user_id,))
    results = cur.fetchall()
    return render_template('my_feedback.html', results=results)
  
  return render_template('notLoggedIn.html')

@app.route('/special_offers', methods=['GET', 'POST'])
def special_offers():

  if (not session) or (not 'user_id' in session):
    return render_template('notLoggedIn.html')

  elif session['role'] != 'admin':
    return render_template('adminBlock.html')

  else:
    if request.method == "POST":
      userDetails = request.form
      offer_type = userDetails['offer']

      if 'offer_type' not in session:
        session['offer_type'] = offer_type    
      elif session['offer_type'] != offer_type:
        session.pop('offer_type')
        session['offer_type'] = offer_type       
      else:
        session.pop('offer_type')
      
      return redirect(url_for('special_offers'))

    return render_template('special_offers.html')

@app.route('/reservation_history', methods=['GET', 'POST'])
def reservation_history():

  if (not session) or (not 'user_id' in session):
    return render_template('notLoggedIn.html')

  elif session['role'] != 'admin':
    return render_template('adminBlock.html')
  
  else:
    if request.method == "POST":
      userDetails = request.form
      delete_res = userDetails['delete_res']

      cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cur.execute("SELECT * FROM reservations WHERE Reservation_id = %s", (delete_res,))
      result = cur.fetchone()

      if result is not None:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("DELETE FROM reservations WHERE Reservation_id = %s", (delete_res,))
        mysql.connection.commit()
        flash("Reservation " + delete_res + " canceled")
        return redirect(url_for('reservation_history'))

      else: 
        flash("Reservation " + delete_res + " does not exist")
        return redirect(url_for('reservation_history'))
        
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM reservations")
    results = cur.fetchall()

  return render_template('reservation_history.html', results=results)

if __name__ == "__main__":
  app.secret_key = os.getenv('SECRET_KEY')
  app.run(debug=True)