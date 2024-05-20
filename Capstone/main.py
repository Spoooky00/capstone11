import os.path

import pymysql.cursors

from app import app
from config import mysql
from flask import Flask, render_template, request, redirect, jsonify, session


# Route to render the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM login WHERE Em_ID = %s AND Em_password = %s AND Em_Status=1',
                       (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['Em_ID']
            # Redirect to home page
            print("TEST LOGIN")
            return redirect('/clinic_admin')
        else:
            msg = 'INCORRECT CREDENTIALS!'
    return render_template('login/login.html')


# Route ro render the log out
##LOGOUT ROUTE
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    # Redirect to login page
    return redirect('/')


# Route to render the clinic_admin page
@app.route('/clinic_admin',methods=['GET'])
def dashboard():
    if 'loggedin' in session:
        return render_template('clinic_admin.html')
    else:
        return redirect('/')


# Route to render the events page
@app.route('/events',methods=['GET'])
def events():
    if 'loggedin' in session:
        print("TEST EVENTS")
        return render_template('events_appointments.html')
    else:
        return redirect('/')


# Route to render the account_management page
@app.route('/account_management', methods=['GET', 'POST'])
def account_management():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT* from `account_management`")
            accountmanagement = cursor.fetchall()
            print(accountmanagement)
            return render_template('account_management/account_management2.html', data=accountmanagement)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")


# update
@app.route('/updateAM/<int:id>', methods=['GET', 'POST'])
def updateAM(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `account_management` where Am_ID = %s", id)
        accountmanagement = cursor.fetchall()
        print(accountmanagement)
        return render_template('account_management/updateAM.html', data=accountmanagement)
    if request.method == 'POST':
        _Username = request.form['Username']
        _Password = request.form['Password']
        _Email = request.form['Email']
        _Role = request.form['Role']

        if request.form:
            query = "update account_management set Username=%s , Email=%s, Password=%s, Role=%s where Am_ID=%s"
            bindData = (_Username, _Email, _Password, _Role, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/account_management')


# add
@app.route('/addAM', methods=['GET','POST'])
def addAM():
    if request.method == 'POST':
        print("result : " + str(request.json))
        _name = request.json['AM_User_name']
        _Email = request.json['AM_Email']
        _Role = request.json['AM_Role']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into account_management(Username,Email,Role) values(%s,%s,%s)"
            bindData = (_name, _Email, _Role)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/account_management')
    else:
         return render_template('account_management/addAM.html')

# Route to render the patient_masters_record page
@app.route('/Pmr', methods=['GET', 'POST'])
def Pmr():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT* from `pmr` ")
            pmr = cursor.fetchall()
            print(pmr)
            return render_template('Pmr.html', data=pmr)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")


# update
@app.route('/updatePmr/<int:id>', methods=['GET', 'POST'])
def updatePmr(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `pmr` where User_NFC_ID = %s")
        pmr = cursor.fetchall()
        print(pmr)
        return render_template('pmr/updatePmr.html', data=pmr)
    if request.method == 'POST':
        _NFC = request.form['NFC']
        _Fname = request.form['PMR_Fname']
        _Lname = request.form['PMR_Lname']
        _Section = request.form['PMR_Section']
        _Lvl = request.form['PMR_Yr_Lvl']
        _DB = request.form['PMR_DB']
        _Address = request.form['PMR_Address']
        _Gender = request.form['PMR_Gender']
        _BT = request.form['PMR_BT']
        _LUD = request.form['PMR_LUD']
        _ECN = request.form['PMR_ECN']
        _RTTP = request.form['PMR_RTTP']
        _ECNO = request.form['PMR_ECNO']
        _HI = request.form['PMR_HI']



        if request.form:
            query = "update account_management set PMR_Fname=%s , PMR_Lname=%s, PMR_Section=%s, PMR_Yr_Lvl=%s , PMR_DB=%s, PMR_Address=%s, PMR_Gender=%s, PMR_BT=%s, PMR_LUD=%s, PMR_ECN=%s, PMR_RTTP=%s, PMR_ECNO=%s, PMR_HI=%s where User_NFC_ID=%s"
            bindData = (_NFC,  _Fname, _Lname,_Section,_Lvl,_DB,_Address, _Gender, _BT,_LUD,_ECN ,_RTTP, _ECNO,_HI,id)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/pmr')


# add
@app.route('/addPmr', methods=['GET','POST'])
def addPmr():
    if request.method == 'POST':
        print("result : " + str(request.json))
        _Username = request.json['Username']
        _Email = request.json['Email']
        _Role = request.json['Role']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into account_management(Username,Email,Role) values(%s,%s,%s)"
            bindData = (_Username, _Email, _Role)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/account_management')
    else:
         return render_template('account_management/addAM.html')

#########################DAILY LOGS ROUTES
# Route to render the daily_logs page
@app.route('/daily_logs', methods=['GET', 'POST'])
def daily_logs():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(
                "SELECT* from `pmr` JOIN `daily_logs` on `pmr`.`User_NFC_ID` = `daily_logs`.`User_NFC_ID`;")
            dailylogs = cursor.fetchall()
            print(dailylogs)
            return render_template('daily_logs/daily_logs.html', data=dailylogs)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")


# update
@app.route('/updateDL/<int:id>', methods=['GET', 'POST'])
def updateDL(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `pmr` JOIN `daily_logs` on `pmr`.`User_NFC_ID` = `daily_logs`.`User_NFC_ID` where `DL_ID`=%s;",
            id)
        dailylogs = cursor.fetchall()
        print(dailylogs)
        return render_template('daily_logs/updateDl.html', data=dailylogs)
    if request.method == 'POST':
        _NFC = request.form['NFC']
        _Concern = request.form['DL_Concern']
        _TI = request.form['DL_TI']
        _TO = request.form['DL_TO']
        if request.form:
            query = "update daily_logs set DL_Concerm=%s, DL_Timein=%s, DL_Timeout=%s where DL_ID=%s"
            bindData = (_Concern, _TI, _TO, _NFC)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/daily_logs')


# add
@app.route('/addDL', methods=['POST'])
def addDL():
    if request.method == 'POST':
        print("result : " + str(request.json))
        _nfc = request.json['nfc']
        _concern = request.json['concern']
        _ti = request.json['ti']
        _to = request.json['to']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into daily_logs(USER_NFC_ID,DL_Concerm,DL_Timein,DL_Timeout) values(%s,%s,%s,%s)"
            bindData = (_nfc, _concern, _ti, _to)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/daily_logs')
    # render_template('addDL.html')


#########################INVENTORY ROUTES
# Route to render the inventory page
@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT* from `inventory`")
            inventory = cursor.fetchall()
            print(inventory)
            return render_template('Inventory/Inventory.html', data=inventory)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")


# update
@app.route('/updateinventory/<int:id>', methods=['GET', 'POST'])
def updateinventory(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `inventory` where Item_ID = %s", id)
        inventory = cursor.fetchall()
        print(inventory)
        return render_template('inventory/updateInventory.html', data=inventory)
    if request.method == 'POST':
        _name = request.form['Item_name']
        _Quantity = request.form['Quantity']
        _Manufacturer = request.form['Manufacturer']
        _Description = request.form['Description']
        _code = request.form['Item_code']
        _expiry = request.form['Item_expiry']
        _type = request.form['Item_type']

        if request.form:
            query = "update inventory set Item_name=%s, Quantity=%s ,Manufacturer=%s , Description=%s , Item_code=%s , Item_expiry=%s , Item_type=%s  where Item_ID = %s"
            bindData = (_name, _Quantity, _Manufacturer, _Description, _code, _expiry, _type, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/inventory')


# add
@app.route('/addinventory', methods=['GET','POST'])
def addinventory():
    if request.method == 'POST':
        print("result : " + str(request.json))
        _name = request.form['name']
        _quantity = request.form['quantity']
        _manufacturer = request.form['manufacturer']
        _description = request.form['description']
        _code = request.form['code']
        _expiry = request.form['expiry']
        _type = request.form['type']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into inventory(Item_name,Quantity,Manufacturer,Description,Item_code,Item_expiry,Item_type) values(%s,%s,%s,%s,%s,%s,%s)"
            bindData = (_name, _quantity, _manufacturer, _description, _code, _expiry, _type)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/inventory')
    else:
         return render_template('inventory/addinventory.html')


if __name__ == '__main__':
    app.run(debug=True)
