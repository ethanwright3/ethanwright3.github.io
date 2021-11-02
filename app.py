#Not actually planning on using this I just keep it just in case
#Deleted stuff from https://www.askpython.com/python-modules/flask/flask-mysql-database
import pymysql
from flask import Flask,render_template, request
app = Flask(__name__)

conn = pymysql.connect(
        host= 'database-1-instance-1.coig4wr2sngc.us-east-2.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = '88888888',
        db = 'icuneedbeds',
        )


# #insert query
# def insert_details(name,email,comment,gender):
#     cur=conn.cursor()
#     cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
#     conn.commit()
#read the data
def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictionDashboard/')
def predictionDashboard():
    return render_template('predictionDashboard.html')

@app.route('/dataDisplay/')
def dataDisplay():
    return render_template('dataDisplay.html')

@app.route('/mainDashboard/')
def mainDashboard():
    return render_template('mainDashboard.html')

@app.route('/insert')
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['optradio']
        comment = request.form['comment']
        db.insert_details(name,email,comment,gender)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        return render_template('dataDisplay.html',var=var)
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()