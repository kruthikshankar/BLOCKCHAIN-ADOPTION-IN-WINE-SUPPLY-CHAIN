import os
import MySQLdb
import smtplib
import random
import string
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, send_file

from database import db_connect,owner_reg,owner_login,ac_act1,c_login1,cvp1,cvp_act,con_act
# from cloud import uploadFile,downloadFile,close
from database import db_connect,ap_act,p_login,ad_act,d_login,ar_act,r_login,addp_act,dvp1,dvp3,rvp1,rvp3,s_act
from sendmail import sendmail
from main import generateblockchain


# def db_connect():
#     _conn = MySQLdb.connect(host="localhost", user="root",
#                             passwd="root", db="assigndb")
#     c = _conn.cursor()

#     return c, _conn


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")


@app.route("/producer.html")
def producer():
    return render_template("producer.html")

@app.route("/search.html")
def search():
    return render_template("search.html")

@app.route("/consumer.html")
def consumer():
    return render_template("consumer.html")

@app.route("/distb.html")
def distb():
    return render_template("distb.html")

@app.route("/phome.html")
def phome():
    return render_template("phome.html")


@app.route("/dhome.html")
def dhome():
    return render_template("dhome.html")

@app.route("/re.html")
def re():
    return render_template("re.html")


@app.route("/addp.html")
def addp():
    return render_template("addp.html")

@app.route("/ad.html")
def ad():
    return render_template("ad.html")

@app.route("/ac.html")
def ac():
    return render_template("ac.html")

@app.route("/ar.html")
def ar():
    return render_template("ar.html")

@app.route("/ap.html")
def ap():
    return render_template("ap.html")



@app.route("/dvp.html")
def dvp():
    data = dvp1()
    print(data)
    return render_template("dvp.html",data = data)



@app.route("/cvp.html")
def cvp():
    data = cvp1()
    print(data)
    return render_template("cvp.html",data = data)

@app.route("/rvp.html")
def rvp():
    data = rvp1()
    print(data)
    return render_template("rvp.html",data = data)




#-----------
    

@app.route("/ohome.html")
def ohome():
    return render_template("ohome.html")





@app.route("/owner.html")
def owner():
    return render_template("owner.html")

@app.route("/ownerreg.html")
def ownerreg():
    return render_template("ownerreg.html")






@app.route("/increg.html")
def increg():
    return render_template("increg.html")





@app.route("/index")
def index():
    return render_template("index.html") 



 #--------------code


@app.route("/dvp2", methods = ['GET','POST'])
def dvp2():
    a = request.args.get('a')
    b = request.args.get('b')
    username = session['username']
    atas,key=generateblockchain(username,username)
    print("blockchain")
    print(key)  
    key2  = key
    dvp3(a,b,username,key2)
    return render_template("dhome.html")



@app.route("/cvp2.html", methods = ['GET','POST'])
def cvp2():
    a = request.args.get('a')
    b = request.args.get('b')
    c1 = request.args.get('c1')
    d = request.args.get('d')
    username = session['username']
    atas,key=generateblockchain(username,username)
    print("blockchain")
    print(key)  
    key2  = key
    return render_template("cvp1.html",a=a,b=b,c1=c1,d=d,key2=key2)


@app.route("/rvp2", methods = ['GET','POST'])
def rvp2():
    a = request.args.get('a')
    b = request.args.get('b')
    username = session['username']
    atas,key=generateblockchain(username,username)
    print("blockchain")
    print(key)  
    key2  = key
    rvp3(a,b,username,key2)
    return render_template("rhome.html")


  
# -------------------------------Registration-----------------------------------------------------------------    






@app.route("/oregact", methods = ['GET','POST'])
def oregact():
   if request.method == 'POST':    
      
      status = owner_reg(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("owner.html",m1="sucess")
      else:
       return render_template("ownerreg.html",m1="failed")



@app.route("/apact", methods = ['GET','POST'])
def apact():
   if request.method == 'POST':    
      
      status = ap_act(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("ap.html",m1="sucess")
      else:
       return render_template("ap.html",m1="failed")
      
@app.route("/addpact", methods = ['GET','POST'])
def addpact():
   if request.method == 'POST':
    
      pid = request.form['pid'] 
      pname = request.form['pname'] 
      price = request.form['price'] 
      image = request.form['image'] 
      username = session['username']
      atas,key=generateblockchain(username,username)
      print("blockchain")
      print(key)  
      key2  = key
       
      
      status = addp_act(pid,pname,price,image,request,username,key2)
      
      if status == 1:
       return render_template("addp.html",m1="sucess")
      else:
       return render_template("addp.html",m1="failed")
      

@app.route("/cvp3", methods = ['GET','POST'])
def cvp3():
   if request.method == 'POST':
    
      pid = request.form['pid'] 
      pname = request.form['pname'] 
      price = request.form['price'] 
      image = request.form['image'] 
      key2 = request.form['key2'] 
      username = session['username']
      
      status = cvp_act(pid,pname,price,image,username,key2)
      
      if status == 1:
       return render_template("purchase.html",data="purchased succesfully",product=pname,price=price,image=image,bc=key2)
      else:
       return render_template("cvp.html",m1="failed")
      

@app.route("/searchact", methods = ['GET','POST'])
def searchact():
   if request.method == 'POST':
    
      pid = request.form['pid']
      
      data = s_act(pid)
      data1 = con_act(pid)
      return render_template("search1.html",m1="sucess",data=data,data1=data1)


      
@app.route("/aract", methods = ['GET','POST'])
def aract():
   if request.method == 'POST':    
      
      status = ar_act(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("ar.html",m1="sucess")
      else:
       return render_template("ar.html",m1="failed")


@app.route("/adact", methods = ['GET','POST'])
def adact():
   if request.method == 'POST':    
      
      status = ad_act(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("ad.html",m1="sucess")
      else:
       return render_template("ad.html",m1="failed")


@app.route("/acact", methods = ['GET','POST'])
def acact():
   if request.method == 'POST':    
      
      status = ac_act1(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("ac.html",m1="sucess")
      else:
       return render_template("ac.html",m1="failed")



      
# #-------------------------------ADD_END---------------------------------------------------------------------------
# # -------------------------------Loginact-----------------------------------------------------------------






@app.route("/ologin", methods=['GET', 'POST'])       
def ologin():
    if request.method == 'POST':
        status = owner_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("ohome.html", m1="sucess")
        else:
            return render_template("owner.html", m1="Login Failed")


@app.route("/plogin", methods=['GET', 'POST'])       
def plogin():
    if request.method == 'POST':
        status = p_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("phome.html", m1="sucess")
        else:
            return render_template("producer.html", m1="Login Failed")

@app.route("/rlogin", methods=['GET', 'POST'])       
def rlogin():
    if request.method == 'POST':
        status = r_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("rhome.html", m1="sucess")
        else:
            return render_template("re.html", m1="Login Failed")


@app.route("/dlogin", methods=['GET', 'POST'])       
def dlogin():
    if request.method == 'POST':
        status = d_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("dhome.html", m1="sucess")
        else:
            return render_template("distb.html", m1="Login Failed")


@app.route("/clogin", methods=['GET', 'POST'])       
def clogin():
    if request.method == 'POST':
        status = c_login1(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("chome.html", m1="sucess")
        else:
            return render_template("consumer.html", m1="Login Failed")

        



# # -------------------------------Loginact End-----------------------------------------------------------------


   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
