from flask import Flask, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
# filename ='ATL25OCT22.pkl'
# fbrList = pickle.load(open(filename, 'rb'))

@app.route("/")
def index():
    return ''' 
<form action="/info" method="POST">
<input type="text" name="user" placeholder="Full Name"><br>
<input type="text" name="cnic" placeholder="Enter Your CNIC Number"><br>
<input type="submit" value="Send">
</form>
'''

@app.route("/info",methods=['GET','POST'])
def info():
    outList = []
    outList = GetFilerStatus(request.form['cnic'])

    if request.method == "GET":
        return "<h1>GET Method</h1>Hello "+ request.args.get('user') + " Your Email:"+request.args.get('cnic')
    else:
        return "<h1>POST Method</h1>Hello "+ request.form['user'] + \
    " Your CNIC:"+ outList[0] + "CNIC Holder Name :" + outList[1] + \
    " Your CNIC:"+ outList[0] + "CNIC Holder Name :" + outList[1] + \
    " FRB Status"+ outList[2]
    

def GetFilerStatus(p_cnic):
    vList = []
    # import os
    # print(os.getcwd())
    fbrList = pd.read_pickle("D:/Online Education/Data Science/Artificial Intellengence/Saylani-AI-Course/07-Flask/FirstPage/ATL25OCT22.pkl") 
   
    if fbrList[fbrList['NTN'] == p_cnic].empty == True:
        vList.append('CNIC Number = ' + p_cnic)
        vList.append('Name  =  Unknown')
        vList.append('Filer Status = Non Filer')
    else:
        vList.append('CNIC Number = ' + p_cnic)
        vList.append('Name  =  '+ fbrList[fbrList['NTN'] == p_cnic].iloc[0,2])
        vList.append('Filer Status =  Filer')
        
        return vList

app.run(debug=True)