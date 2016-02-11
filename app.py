from flask import Flask, redirect, url_for, send_from_directory
from flask import render_template
from flask import request 
from werkzeug import secure_filename
import os
app = Flask(__name__)

#uploaded faces' directory
app.config['UPLOAD_FOLDER'] = 'faces/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

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
		return render_template("main/picture.html",link=test)
		return "Well done! You managed to connect to TechSoc's IoT Server"
	else:
		return "Heard a get request"

@app.route("/get")
def send():
	return "Yes, I hear you loud and clear"

#picture upload files
@app.route('/upload_face')
def upload_face():
	return render_template("face_recog.html")

@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']
	filename = secure_filename(file.filename)
	#save file into the folder
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	#showing the user uploaded file
	return redirect(url_for('uploaded_face',filename = filename))

@app.route('/uploads/<filename>')
def uploaded_face(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)	




if __name__ == "__main__":
	app.run(debug=True)
