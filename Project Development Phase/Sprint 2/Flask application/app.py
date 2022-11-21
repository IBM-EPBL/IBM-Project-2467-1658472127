from ast import main
import flask
from flask import request, render_template
from flask_cors import CORS
import pickle
model=pickle.load(open('engine_model_new.sav','rb'))
app=flask.Flask(__name__, static_url_path='')
CORS(app)

@app.route('/',methods=['GET'])
def sendHomePage():
    return render_template('index.html')

@app.route("/predict.html",methods=['POST'])
def predictFailiure():
    col_names=['id', 'cycle', 'setting1','setting2','setting3','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19','s20','s21']
    input=[]
    for feature in col_names:
        input.append(request.form[feature])
    result=model.predict([input[1::]])
    if result[0]==1:
        
        return render_template('predict.html',predict="<div class=\"alert alert-danger\" role=\"alert\"><h4 class=\"alert-heading\">Fail!</h4><p>Aircraft engine with these parameters may fail within 30 Days. </p><hr><p class=\"mb-0\"></p></div>")
    else:
        return render_template('predict.html',predict="<div class=\"alert alert-success\" role=\"alert\"><h4 class=\"alert-heading\">Not Fail!</h4><p>Aircraft engine with these parameters will not fail within 30 Days. </p><hr><p class=\"mb-0\"></p></div>")
if __name__=='__main__':
    app.run(debug=True)