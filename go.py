from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/user')
def user():
	return render_template('user.html')

@app.route('/home',methods=['POST','GET'])
def home():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['pass']
		accesscode = request.form['code']

		with sql.connect("Form.db") as con:
			cur = con.cursor()

			cur.execute(" SELECT Email,Password,AccessCode FROM Signup WHERE Email = ? and Password = ? and AccessCode= ?", (username, password,accesscode))

			con.commit()
			if  cur.fetchone() is not None:
				return render_template("main.html")


@app.route('/admin',methods=['POST','GET'])
def admin():
	if request.method == 'POST':
		username = request.form['uname']
		password = request.form['pwd']

		with sql.connect("Form.db") as con:
			cur = con.cursor()

			cur.execute("SELECT Username,Password FROM Admin WHERE Username = ? and Password = ?", (username, password))

			con.commit()
			if  cur.fetchone() is not None:
				return render_template("main.html")




@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/forget')
def forget():
	return render_template("forget.html")

@app.route('/sign')
def sign():
	return render_template("signup.html")

@app.route('/signup', methods=['POST','GET'])
def signup():
		if request.method == 'POST':
			try:
				firstname = request.form['FirstName']
				lastname = request.form['LastName']
				password = request.form['password']
				email = request.form['email']

				with sql.connect("Form.db") as con:
					cur = con.cursor()

					cur.execute(" INSERT INTO Signup (FirstName, LastName, Password, Email) VALUES (?,?,?,?)", (firstname, lastname, password, email))

					con.commit()
			except:
				con.rollback()
			finally:
				return render_template("signup.html")
				con.close()
	
if __name__ == '__main__':
	app.run(debug= True, host='127.0.0.1')