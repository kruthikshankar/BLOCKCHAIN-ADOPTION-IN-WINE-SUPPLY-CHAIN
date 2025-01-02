import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from flask import Flask, request, send_file
import io
import base64

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="bcc")
    c = _conn.cursor()

    return c, _conn



# -------------------------------Registration-----------------------------------------------------------------




def owner_reg(username,password,email,address):
    try:
        c, conn = db_connect()
        print(username,password,email,address)
        id="0"
        status = "pending"
        j = c.execute("insert into owner (id,username,password,email,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def ap_act(username,password,email,address):
    try:
        c, conn = db_connect()
        print(username,password,email,address)
        id="0"
        status = "pending"
        j = c.execute("insert into producer (id,username,password,email,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def ar_act(username,password,email,address):
    try:
        c, conn = db_connect()
        print(username,password,email,address)
        id="0"
        status = "pending"
        j = c.execute("insert into re (id,username,password,email,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def ad_act(username,password,email,address):
    try:
        c, conn = db_connect()
        print(username,password,email,address)
        id="0"
        status = "pending"
        j = c.execute("insert into distb (id,username,password,email,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def ac_act1(username,password,email,address):
    try:
        c, conn = db_connect()
        print(username,password,email,address)
        id="0"
        status = "pending"
        j = c.execute("insert into consumer (id,username,password,email,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def addp_act(pid,pname,price,image,request,username,key2):
    try:
        c, conn = db_connect()
        print(pid,pname,price,image,request,username,key2)
        id="0"
        status = "pending"
        j = c.execute("insert into product (pid,pname,price,image,producer,bc,distb,bc1,re,bc2) values ('"+pid +
                      "','"+pname+"','"+price+"','"+image+"','"+username+"','"+key2+"','pendng','pendng','pendng','pendng')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def cvp_act(pid,pname,price,image,username,key2):
    try:
        c, conn = db_connect()
        print(pid,pname,price,image,username,key2)
        id="0"
        status = "pending"
        j = c.execute("insert into purchase (pid,pname,price,image,username,key2) values ('"+pid +
                      "','"+pname+"','"+price+"','"+image+"','"+username+"','"+key2+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


# def vp():
#     c, conn = db_connect()
#     c.execute("select * from owner ")
#     result = c.fetchall()
#     conn.close()
#     print("result")
#     return result









    






#******

def dvp1():
    c, conn = db_connect()
    c.execute("select * from product where bc1='pendng' and bc!='pendng' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def cvp1():
    c, conn = db_connect()
    c.execute("select * from product where bc2!='pendng' and bc1!='pendng' and bc!='pendng' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def s_act(pid):
    c, conn = db_connect()
    c.execute("select * from product where pid='"+pid+"' ")
    result = c.fetchall()
    conn.close()
    print(result)
    print("result")
    return result

def con_act(pid):
    c, conn = db_connect()
    c.execute("select * from purchase where pid='"+pid+"' ")
    result = c.fetchall()
    conn.close()
    print(result)
    print("result")
    return result


def rvp1():
    c, conn = db_connect()
    c.execute("select * from product where bc2='pendng' and bc!='pendng' and bc1!='pendng'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def dvp3(a,b,username,key2):
    try:
        c, conn = db_connect()
        id="0"
        
        j = c.execute("update product set distb='"+username+"',bc1='"+key2+"' where pid='"+a+"' and pname='"+b+"' ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    


def rvp3(a,b,username,key2):
    try:
        c, conn = db_connect()
        id="0"
        
        j = c.execute("update product set re='"+username+"',bc2='"+key2+"' where pid='"+a+"' and pname='"+b+"' ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

# # -------------------------------Registration End-----------------------------------------------------------------
# # -------------------------------Loginact Start-----------------------------------------------------------------








def owner_login(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from owner where username='" +
                      username+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))
    

def p_login(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from producer where username='" +
                      username+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))
    

def d_login(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from distb where username='" +
                      username+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))
    

def c_login1(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from consumer where username='" +
                      username+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))
    
def r_login(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from re where username='" +
                      username+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))


if __name__ == "__main__":
    print(db_connect())
