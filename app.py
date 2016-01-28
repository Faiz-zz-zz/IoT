from flask import Flask
from flask import render_template
from flask import request 
app = Flask(__name__)

@app.route("/")
def index():
	return "Well done! You managed to connect to TechSoc's IoT Server" #render_template("main/index.html")

@app.route("/send/<message>")
def recieve(message):
	return render_template("main/send.html",message=message)

@app.route("/send_picture/<link>")
def send_picture(link):
	return render_template("main/picture.html",link=link)


@app.route("/testsomething",methods=['GET', 'POST'])
def send_string():
	if request.method == 'POST':
		print request.form['test']
		return send_picture(request.form['test'])
		#return render_template("main/picture.html",link=test)
		#return "Well done! You managed to connect to TechSoc's IoT Server"
	else:
		return "Heard a get request"

@app.route("/get")
def send():
	return "Yes, I hear you loud and clear"

if __name__ == "__main__":
	app.run(debug=True)
