from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/send/<message>")
def recieve(message):
	return render_template("recieve.html",message=message)

@app.route("/get")
def send():
	return "Yes, I hear you loud and clear"

if __name__ == "__main__":
	app.run(debug=True)
