from ast import main
import flask
from flask import request, render_template
from flask_cors import CORS
import requests
API_KEY = "F6vTzfQddI_tNuvMuGjiv9-b9Ter6rDuTIeL9sM8yPMq"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
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
    input=[input[1::]]
    payload_scoring = {"input_data": [{"field": [col_names], "values": input}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/failiure_prediction/predictions?version=2022-11-17', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
    predictions=response_scoring.json()
    # print(predictions)
    result=predictions['predictions'][0]['values'][0][0]
    if result==1:
        
        return render_template('predict.html',predict="<div class=\"alert alert-danger\" role=\"alert\"><h4 class=\"alert-heading\">Fail!</h4><p>Aircraft engine with these parameters may fail within 30 Days. </p><hr><p class=\"mb-0\"></p></div>")
    else:
        return render_template('predict.html',predict="<div class=\"alert alert-success\" role=\"alert\"><h4 class=\"alert-heading\">Not Fail!</h4><p>Aircraft engine with these parameters will not fail within 30 Days. </p><hr><p class=\"mb-0\"></p></div>")
if __name__=='__main__':
    app.run(debug=True)