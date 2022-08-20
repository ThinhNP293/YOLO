from flask import Flask, render_template , request
import numpy as np, os
import cv2
import base64

from object_detection import object_detection

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
img_file = os.path.join("static/detected.jpg")

@app.route('/detect' , methods=['POST'])
def mask_image():
	file = request.files['image'].read()
	npimg = np.frombuffer(file, np.uint8)
	img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
	
	object_detection(img)

	#Render image from file saved
	with open(img_file, "rb") as f:
		img = f.read()

	img_base64 = str(base64.b64encode(img)).split('\'')[1]
	return render_template("index.html", img_data = img_base64)

@app.route('/', methods=['GET'])
def home():
	return render_template("index.html")


if __name__ == '__main__':
	app.run()