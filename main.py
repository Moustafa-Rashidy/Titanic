from flask import Flask,request,render_template,jsonify
from flask_cors import cross_origin
import pickle

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def page():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def home():
    if request.method =='POST':
        Pclass = float(request.form['Pclass'])
        Sex = float(request.form['Sex'])
        Age = float(request.form['Age'])
        SibSp = float(request.form['SibSp'])
        Parch = float(request.form['Parch'])
        Fare = float(request.form['Fare'])


        #load file
        file = 'Dt Titanic.pkl'
        load = pickle.load(open(file,'rb'))
        predict = load.predict([[Pclass,Sex,Age,SibSp,Parch,Fare]])

        return render_template('results.html',predict=predict[0])
if __name__ =='__main__':
    app.debug = True
    app.run()