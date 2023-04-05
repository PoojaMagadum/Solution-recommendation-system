from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np



app=Flask(__name__,template_folder='template')
cors=CORS(app)
model= pickle.load(open('lr.pkl','rb'))
df=pd.read_csv('incident.csv')

@app.route('/',methods=['GET','POST'])
def index():
    product=sorted(df['Product'].unique())
    objects=sorted(df['Business object'].unique())
    issues=sorted(df['Issue'].unique())

    product.insert(0,'Select Product')




    return render_template('index.html',product=product, objects=objects, Issues=issues)


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    product=request.form.get('product')

    objects=request.form.get('objects')
    issues=request.form.get('issues')

    #print(product,objects,issues)

    prediction = model.predict(pd.DataFrame([[product,objects,issues]],columns=['Product','Business object','Issue']))
    predict = str(prediction)
    pred = str(predict)



    return pred


if __name__=='__main__':
    app.run(debug=True)