#!/root/flask_projects/test_proj/venv/bin/python2.7
# vim: set fileencoding= utf-8
from flask import Flask, redirect, url_for, render_template,request
import key
import boto

app = Flask(__name__)

conn = boto.connect_iam(aws_access_key_id=key.acc_tok,aws_secret_access_key=key.acc_sec)

@app.route('/')
def hello_world():
        return render_template("index.html")


@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method == "POST":
		age=request.form['age']
		return render_template('age.html', age=age)
	return render_template('index.html')


@app.route('/get_all_users', methods=['GET', 'POST'])
def get_all_users():
	if request.method == "GET":
		d = conn.get_all_users()
        	return render_template("mand.html", nums=d)


@app.route('/get_all_groups', methods=['GET', 'POST'])
def get_all_groups():
	if request.method == "GET":
		d = conn.get_all_groups()
        	return render_template("mand1.html", num=d)

if __name__ == "__main__":
        app.run(debug=True)

