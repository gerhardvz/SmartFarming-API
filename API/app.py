import os

from flask import Flask, request, Response,send_file
import cv2
import jsonpickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello There!"


@app.route('/ML/Image',methods=['POST','GET'])
def getSetImage():
    r = request
    if request.method == 'POST':

        # convert string of image data to uint8
        img = r.files['data']
        if( len(os.listdir("./img/"))>4):
            oldest = min(os.listdir("./img/"), key=lambda p: os.path.getctime(os.path.join("./img/", p)))
            os.remove("./img/"+oldest)
        img.save("./img/"+img.filename)

        #pass img to ML Model to predict
        response = {'message':'It is working','datasets':r.form.to_dict()}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled,status=200,mimetype="application/json")

    pos = r.form.to_dict()['Pos']
    img = os.listdir("./img/").index(pos)

    return send_file(img,mimetypes='image/JPEG')



@app.route('/ML/Prediction',methods=['POST'])
def getMLResult():
    r = request
    # convert string of image data to uint8
    img = r.files['data']
    if( len(os.listdir("./img/"))>4):
        oldest = min(os.listdir("./img/"), key=lambda p: os.path.getctime(os.path.join("./img/", p)))
        os.remove("./img/"+oldest)
    img.save("./img/"+img.filename)

    #pass img to ML Model to predict
    response = {'message':'It is working','datasets':r.form.to_dict()}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled,status=200,mimetype="application/json")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
 