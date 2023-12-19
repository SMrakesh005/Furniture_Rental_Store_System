from abc import ABC , abstractmethod
from tkinter import *
from turtle import bgcolor
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
from datetime import datetime as dt
import math
import smtplib
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,  NavigationToolbar2Tk
import unittest
import os



class User(ABC):
    def __init__(self , name , phonenumber , address , signinid , password):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.__signinid = signinid
        self.__password = password
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getPhoneNumber(self):
        pass

    @abstractmethod
    def getAddress(self):
        pass

class Customer(User):
    def __init__(self, name , phonenumber , address , signinid , password , amountdue , numberoforders):
        super().__init__(name , phonenumber , address , signinid , password)
        self.__amountdue = amountdue
        self.__numberoforders = numberoforders
        pass

    def getAddress(self):
        return self.address
    
    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phonenumber


class Admin(User):

    profit = 0
    investment = 0

    def __init__(self, name , phonenumber , address , signinid , password):
        super().__init__(name , phonenumber , address , signinid , password)
        pass

    def getAddress(self):
        return self.address
    
    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phonenumber

class Furniture:
    def __init__(self , id , name , company , price , feedback , description , type , rented , photo , interestrate , timeframe ,userid = 0):
        self.__id = id
        self.__name = name
        self.__company = company
        self.__price = price
        self.__feedback = feedback
        self.__description = description
        self.__type = type
        self.__rented = rented
        self.__photo = photo
        self.__interestrate = interestrate
        self.__timeframe = timeframe
        pass
    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCompany(self):
        return self.__company

    def getPrice(self):
        return self.__price

    def getFeedback(self):
        return self.__feedback

    def getDescription(self):
        return self.__description

    def getType(self):
        return self.__type

    def getUserId(self):
        return self.__id

    def isRented(self):
        return self.__rented

    def getPhoto(self):
        return self.__photo

    def getInterestRate(self):
        return self.__interestrate

    def getTimeFrame(self):
        return self.__timeframe
    

class TestFurnitureMethods(unittest.TestCase):
    myfurniture = Furniture(1, "Center Table", "neelkamal", 4000, "Durable!", "Made of pure wood", "Table", 0, "Imagepath", 2, 365)
    
    def test_id(self):
        self.assertEqual(self.myfurniture.getId(), 1)
    
    def test_name(self):
        self.assertEqual(self.myfurniture.getName(), "Center Table")
    
    def test_Company(self):
        self.assertEqual(self.myfurniture.getCompany(), "neelkamal")
    
    def test_Price(self):
        self.assertEqual(self.myfurniture.getPrice(), 4000)
    
    def test_Feedback(self):
        self.assertEqual(self.myfurniture.getFeedback(), "Durable!")

    def test_Description(self):
        self.assertEqual(self.myfurniture.getDescription(), "Made of pure wood")

    def test_Type(self):
        self.assertEqual(self.myfurniture.getType(), "Table")

    def test_Photo(self):
        self.assertEqual(self.myfurniture.getPhoto(), "Imagepath")

    def test_Interestrate(self):
        self.assertEqual(self.myfurniture.getInterestRate(), 2)
    
    def test_Timeframe(self):
        self.assertEqual(self.myfurniture.getTimeFrame(), 365)

class TestAdminMethods(unittest.TestCase):
    my_admin = Admin("Saurav", "12345667", "india", "saurav123", "saurav")

    def test_name(self):
        self.assertEqual(self.my_admin.getName(), "Saurav")
    
    def test_PhoneNumber(self):
        self.assertEqual(self.my_admin.getPhoneNumber(), "12345667")
    
    def test_Adress(self):
        self.assertEqual(self.my_admin.getAddress(), "india")

class TestCustomerMethods(unittest.TestCase):
    my_customer = Customer("Saurav Likhar", "15667", "india", "saurav13", "saurav", 1200, 2)

    def test_name(self):
        self.assertEqual(self.my_customer.getName(), "Saurav Likhar")
    
    def test_PhoneNumber(self):
        self.assertEqual(self.my_customer.getPhoneNumber(), "15667")
    
    def test_Adress(self):
        self.assertEqual(self.my_customer.getAddress(), "india")


global user_id , pass_word , is_admin
def testsignup(username):
    ex = "SELECT * FROM customers WHERE username = %s"
    va = (username,)
    my_cursor1.execute(ex, va)
    res = my_cursor1.fetchall()
    ex = "SELECT * FROM admins WHERE username = %s"
    va = (username,)
    my_cursor1.execute(ex, va)
    re = my_cursor1.fetchall()
    if len(re) > 0 or len(res) > 0:
        print("User SIGN UP : PASSED")
    else:
        print("USER SIGN UP : FAIL")

def testdeleteuser(username):
    ex = "SELECT * FROM customers WHERE username = %s"
    va = (username,)
    my_cursor1.execute(ex, va)
    res = my_cursor1.fetchall()
    if len(res) == 0:
        print("User DELETE : PASSED")
    else:
        print("USER DELETE : FAILED")

def testnotdeleteduser(username):
    ex = "SELECT * FROM customers WHERE username = %s"
    va = (username,)
    my_cursor1.execute(ex, va)
    res = my_cursor1.fetchall()
    if len(res) == 0:
        print("User DELETE WITH AMOUNT DUE : FAILED")
    else:
        print("USER DELETE WITH AMOUNT DUE : PASSED")

def testaddfuniture(type, file):
    ex = "SELECT * FROM furnitures WHERE type = %s AND photo = %s"
    # print("type here" + type)
    # print("photo here" + file)
    va = (type , file)
    # print("vaaaa ", va)
    my_cursor1.execute(ex, va)
    res = my_cursor1.fetchall()
    mydb1.commit()
    # print(res)
    if len(res) < 1:
        print("ADD FURNITURE : FAILED here")
        return
    else:
        if res[0][5] == type:
            print("ADD FURNITURE : PASSED")
        else:
            print("ADD FURNITURE : FAILED")
        if res[0][7] == file:
            print("CORRECT PHOTO ADDED : PASSED")
        else:
            print("CORRECT PHOTO ADDED : FAILED")

def testinvestment(inv):
    exe = "SELECT SUM(investment) FROM admins"
    my_cursor1.execute(exe)
    investment = my_cursor1.fetchall()
    mydb1.commit()
    if float(investment[0][0]) == inv:
        print("INVESTMENT TEST : PASSED")
        pass
    else:
        print("INVESTMENT TEST : FAILED")

def testprofit(pro):
    exe = "SELECT SUM(profit) FROM admins"
    my_cursor1.execute(exe)
    profit = my_cursor1.fetchall()
    mydb1.commit()
    if float(profit[0][0]) == pro:
        print("PROFIT TEST : PASSED")
        pass
    else:
        print("PROFIT TEST : FAILED")
    pass


def testchangeprice(type, newprice):
    exe = "SELECT price FROM furnitures WHERE type = %s"
    va = (type,)
    my_cursor1.execute(exe, va)
    res = my_cursor1.fetchall()
    mydb1.commit()
    if(int(res[0][0]) == int(newprice)):
        print("CHANGE PRICE TEST : PASSED")
    else:
        print("CHANGE PRICE TEST : FAILED")


def testfurnituredelete(fur_id):
    exe = "SELECT * FROM furnitures WHERE id = %s"
    va = (fur_id,)
    my_cursor1.execute(exe, va)
    res = my_cursor1.fetchall()
    mydb1.commit()
    if len(res) > 0:
        print("DELETE DAMAGED FURNITURE : FAILED")
    else:
        print("DELETE DAMAGED FURNITURE : PASSED")

def testreadditionfurniture(fur_id):
    exe = "SELECT rented FROM furnitures WHERE id = %s"
    va = (fur_id,)
    my_cursor1.execute(exe, va)
    res = my_cursor1.fetchall()
    mydb1.commit()
    if (res[0][0]) != 0:
        print("READDITION FURNITURE : FAILED")
    else:
        print("READDITION FURNITURE : PASSED")

def testcustomeramountdue(username, amt):
    ex = "SELECT amountdue FROM customers WHERE username = %s"
    va = (username , )
    my_cursor1.execute(ex , va)
    res = my_cursor1.fetchall()[0][0]
    mydb1.commit()
    if amt != res:
        print("AMOUNT DUE TEST : FAILED")
    else:
        print("AMOUNT DUE TEST : PASSED")

def testpaymentdone(username, amount):
    ex = "SELECT amountdue FROM  customers WHERE username = %s"
    va = (username, )
    my_cursor1.execute(ex , va)
    res = my_cursor1.fetchall()
    mydb1.commit()
    if res[0][0] != amount:
        print("PAYMENT DONE : PASSED")
    else:
        print("PAYMENT DONE : FAILED")

def testfeedbackinsert(typ, feed):
    ex = "SELECT review FROM feedbacks WHERE type = %s"
    va = (typ ,)
    my_cursor1.execute(ex , va)
    res = my_cursor1.fetchall()
    mydb1.commit()
    if res[0][0] != feed:
        print("FEEDBACK INSERTED : FAILED")
    else:
        print("FEEDBACK INSERTED : PASSED")

def testcustomersignin(username, user_id):
    if username == user_id:
        print("CUSTOMER signin : PASSED")
    else:
        print("CUSTOMER signin : FAILED")

def testadminsignin(username, user_id):
    if username == user_id:
        print("ADMIN signin : PASSED")
    else:
        print("ADMIN signin : FAILED")

def testreturnadded(fur_id):
    ex = "SELECT * FROM current_returns WHERE furniture_id = %s"
    va = (int(fur_id),)
    my_cursor1.execute(ex , va)
    res = my_cursor1.fetchall()
    mydb1.commit()
    if len(res) < 1:
        print("RETURN INITIATED : FAILED")
    else:
        print("RETURN INTIATED : PASSED")



mydb1 = mysql.connector.connect(host = "localhost",
								user = "root",
								passwd = "Vinod@2505",
                                database = "frssdb",)
    
global my_cursor1
my_cursor1 = mydb1.cursor()

def CustomerPage(self) :
    self.destroy()
    customer = Tk()
    customer.geometry("1000x600")
    customer.title("Customer page")
    leftBg = "#67faaf"
    rightBg = "#6d2358"
    rightFrame = Frame(customer , width = 50 , height= 100 , background = rightBg)
    leftFrame = Frame(customer , width = 50 , height = 100 , background = leftBg)
    leftFrame.grid(row = 0 , column = 0 , sticky = "nsew")
    rightFrame.grid(row = 0 , column = 1 , sticky = "nsew")
    customer.grid_columnconfigure(0 , weight = 2)
    customer.grid_columnconfigure(1 , weight = 3)
    customer.grid_rowconfigure(0 , weight = 1)
    leftFrame.grid_propagate(False)
    leftFrame.pack_propagate(False)
    rightFrame.grid_propagate(False)
    rightFrame.pack_propagate(False)


    def buynowonloan():
        loan = Tk()
        loan.geometry("500x500")
        loan.title("Buy on loan")
        bgCol = "#fdf5e6"
        loan.config(bg=bgCol)
        l1 = Label(loan , text = "Enter the id of the furniture", bg=bgCol, font=("Linux Biolinum G", 12))
        l1.grid(row = 0 , column = 0, padx=10, pady=10)
        e1 = Entry(loan)
        e1.grid(row = 0 , column = 1)
        l2 = Label(loan , text = "Enter the days to rent", bg=bgCol, font=("Linux Biolinum G", 12))
        e2 = Entry(loan)
        l2.grid(row = 1, column = 0, padx=10, pady=10)
        e2.grid(row = 1 , column = 1)
        ex = "SELECT COUNT(username) FROM past_orders WHERE username = %s"
        va = (user_id , )
        my_cursor.execute(ex , va)
        count = my_cursor.fetchall()[0][0]
        l3 = Label(loan , text = "Your past orders : " + str(count), bg=bgCol, font=("Source Serif Pro", 13, "italic"))
        l3.grid(row = 2 , column = 0 , columnspan = 2, pady=10)
        # print(count)

        def checkprice():
            fur_id = e1.get()
            num_days = e2.get()
            ex = "SELECT interest_rate FROM furnitures WHERE id = %s"
            va = (fur_id , )
            my_cursor.execute(ex , va)
            interest_rate = my_cursor.fetchall()
            new_interest = float(interest_rate[0][0])*(2**(-count))
            l4 = Label(loan , text = "Interest Rate on your experience with us : " + str(new_interest), bg = bgCol ,font=("Centaur", 10, "italic"))
            l4.grid(row = 3 , column = 0 , columnspan = 2, padx=10, pady=10)
            ex = "SELECT price FROM furnitures WHERE id = %s"
            va = (fur_id , )
            my_cursor.execute(ex , va)
            old_price = my_cursor.fetchall()
            # print("old Price " + str(old_price))
            global new_price
            new_price = float(old_price[0][0])*(1+new_interest*int(num_days)/100)
            l5 = Label(loan , text = "Total price on your experience with us : " + str(new_price), bg = bgCol ,font=("Centaur", 10, "italic"))
            l5.grid(row = 4 , column = 0 , columnspan = 2, padx=10, pady=10)
            pass

        def buynow():
            fur_id = e1.get()
            num_days = int(e2.get())
            ex = "UPDATE furnitures SET rented = %s , days_rented = days_rented + %s WHERE id = %s"
            va = (2 , num_days , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "INSERT INTO past_orders (username , furniture_id) VALUES (%s , %s)"
            va = (user_id , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "UPDATE customers SET amountdue = %s WHERE username = %s"
            messagebox.showinfo("Information", "Furniture Purchased !")
            va = (new_price , user_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            CustomerPage(customer)
            pass

        b1 = Button(loan , text = "Buy Now" , command = buynow, bg="#002366", font=("Arial", 13, "bold"), fg="white")
        b1.grid(row = 7 , column = 0, padx=10, pady=10, columnspan=2)
        b2 = Button(loan , text = "Check Price" , command = checkprice, bg="#991229", font=("Arial", 13, "bold"), fg="white")
        b2.grid(row = 6 , column = 0, padx=10, pady=10, columnspan=2)
        pass

    def buynowonrent():
        rent = Tk()
        rent.geometry("500x500")
        bgCol = "#fdf5e6"
        rent.config(bg=bgCol)
        rent.title("Buy now on rent")
        l1 = Label(rent , text = "Enter the id of the furniture", bg=bgCol, font=("Linux Biolinum G", 12))
        l1.grid(row = 0 , column = 0, padx=10, pady=10)
        e1 = Entry(rent)
        e1.grid(row = 0 , column = 1)
        l2 = Label(rent , text = "Enter the days to rent ", bg=bgCol, font=("Linux Biolinum G", 12))
        e2 = Entry(rent)
        l2.grid(row = 1, column = 0 , padx=10, pady=10)
        e2.grid(row = 1 , column = 1)

        def checkprice():
            fur_id = e1.get()
            num_days = e2.get()
            ex = "SELECT price FROM furnitures WHERE id = %s"
            va = (fur_id , )
            my_cursor.execute(ex , va)
            old_price = my_cursor.fetchall()
            global ne_price
            ne_price = old_price[0][0]*math.ceil(int(num_days)/10)
            l5 = Label(rent , text = "Total price on your experience with us : " + str(ne_price),bg = bgCol, font=("Centaur", 10, "italic"))
            l5.grid(row = 4 , column = 0 , columnspan = 2)
            pass

        def buynow():
            fur_id = e1.get()
            num_days = int(e2.get())
            ex = "UPDATE furnitures SET rented = %s , days_rented = days_rented + %s WHERE id = %s"
            va = (1 , num_days , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "INSERT INTO past_orders (username , furniture_id) VALUES (%s , %s)"
            va = (user_id , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "SELECT profit FROM admins LIMIT 1"
            my_cursor.execute(ex)
            res = my_cursor.fetchall()
            ex = "SELECT username FROM admins LIMIT 1"
            my_cursor.execute(ex)
            re = my_cursor.fetchall()
            ex ="UPDATE admins SET profit = %s WHERE username = %s"
            va = (ne_price + res[0][0] , re[0][0])
            my_cursor.execute(ex , va)
            mydb.commit()
            exe = "SELECT profit FROM graph WHERE id = (SELECT max(id) FROM graph)"
            my_cursor.execute(exe)
            oldprofit = my_cursor.fetchall()
            exe = "SELECT investment FROM graph WHERE id = (SELECT max(id) FROM graph)"
            my_cursor.execute(exe)
            oldinvestment = my_cursor.fetchall()
            exe = "INSERT INTO graph (profit , investment) VALUES (%s , %s)"
            va = (float(oldprofit[0][0])+float(ne_price), float(oldinvestment[0][0]))
            my_cursor.execute(exe , va)
            mydb.commit()
            messagebox.showinfo("Information", "Furniture Purchased !")
            CustomerPage(customer)
            pass

        b2 = Button(rent , text = "Check Price" , command = checkprice, font=("Arial", 13, "bold"), fg="white", bg="#002366")
        b2.grid(row = 5 , column = 0, padx=10, pady=10, columnspan=2)

        b1 = Button(rent , text = "Buy Now" , command = buynow, font=("Arial", 13, "bold"), fg="white", bg="#991229")
        b1.grid(row = 6 , column = 0, padx=10, pady=10, columnspan=2)
        pass

    def returnitem():
        item = Tk()
        item.geometry("500x500")
        item.title("Return item")
        bgCol = "#a2ffa1"
        item.config(bg=bgCol)
        l6 = Label(item , text = "Enter the id of the furniture : ", bg=bgCol, font=("Times new roman", 14))
        l6.grid(row = 0 , column = 0, padx=10, pady=10)
        e6 = Entry(item, relief=FLAT)
        e6.grid(row = 0 , column = 1)

        def addreturn():
            temp = e6.get()
            if temp:
                ex = "INSERT INTO current_returns (username , furniture_id) VALUES (%s , %s)"
                va = (user_id , int(e6.get()))
                my_cursor.execute(ex , va)
                mydb.commit()
                messagebox.showinfo("Information", "Return Process Initiated, you will be notified soon !")
                testreturnadded(e6.get())
            else:
                messagebox.showwarning("Warning", "Enter the ID !")
            pass

        b6 = Button(item , text = "Add to return" , command = addreturn, bg="#800080", font=("Arial", 12, "bold"), fg="white")
        b6.grid(row = 1 , column = 1, padx=10, pady=10)
        pass

    def checkamountdue():
        amount = Tk()
        amount.geometry("500x500")
        amount.title("Amount details")
        cbg="#00eaff"
        amount.config(bg=cbg)
        ex = "SELECT amountdue FROM customers WHERE username = %s"
        va = (user_id , )
        my_cursor.execute(ex , va)
        res = my_cursor.fetchall()[0][0]
        l1 = Label(amount , text = "Your amount due : " + str(res), bg=cbg, font=("Source Serif Pro", 13))
        l1.grid(row=0, column=0,padx=10, pady=10, columnspan=2)
        testcustomeramountdue(user_id, res)
        l2 = Label(amount , text = "Enter amount to be paid", bg=cbg, font=("Source Serif Pro", 13))
        l2.grid(row=1, column=0, padx=10, pady=10)
        e2 = Entry(amount, relief=FLAT)
        e2.grid(row=1, column=1)

        def paynow():
            
            money = (e2.get())
            if money:
                money = float(money)
                ex = "SELECT profit FROM admins LIMIT 1"
                my_cursor.execute(ex)
                r = my_cursor.fetchall()
                new_profit = r[0][0] + money
                ex = "SELECT username FROM admins LIMIT 1"
                my_cursor.execute(ex)
                re = my_cursor.fetchall()
                ex ="UPDATE admins SET profit = %s WHERE username = %s"
                va = (new_profit , re[0][0])
                my_cursor.execute(ex , va)
                mydb.commit()
                ex = "UPDATE customers SET amountdue = %s WHERE username = %s"
                va = (max(res-money , 0) , user_id)
                my_cursor.execute(ex , va)
                mydb.commit()
                testpaymentdone(user_id, res)
                messagebox.showinfo("Information", "Amount Paid !")
                exe = "SELECT profit FROM graph WHERE id = (SELECT max(id) FROM graph)"
                my_cursor.execute(exe)
                oldprofit = my_cursor.fetchall()
                exe = "SELECT investment FROM graph WHERE id = (SELECT max(id) FROM graph)"
                my_cursor.execute(exe)
                oldinvestment = my_cursor.fetchall()
                exe = "INSERT INTO graph (profit , investment) VALUES (%s , %s)"
                va = (float(oldprofit[0][0])+float(money), float(oldinvestment[0][0]))
                my_cursor.execute(exe , va)
                mydb.commit()
            else:
                messagebox.showwarning("Warning", "No money added !")
            pass

        b1 = Button(amount , text = "Pay amount due !" , command = paynow, bg="#60e84e", font=("Arial", 13, "bold"))
        b1.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        pass

    def pastorder():
        past = Tk()
        past.geometry("500x500")
        past.title("Past order history")
        ex = "SELECT * FROM past_orders WHERE username = %s"
        va = (user_id , )
        my_cursor.execute(ex , va)
        res = my_cursor.fetchall()
        text_scroll = Scrollbar(past)
        text_scroll.pack(side = RIGHT , fill = Y)
        my_text = Text(past , width = 100 , height = 120 , font = ('Source Serif Pro' , 10) , yscrollcommand = text_scroll.set, spacing1=8)
        my_text.pack(pady = 10 , padx = 10)
        text_scroll.config(command = my_text.yview)
        for furniture in res:
            my_text.insert(END , "          Furniture id = " + str(furniture[2]) + "\n")
        pass

    def giveFeedback():
        give = Tk()
        give.geometry("800x500")
        give.title("Give feedback")
        gbg = "#fdcb9f"
        give.config(bg = gbg)
        lab2 = Label(give , text = "Enter the name of the furniture", bg=gbg, font=("Courier New", 12, "bold"))
        lab2.grid(row = 0 ,column = 0, padx=10, pady=10)
        ent2 = Entry(give, relief=FLAT, width=70)
        ent2.grid(row = 0 , column = 1)
        lab1 = Label(give , text = "Give Feedback", bg=gbg, font=("Courier New", 12, "bold"))
        lab1.grid(row = 1,column = 0, padx=10, pady=10)
        ent1 = Entry(give, relief=FLAT, width=70)
        ent1.grid(row = 1 , column = 1)
        
        def submitFeedback():
            typ = ent2.get()
            feed = ent1.get()
            if typ and feed:
                ex = "INSERT INTO feedbacks (type , review) VALUES (%s , %s)"
                va = (typ , feed)
                my_cursor.execute(ex , va)
                mydb.commit()
                testfeedbackinsert(typ, feed)
                messagebox.showinfo("Information", "Feedback Submitted !")
            else:
                messagebox.showwarning("Warning", "All fields must be filled !")
            
            pass

        but1 = Button(give , text = "Submit feedback" , command = submitFeedback, bg="#60e84e", font=("Arial", 13, "bold"))
        but1.grid(row = 2 , column = 0 , columnspan = 2, padx=10, pady=10)

        pass

    def searchFurniture():
        search = Tk()
        search.geometry("800x500")
        search.title("Search for furniture")
        lbg = "#ccff47"
        rbg = "#f56c00"
        frame1 = Frame(search , background = lbg)
        frame1.grid(row = 0 , column = 0 , sticky = "nsew")
        frame2 = Frame(search , background = rbg)
        frame2.grid(row = 0 , column = 1 , sticky = "nsew")
        search.grid_columnconfigure(0 , weight = 2)
        search.grid_columnconfigure(1 , weight = 3)
        search.grid_rowconfigure(0 , weight = 1)
        frame1.grid_propagate(False)
        frame2.grid_propagate(False)
        frame1.pack_propagate(False)
        frame2.pack_propagate(False)
        la1 = Label(frame1 , text = "Enter the name :", font=("Times new roman", 14), bg=lbg)
        la1.grid(row = 0 , column = 0, padx=10, pady=10)
        ent1 = Entry(frame1, relief=FLAT, font=("Source Serif Pro", 9))
        ent1.grid(row = 0 , column = 1)
        text_scroll2 = Scrollbar(frame2)
        text_scroll2.pack(side = RIGHT , fill = Y)
        my_text2 = Text(frame2 , width = 100 , height = 120 , font = ('Source Serif Pro' , 10) , yscrollcommand = text_scroll2.set, spacing1=8)
        my_text2.pack(pady = 10 , padx = 10)
        text_scroll2.config(command = my_text2.yview)
        global my_imag
        global imag
        imag = []
        def searchNow():
            my_text2.delete("1.0" , END)
            typ = ent1.get()
            exe = "SELECT * FROM furnitures WHERE rented = 0"
            my_cursor.execute(exe)
            relu = my_cursor.fetchall()
            for furniture in relu:
                if typ in furniture[5]:
                    # print("type", typ)
                    # print("furniture" , furniture)
                    my_imag = Image.open(furniture[7])
                    my_imag = my_imag.resize((120,150) , Image.ANTIALIAS)
                    # my_imag = my_imag.rotate(270)
                    my_imag = ImageTk.PhotoImage(my_imag , master = frame2)
                    my_text2.image_create(END , image = my_imag, padx=40, pady=10)
                    my_text2.insert(END , '\n')
                    imag.append(my_imag)
                    my_text2.insert(END , "         Id : " + str(furniture[0]) + '\n')
                    my_text2.insert(END , "         Name : " + furniture[5] + '\n')
                    my_text2.insert(END , "         Company : " + furniture[2] + '\n')
                    my_text2.insert(END , "         Price : " + str(furniture[3]) + '\n')
                    my_text2.insert(END , "         Description : " + furniture[4] + '\n')
                    my_text2.insert(END , "         Interest Rate : " + str(furniture[8]) + '\n')
                    ex = "SELECT review FROM feedbacks WHERE type = %s"
                    va = (furniture[5],)
                    my_cursor.execute(ex , va)
                    rel = my_cursor.fetchall()
                    my_text2.insert(END , "         Reviews :\n")
                    for feedback in rel:
                        my_text2.insert(END , "         "+ feedback[0] + "\n")
                        pass
                    my_text2.insert(END , "\n\n")
            pass

        bu1 = Button(frame1 , text = "Search Now" , command = searchNow, bg="red", fg="white", font=("Centaur", 14, "bold"))
        bu1.grid(row = 1 , column = 0 , columnspan = 2, padx=10, pady=10)
        pass

    def logOut():
        Signin(customer)
        pass
    
    BtnBg = "#f3893E"
    buy_now_on_loan = Button(leftFrame , text = "Buy Now On Loan" , width = 35 , command = buynowonloan, bg=BtnBg, font=("Source Serif Pro", 13))
    buy_now_on_loan.pack(padx=10, pady=(50, 10))
    buy_now_on_rent = Button(leftFrame , text = "Buy Now On Rent" , width = 35 , command = buynowonrent, bg=BtnBg, font=("Source Serif Pro", 13))
    buy_now_on_rent.pack(padx=10, pady=10)
    returnbutton = Button(leftFrame , text = "Return" , width = 35 , command = returnitem, bg=BtnBg, font=("Source Serif Pro", 13))
    returnbutton.pack(padx=10, pady=10)
    amountdue = Button(leftFrame , text = "Amount Due" , width = 35 , command = checkamountdue, bg=BtnBg, font=("Source Serif Pro", 13))
    amountdue.pack(padx=10, pady=10)
    pastorder = Button(leftFrame , text = "Past Order History" , width = 35 , command = pastorder, bg=BtnBg, font=("Source Serif Pro", 13))
    pastorder.pack(padx=10, pady=10)
    feedback = Button(leftFrame , text = "Give Feedback" , command = giveFeedback, bg=BtnBg, font=("Source Serif Pro", 13), width=35)
    feedback.pack(padx=10, pady=10)
    searchbutton = Button(leftFrame , text = "Search furniture" , width = 35,command = searchFurniture, bg=BtnBg, font=("Source Serif Pro", 13))
    searchbutton.pack(padx=10, pady=10)
    logout = Button(leftFrame , text = "Log Out" , width = 35 , command = logOut, bg=BtnBg, font=("Source Serif Pro", 13))
    logout.pack(padx=10, pady=10)

    text_scroll = Scrollbar(rightFrame)
    text_scroll.pack(side = RIGHT , fill = Y)
    my_text = Text(rightFrame , width = 100 , height = 120 , font = ('Source Serif Pro' , 10) , yscrollcommand = text_scroll.set, spacing1=8)
    my_text.pack(pady = 10 , padx = 10)
    text_scroll.config(command = my_text.yview)
    global my_image
    global images
    images = []

    exe = "SELECT * FROM furnitures WHERE rented = 0 group by price ,type"
    my_cursor.execute(exe)
    result = my_cursor.fetchall()
    for furniture in result:
        # print(furniture)
        my_image = Image.open(furniture[7])
        my_image = my_image.resize((120,150) , Image.ANTIALIAS)
        # my_image = my_image.rotate(270)
        my_image = ImageTk.PhotoImage(my_image)
        my_text.image_create(END , image = my_image, padx=40, pady=10)
        my_text.insert(END , '\n')
        images.append(my_image)
        my_text.insert(END , "          Id : " + str(furniture[0]) + '\n')
        my_text.insert(END , "          Name : " + furniture[5] + '\n')
        my_text.insert(END , "          Company : " + furniture[2] + '\n')
        my_text.insert(END , "          Price : " + str(furniture[3]) + '\n')
        my_text.insert(END , "          Description : " + furniture[4] + '\n')
        my_text.insert(END , "          Interest Rate : " + str(furniture[8]) + '\n')
        ex = "SELECT review FROM feedbacks WHERE type = %s"
        va = (furniture[5],)
        my_cursor.execute(ex , va)
        rel = my_cursor.fetchall()
        my_text.insert(END , "          Reviews :\n")
        for feedback in rel:
            my_text.insert(END , "          " + feedback[0] + "\n")
            pass
        my_text.insert(END , "\n\n")
        pass


def AdminPage(self):
    self.destroy()
    admin = Tk()
    admin.geometry("900x550")
    admin.title("Admin page")
    leftBg = "#f0b241"
    rightBg = "#41f06d"
    rightFrame = Frame(admin , width = 50 , height= 100 , background = rightBg)
    leftFrame = Frame(admin , width = 50 , height = 100 , background = leftBg)
    leftFrame.grid(row = 0 , column = 0 , sticky = "nsew")
    rightFrame.grid(row = 0 , column = 1 , sticky = "nsew")
    admin.grid_columnconfigure(0 , weight = 1)
    admin.grid_columnconfigure(1 , weight = 1)
    admin.grid_rowconfigure(0 , weight = 1)
    leftFrame.grid_propagate(False)
    leftFrame.pack_propagate(False)
    rightFrame.grid_propagate(False)
    rightFrame.pack_propagate(False)

    exe = "SELECT id FROM furnitures WHERE days_rented >= %s"
    va = (365,)
    my_cursor.execute(exe, va)
    res = my_cursor.fetchall()

    if(len(res) > 0):
        for id in res[0]:
            ex = "UPDATE furnitures SET days_rented = days_rented - %s , price = price * %s WHERE id = %s"
            va = (365, 0.9, id)
            my_cursor.execute(ex, va)


    mydb.commit()




    def createCustomer():
        Signup()
        pass

    def deleteCustomer():
        delcustomer = Tk()
        delcustomer.geometry("650x200")
        delcustomer.title("Delete a customer account")
        delcustomer.config(bg="#a2ffa1")
        l1 = Label(delcustomer , text = "Enter the username of the customer to delete : ", bg="#a2ffa1", font=("Courier new", 13))
        l1.grid(row = 0 , column = 1, padx=10, pady=10)
        e1 = Entry(delcustomer, relief=FLAT)
        e1.grid(row = 0 , column = 2)

        def removeCustomer():
            user = e1.get()
            exe = "SELECT * FROM customers WHERE username = %s"
            val = (user , )
            my_cursor.execute(exe , val)
            res = my_cursor.fetchall()
            if len(res) == 0:
                messagebox.showwarning("ALERT !" , "NO such user found !")
            elif res[0][5] != 0:
                messagebox.showwarning("Warning","User Cannot be Deleted !")
                testnotdeleteduser(user)
            else:
                exe = "DELETE FROM customers WHERE username = %s"
                my_cursor.execute(exe , val)
                mydb.commit()
                messagebox.showinfo("ALERT !" , "USER DELETED !")
                testdeleteuser(user)
            pass

        b = Button(delcustomer , text = "Delete !" , command = removeCustomer, bg="red", fg="white", font=("Arial", 13, "bold"))
        b.grid(row = 1 , column = 0 , columnspan = 2)
        pass

    def seeNotifications():
        # get distinct type of furniture put it in the list
        # do a count query with each item in the list
        # if any count falls below threshold display it
        see = Tk()
        see.geometry("500x500")
        see.title("Notifications")
        text_scroll = Scrollbar(see)
        text_scroll.pack(side = RIGHT , fill = Y)
        my_text = Text(see , width = 100 , height = 120 , font = ('Source Serif Pro' , 10) , yscrollcommand = text_scroll.set, spacing1=8)
        my_text.pack(pady = 10 , padx = 10)
        text_scroll.config(command = my_text.yview)
        exe = "SELECT DISTINCT type FROM furnitures"
        my_cursor.execute(exe)
        res = my_cursor.fetchall()
        # print("REsult : " , res)
        for t in res:
            ex = "SELECT COUNT(type) FROM furnitures WHERE rented = %s AND type = %s"
            # print("t = " , t[0])
            v = (0 , t[0])
            my_cursor.execute(ex , v)
            r = my_cursor.fetchall()
            # print("r = " , r)
            if r[0][0]<5:
                my_text.insert(END , "          " + t[0] + " type of furniture is low !\n")
            pass
        pass

    def checkInvestmentAndProfit():
        inv = Tk()
        inv.geometry("1360x678")
        leftBg = "#FFA400"
        rightBg = "#9ACD32"
        fram1 = Frame(inv , background = leftBg)
        fram2 = Frame(inv , background = rightBg)
        fram1.grid(row = 0 , column = 0 , sticky = "nsew")
        fram2.grid(row = 0 , column = 1 , sticky = "nsew")
        inv.grid_columnconfigure(0 , weight = 3)
        inv.grid_columnconfigure(1 , weight = 4)
        inv.grid_rowconfigure(0 , weight = 1)
        fram1.grid_propagate(False)
        fram2.grid_propagate(False)
        # fram1.pack_propagate(False)
        # fram2.pack_propagate(False)
        exe = "SELECT SUM(investment) FROM admins"
        my_cursor.execute(exe)
        investment = my_cursor.fetchall()
        # print(investment[0][0])
        l4 = Label(fram1 , text = "INVESTMENT = " + str(investment[0][0]), bg=leftBg, font=("Source Serif Pro", 13, "bold"))
        l4.grid(row=0, column=0, pady=200, padx=25)
        testinvestment(float(investment[0][0]))
        exe = "SELECT SUM(profit) FROM admins"
        my_cursor.execute(exe)
        pro = my_cursor.fetchall()
        # print(pro[0][0])
        l5 = Label(fram1 , text = "Profit = " + str(pro[0][0]), bg=leftBg, font=("Source Serif Pro", 13, "bold"))
        testprofit(float(pro[0][0]))
        l5.grid(row=1, column=0, padx=25)
        exe = "SELECT profit , investment FROM graph"
        my_cursor.execute(exe)
        rel = my_cursor.fetchall()
        x = []
        y = []
        for tup in rel:
            x.append(tup[1])
            y.append(tup[0])
        fig = Figure(figsize = (8,6),dpi = 100)
        canvas = FigureCanvasTkAgg(fig, master = fram2)
        plot1 = fig.add_subplot(111)
        plot1.plot(x,y)
        plot1.set_xlabel("investment")
        plot1.set_ylabel("profit")
        canvas.draw()
        canvas.get_tk_widget().pack(pady = 30 , padx = 8)
        pass

    def changePrice():
        change = Tk()
        change.geometry("600x400")
        change.title("Change price of an item")
        changeBg = "#ff9a5b"
        change.config(bg=changeBg)
        l2 = Label(change, text = "Enter the type of the furniture for changing price: ", font=("Times New Roman", 15), bg=changeBg)
        l2.grid(row = 0 , column = 0, padx=10, pady=10)
        e2 = Entry(change, relief=FLAT)
        e2.grid(row = 0 , column = 1)
        l3 = Label(change , text = "Enter the new price :", font=("Times New Roman", 15), bg=changeBg)
        l3.grid(row = 1 , column = 0, padx=10, pady=10)
        e3 = Entry(change, relief=FLAT)
        e3.grid(row = 1 , column = 1)

        def alter():
            typ = e2.get()
            np = e3.get()
            ex = "SELECT * FROM furnitures WHERE type = %s"
            va = (typ,)
            my_cursor.execute(ex , va)
            res = my_cursor.fetchall()
            if len(res) == 0:
                messagebox.showerror("Error", "No furniture of this type found !")
                return
            exe = "UPDATE furnitures SET price = %s WHERE type = %s"
            va = (np , typ)
            my_cursor.execute(exe , va)
            mydb.commit()
            testchangeprice(str(typ), float(np))
            messagebox.showinfo("Information", "Price Changed")
            pass

        b2 = Button(change , command = alter , text = "Alter", bg="red", font=("Arial", 16, "bold"), fg="white")
        b2.grid(row = 2 , column = 1, pady=10)
        
        pass

    def reAddition():
        readd = Tk()
        readd.geometry("1000x500")
        readd.title("Verify Returns")
        rightBg = "#ADFF2F"
        leftBg = "#DEB887"
        rightFrame1 = Frame(readd , width = 50 , height= 100 , background = rightBg)
        leftFrame1 = Frame(readd , width = 50 , height = 100 , background = leftBg)
        leftFrame1.grid(row = 0 , column = 0 , sticky = "nsew")
        rightFrame1.grid(row = 0 , column = 1 , sticky = "nsew")
        readd.grid_columnconfigure(0 , weight = 2)
        readd.grid_columnconfigure(1 , weight = 3)
        readd.grid_rowconfigure(0 , weight = 1)
        leftFrame1.grid_propagate(False)
        leftFrame1.pack_propagate(False)
        rightFrame1.grid_propagate(False)
        rightFrame1.pack_propagate(False)

        text_scroll1 = Scrollbar(rightFrame1)
        text_scroll1.pack(side = RIGHT , fill = Y)
        my_text1 = Text(rightFrame1 , width = 100 , height = 120 , font = ('Source Serif Pro' , 10) , yscrollcommand = text_scroll1.set, spacing1=8)
        my_text1.pack(pady = 10 , padx = 10)
        text_scroll1.config(command = my_text1.yview)

        ex = "SELECT * FROM current_returns"
        my_cursor.execute(ex)
        result = my_cursor.fetchall()
        for query in result:
            my_text1.insert(END , "         Furniture id = " + str(query[2]) + " Username = " + str(query[1]) + "\n")

        l1 = Label(leftFrame1 , text = "Enter the furniture id : ", font=("Eras Demi ITC", 12), bg=leftBg)
        e1 = Entry(leftFrame1)
        l1.grid(row = 0 , column = 0, padx=10, pady=10)
        e1.grid(row = 0 , column = 1)
        l2 = Label(leftFrame1 , text = "Enter the username : ", font=("Eras Demi ITC", 12), bg=leftBg)
        e2 = Entry(leftFrame1)
        l2.grid(row = 1 , column = 0, padx=10, pady=10)
        e2.grid(row = 1 , column = 1)
        v1 = StringVar(leftFrame1 , "1")
        R1 = Radiobutton(leftFrame1 , text = "Damaged" , variable = v1 , value = "1", bg=leftBg)
        R2 = Radiobutton(leftFrame1 , text = "Not Damaged" , variable = v1 , value ="2", bg=leftBg)
        R1.grid(row = 2 , column = 0, padx=10, pady=10)
        R2.grid(row = 2 , column = 1, padx=10, pady=10)


        def completereturn():
            fur_id = e1.get()
            user = e2.get()
            if v1.get() == "1" :
                ex = "SELECT price FROM furnitures WHERE id = %s"
                va = (fur_id,)
                my_cursor.execute(ex , va)
                price = my_cursor.fetchall()
                ex = "SELECT amountdue FROM customers WHERE username = %s"
                va = (user,)
                my_cursor.execute(ex , va)
                oldamount = my_cursor.fetchall()
                ex = "UPDATE customers SET amountdue = %s WHERE username = %s"
                va = (oldamount[0][0] + price[0][0] , user)
                my_cursor.execute(ex , va)
                mydb.commit()
                ex = "DELETE FROM furnitures WHERE id = %s"
                va = (fur_id , )
                my_cursor.execute(ex , va)
                mydb.commit()
                messagebox.showinfo("Information", "Furniture Deleted !")
                testfurnituredelete(int(fur_id))
                pass
            else:
                ex = "UPDATE furnitures SET rented = %s WHERE id = %s"
                va = (0 , fur_id )
                my_cursor.execute(ex , va)
                mydb.commit()
                messagebox.showinfo("Information", "Furniture Added to the Inventory !")
                testreadditionfurniture(int(fur_id))
                pass
            ex = "DELETE FROM current_returns WHERE username = %s AND furniture_id = %s"
            va = (user , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "SELECT * FROM current_returns"
            my_cursor.execute(ex)
            result = my_cursor.fetchall()
            my_text1.delete("1.0",END)
            for query in result:
                my_text1.insert(END , "Furniture id = " + str(query[2]) + " Username = " + str(query[1]) + "\n")
            pass

        b1 = Button(leftFrame1 , text = "Complete the return !" , command = completereturn, bg="#B22222", font=("Arial", 13, "bold"), fg="white")
        b1.grid(row = 3 , column = 0 , columnspan = 2)
        pass
    
    btnBg = "#ffe08d"
    createcustomeraccountbutton = Button(rightFrame , text = "Create a customer account" , width = 30 , command = createCustomer, bg=btnBg,fg="black",font=("Source Serif Pro", 13))
    createcustomeraccountbutton.pack(pady=(50,10))
    deletecustomeraccountbutton = Button(rightFrame , text = "Delete a customer account" , width = 30 , command = deleteCustomer, bg=btnBg,fg="black",font=("Source Serif Pro", 13))
    deletecustomeraccountbutton.pack(pady=10)
    notificationsbutton = Button(rightFrame , text = "See the notifications" , width = 30 , command = seeNotifications, bg=btnBg,fg="black",font=("Source Serif Pro", 13))
    notificationsbutton.pack(pady=10)
    investmentprofitbutton = Button(rightFrame , text = "Investment and profit" , width = 30 , command = checkInvestmentAndProfit, bg=btnBg,fg="black",font=("Source Serif Pro", 13))
    investmentprofitbutton.pack(pady=10)
    changeprice = Button(rightFrame , text = "Change price" , width = 30 , command = changePrice, bg=btnBg,fg="black",font=("Source Serif Pro", 13))
    changeprice.pack(pady=10)
    readdition = Button(rightFrame , text = "Check returns" , width = 30 , command = reAddition, bg=btnBg,fg="black",font=("Source Serif Pro", 13))
    readdition.pack(pady=10)

    def adminlogoutcommand():
        Signin(admin)

    adminlogout = Button(rightFrame , text = "Log Out" , width = 30 , command = adminlogoutcommand, bg=btnBg,fg="black",font=("Source Serif Pro", 13))
    adminlogout.pack(pady=10)

    notifl = Label(leftFrame , text = "Add new funiture to inventory", bg=leftBg, relief=FLAT, font=("Source Serif Pro", 13), fg="red")
    notifl.grid(row=0, column=0, columnspan=2, padx=30)
    namel =  Label(leftFrame , text = "Name", bg=leftBg, relief=FLAT, font=("Source Serif Pro", 13))
    namel.grid(row = 1 , column = 0, padx=30, pady=10)
    type = Label(leftFrame , text = "Type", bg=leftBg, relief=FLAT, font=("Source Serif Pro", 13))
    type.grid(row = 2 , column = 0, padx=30, pady=10)
    price = Label(leftFrame , text = "Price", bg=leftBg, relief=FLAT, font=("Source Serif Pro", 13))
    price.grid(row = 3 , column = 0, padx=30, pady=10)
    interestrate = Label(leftFrame , text = "Interest Rate", bg=leftBg, relief=FLAT, font=("Source Serif Pro", 13))
    interestrate.grid(row = 4 , column = 0, padx=30, pady=10)
    description = Label(leftFrame , text = "Description", bg=leftBg, relief=FLAT, font=("Source Serif Pro", 13))
    description.grid(row = 5 , column = 0, padx=30, pady=10)
    companyl = Label(leftFrame , text = "Company", bg=leftBg, relief=FLAT, font=("Source Serif Pro", 13))
    companyl.grid(row = 6 , column = 0, padx=40, pady=10)

    nameentry =  Entry(leftFrame, relief=FLAT)
    nameentry.grid(row = 1 , column = 1)
    typeentry = Entry(leftFrame, relief=FLAT)
    typeentry.grid(row = 2 , column = 1)
    priceentry = Entry(leftFrame , relief=FLAT)
    priceentry.grid(row = 3 , column = 1)
    interestrateentry = Entry(leftFrame, relief=FLAT)
    interestrateentry.grid(row = 4 , column = 1)
    descriptionentry = Entry(leftFrame, relief=FLAT)
    descriptionentry.grid(row = 5 , column = 1)
    companyentry = Entry(leftFrame, relief=FLAT)
    companyentry.grid(row = 6 , column = 1)

    global filepath
    filepath = ""

    def openImage():
        leftFrame.filename= filedialog.askopenfilename(initialdir = os.path.join(os.getcwd() , "Images") , title = 'Choose a picture' , filetypes = (("jpg files" , "*.jpg"),))
        global filepath
        filepath = leftFrame.filename
        pass

    def add_furniture():
        name = nameentry.get()
        company = companyentry.get()
        type = typeentry.get()
        interestrate = (interestrateentry.get())
        price = (priceentry.get())
        description = descriptionentry.get()
        date = dt.today().strftime('%Y-%m-%d')
        # print(filepath , date)
        if name and type and interestrate and price and description and filepath:
            interestrate = float(interestrate)
            price = float(price)
            exe = 'INSERT INTO furnitures (name , company , price , description , type , rented , photo , interest_rate , date_started) VALUES (%s , %s , %s , %s , %s , %s , %s , %s ,%s)'
            values = (name , company , price , description , type , 0 , filepath , interestrate , date)
            my_cursor.execute(exe , values)
            mydb.commit()
            exe = "UPDATE admins SET investment = investment + %s WHERE username = %s"
            va = (price , user_id)
            my_cursor.execute(exe , va)
            mydb.commit()
            exe = "SELECT profit FROM graph WHERE id = (SELECT max(id) FROM graph)"
            my_cursor.execute(exe)
            oldprofit = my_cursor.fetchall()
            # print("oldprofit " , oldprofit)
            exe = "SELECT investment FROM graph WHERE id = (SELECT max(id) FROM graph)"
            my_cursor.execute(exe)
            oldinvestment = my_cursor.fetchall()
            print("oldinvestment " , oldinvestment)
            exe = "INSERT INTO graph (profit , investment) VALUES (%s , %s)"
            va = (float(oldprofit[0][0]), float(oldinvestment[0][0])+float(price))
            # va = ( 0 ,  price)
            my_cursor.execute(exe , va)
            mydb.commit()
            messagebox.showinfo("Information", "Furniture Added !")
            nameentry.delete(0,END)
            companyentry.delete(0,END)
            typeentry.delete(0,END)
            interestrateentry.delete(0,END)
            priceentry.delete(0,END)
            descriptionentry.delete(0,END)
            testaddfuniture(type, filepath)
        else:
            messagebox.showwarning("ALERT !" , "Complete all of the fields")
        pass

    chooseimage = Button(leftFrame , text = "Choose Image" , command = openImage , width = 20, bg="#fd759f", font=("Arial", 13, "bold"))
    chooseimage.grid(row = 7 , column = 0, padx=30, pady=10, columnspan=2)

    add = Button(leftFrame , text = "Add Furniture" , width = 30 , command = add_furniture, bg="#60e84e", font=("Arial", 13, "bold"))
    add.grid(row = 8 , column = 0, padx=30, pady=10, columnspan=2)

# make a back button here!

def Signin(self):
    self.destroy()
    signin = Tk()
    signin.title("Sign in to your account")
    signin_background = "#a2ffa1"

    notification = Label(signin, text="   Fill up your signin information!", font=("Source Serif Pro", 13), fg="red", bg=signin_background)
    notification.grid(row=0, column=0, columnspan=2, padx=(70,0), pady=10)
    signin.geometry("500x400")
    signin.config(bg=signin_background)
    v1 = StringVar(signin , "1")
    adminradiobutton = Radiobutton(signin , text = "Admin" , variable = v1 , value = "1", font=("Arial", 12), bg=signin_background)
    customerradiobutton = Radiobutton(signin , text = "Customer" , variable = v1 , value ="2", font=("Arial", 12), bg=signin_background)
    usernamel = Label(signin , text = "Username", bg=signin_background,font=("Source Serif Pro", 13))
    usernamel.grid(row = 1 , column = 0, padx=80, pady=10)
    passwdl = Label(signin , text = "Password", bg=signin_background,font=("Source Serif Pro", 13))
    passwdl.grid(row = 2 , column = 0, padx=(80,80), pady=10)
    adminradiobutton.grid(row = 3 , column = 0, padx=(80,80), pady=10)
    customerradiobutton.grid(row = 3 , column = 1, pady=10)

    def adduser():
        username = usernameentry.get()
        password = passwordentry.get()
        
        # print(username , password)
        if username and password:
            if v1.get() == "2":
                exe =  f'SELECT username , password FROM customers WHERE username = "{username}" AND password = "{password}"'
                
                my_cursor.execute(exe)
                result  = my_cursor.fetchall()
                if len(result) == 0 :
                    messagebox.showerror("Error", "Invalid Username or Password !")
                    return 
                global user_id , pass_word , is_admin
                user_id = result[0][0]
                pass_word = result[0][1]
                testcustomersignin(username, user_id)
                is_admin = False
                CustomerPage(signin)
            else :
                exe =  f'SELECT username , password FROM admins WHERE username = "{username}" AND password = "{password}"'
                # global user_id , pass_word , is_admin
                my_cursor.execute(exe)
                result  = my_cursor.fetchall()
                if len(result) == 0 :
                    messagebox.showerror("Error", "Invalid Username or Password !")
                    return
                user_id = result[0][0]
                pass_word = result[0][1]
                testadminsignin(username, user_id)
                is_admin = True
                AdminPage(signin)

        else:
            messagebox.showwarning("ALERT !" , "All fields should be filled !")

    usernameentry = Entry(signin, relief=FLAT)
    usernameentry.grid(row = 1 , column = 1)
    passwordentry = Entry(signin , show ='*', relief=FLAT)
    passwordentry.grid(row = 2 , column = 1)
    global lb
    lb = Image.open(os.path.join(os.getcwd() , "Images\\Signin.png"))
    lb = lb.resize((120, 30))
    lb = ImageTk.PhotoImage(lb)
    completesignin = Button(signin ,image = lb, command = adduser, bg=signin_background, relief=FLAT)
    completesignin.grid(row = 4 , column = 0, columnspan = 2, padx=(70,0))

def verified_signup(self):
    self.destroy()
    status = Tk()
    status.title("Sign Up status")
    status.config(bg = "#a2ffa1")
    status.geometry("300x80")
 
    notification = Label(status, text="Successfully registered ", font=("Source Serif Pro", 13), fg="red", bg="#a2ffa1")
    notification.grid(row=2, column=3, columnspan=3)
    notification1 = Label(status, text=" You can signin to your account", font=("Source Serif Pro", 13), fg="red", bg="#a2ffa1")
    notification1.grid(row=4, column=3, columnspan=3)
    # lb = Image.open(os.path.join(os.getcwd() , "Images\\Signin.png"))
    # lb = lb.resize((120, 30))
    # lb = ImageTk.PhotoImage(lb)
    # signinbtn = Button(status ,image = lb, command = Signin, bg="#a2ffa1", relief=FLAT)
    # signinbtn.grid(row = 4 , column = 0, columnspan = 2, padx=(70,0))

def Signup():
    signup = Toplevel(bg="#a2ffa1")
    signup.geometry("650x700")
    signup.title("Sign Up")

    # namel = Label(signup , text = "Name", bg="#adccb0")
    name_label = Label(signup,text="Name",bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    name_label.grid(row = 1 , column = 0, padx=10, pady=10)
    notification = Label(signup, text="Fill in the details!", font=("Source Serif Pro", 13), fg="red", bg="#a2ffa1")
    notification.grid(row=0, column=0, columnspan=2)
    username_label = Label(signup , text = "Username", bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    username_label.grid(row = 2 , column = 0, padx=10, pady=10)
    password_label = Label(signup , text = "Enter password", bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    password_label.grid(row = 3 , column = 0)
    confirmpassword_label = Label(signup , text = "Confirm password", bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    confirmpassword_label.grid(row = 4 , column = 0, padx=10, pady=10)
    address_label = Label(signup , text = "Enter the address", bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    address_label.grid(row = 5 , column = 0, padx=10, pady=10)
    phonenumber_label = Label(signup , text = "Enter the phone number", bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    phonenumber_label.grid(row = 6 , column = 0, padx=10, pady=10)
    emailIdInput_label = Label(signup, text = "Enter email id", bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    emailIdInput_label.grid(row = 7 , column =0, padx=10, pady=10)
    # sendmailbtn = Button(signup, text="Verify details and send email", font = ("Arial", 10, "bold"),cursor="hand2", bg="#dc143c", fg="white", pady=1)
    # sendmailbtn.grid(row=9, padx=40, pady=10, column=0, columnspan=2)
    # verifymailbtn = Button(signup, text="Verify OTP!", font = ("Arial", 10), state=DISABLED, bg="#4169e1", fg="white")
    # verifymailbtn.grid(row=13, padx=10, pady=10, column=1)

    # enterotp = Label(signup, text="Enter the OTP here: ", bg="#a2ffa1",fg="black",font=("Source Serif Pro", 13))
    # enterotp.grid(row=10, column=0, padx=10, pady=10)

    nameentry = Entry(signup , width = 50, relief=FLAT )
    nameentry.grid(row = 1 , column = 1, padx=10, pady=10)
    usernameentry = Entry(signup , width = 50, relief=FLAT  )
    usernameentry.grid(row = 2 , column = 1, padx=10, pady=10)
    passwordentry = Entry(signup , width = 50  , show ='*', relief=FLAT)
    passwordentry.grid(row = 3 , column = 1, padx=10, pady=10)
    confirmpasswordentry = Entry(signup , width = 50  , show = '*', relief=FLAT)
    confirmpasswordentry.grid(row = 4 , column = 1, padx=10, pady=10)
    addressentry = Entry(signup , width = 50, relief=FLAT )
    addressentry.grid(row = 5 , column = 1, padx=10, pady=10)
    phonenumberentry = Entry(signup , width = 50, relief=FLAT)
    phonenumberentry.grid(row = 6 , column = 1, padx=10, pady=10 )
    emailentry = Entry(signup, width = 50, relief=FLAT)
    emailentry.grid(row=7, column=1, padx=10, pady=10)
    # otpEntry = Entry(signup, width=50, relief=FLAT)
    # otpEntry.grid(row=10, column=1, padx=10, pady=10)

    v1 = StringVar(signup , "1")
    adminradiobutton = Radiobutton(signup , text = "Admin" , variable = v1 , value = "1", bg="#a2ffa1", font=("Arial", 12))
    adminradiobutton.grid(row = 8 , column = 0, padx=10, pady=10)
    customerradiobutton = Radiobutton(signup , text = "Customer" , variable = v1 , value ="2", bg="#a2ffa1", font=("Arial", 12))
    customerradiobutton.grid(row = 8 , column = 1, padx=10, pady=10)

    def verify():                                      # these checks have to be made!
        name = nameentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        cpassword = confirmpasswordentry.get()
        address = addressentry.get()
        phonenumber = phonenumberentry.get()
        emailid = emailentry.get()
        flag = 0
        global starttime 
        starttime = time.time()
        # global otp
        # otp = ""

        if v1.get() == "2":
            if name and username and password and cpassword and address and phonenumber and emailid:        
                my_cursor.execute("SELECT username from customers")
                total = my_cursor.fetchall()
                if len(total) > 0 and username in total[0]:
                    messagebox.showwarning("ALERT !" , "Username is already in use, Choose diffrent username")
                    usernameentry.delete(0 , END)
                    flag = flag + 1
                elif password != cpassword:
                    messagebox.showerror("ALERT !" , "The passwords are incompatible")
                    passwordentry.delete(0 , END)
                    confirmpasswordentry.delete(0 , END)
                    flag = flag + 1
                # else:
                #     try:
                #         server = smtplib.SMTP('smtp.gmail.com', 587)
                #         server.starttls()       # starts a secure shell else you get an error
                #         server.signin("frental123@gmail.com", "frss1234") # signin information
                #         dig = "0123456789"
                #         for _ in range(4):
                #             otp += random.choice(dig)
                #         finalMessage = "OTP for signin verification to our Furniture rental store system is " + otp
                #         to = emailentry.get()
                #         server.sendmail("frental123@gmail.com", to, finalMessage)       # check to
                #         notification.config(text = "Success! Email has been sent. Enter OTP sent to email id in 2 minutes", fg = "green")
                #         verifymailbtn.config(state=ACTIVE, bg="#4169e1", fg="white")
                #     except:
                #         messagebox.showerror("Invalid email!" , "Error! Please check the email id entered")
            else:
                messagebox.showwarning("ALERT !" , "Complete all of the fields")
                flag = flag + 1
        else:
            if name and username and password and cpassword and address and phonenumber:
                my_cursor.execute("SELECT username from admins")
                total = my_cursor.fetchall()
                
                if len(total) > 0 and username in total[0]:
                    messagebox.showwarning("ALERT !" , "Username is already in use, Choose diffrent username")
                    usernameentry.delete(0 , END)
                    flag = flag + 1
                elif password != cpassword:
                    messagebox.showwarning("ALERT !" , "The passwords are incompatible")
                    passwordentry.delete(0 , END)
                    confirmpasswordentry.delete(0 , END)
                    flag = flag + 1
                # else:
                #     try:
                #         server = smtplib.SMTP('smtp.gmail.com', 587)
                #         server.starttls()       # starts a secure shell else you get an error
                #         server.signin("frental123@gmail.com", "frss1234") # signin information
                #         dig = "0123456789"
                #         for _ in range(4):
                #             otp += random.choice(dig)
                #         finalMessage = "OTP for signin verification to our Furniture rental store system is " + otp
                #         to = emailentry.get()
                #         server.sendmail("frental123@gmail.com", to, finalMessage)       # check to
                #         notification.config(text = "Success! Email has been sent. Enter OTP sent to email id in 2 minutes", fg = "green")
                #         verifymailbtn.config(state=ACTIVE, bg="#4169e1", fg="white")
                #     except:
                #         messagebox.showwarning("Invalid email!" , "Error! Please check the email id entered")
            else:
                messagebox.showwarning("ALERT !" , "Complete all of the fields")
                flag = flag + 1

        if( True ):
            adduser()
            verified_signup(signup)
            # nameentry.delete(0 , END)
            # usernameentry.delete(0 , END)
            # passwordentry.delete(0 , END)
            # confirmpasswordentry.delete(0 , END)
            # addressentry.delete(0 , END)
            # phonenumberentry.delete(0 , END)
            # emailentry.delete(0 , END)
                

    # def verifyOTP():
    #     end = time.time()
    #     t = format(end-starttime)
    #     if float(t) >= 120:
    #         messagebox.showinfo("Timed out", "Session expired! Please regenerate OTP")
    #     else:
    #         enteredOTP = otpEntry.get()
    #         if enteredOTP == otp:
    #             notification.config(text = "Successfully verified OTP! Please click on Sign Up button to add your account!", fg = "green")
    #             addbutton.config(state=ACTIVE)
    #         else:
    #             messagebox.showerror("Invalid OTP", "Please enter a valid OTP!")

    def adduser():
        name = nameentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        address = addressentry.get()
        phonenumber = phonenumberentry.get()

        if v1.get() == "1":
            exe = 'INSERT INTO admins (name , username , password , address , phonenumber) VALUES (%s , %s , %s , %s , %s)'
            values = (name , username , password , address , phonenumber)
            my_cursor.execute(exe , values)
            mydb.commit()
            testsignup(username)
            

        else:
            exe = 'INSERT INTO customers (name , username , password , address , phonenumber) VALUES (%s , %s , %s , %s , %s)'
            values = (name , username , password , address , phonenumber)
            my_cursor.execute(exe , values)
            mydb.commit()
            testsignup(username)
            
    global sub
    sub = Image.open(os.path.join(os.getcwd() , "Images\\Signup.png"))
    sub = sub.resize((120, 30))
    sub = ImageTk.PhotoImage(sub)
    addbutton = Button(signup,image=sub, bg="#a2ffa1", relief=FLAT ,  cursor= "circle")
    addbutton.grid(row=15 , column=1, pady=3) 
    addbutton.config(command=verify)
    # verifymailbtn.config(command=verifyOTP)


if __name__ == '__main__':
    root = Tk()
    root.geometry("1580x800")
    root.title("FRSS Pvt Ltd")
    mydb = mysql.connector.connect(host = "localhost",
								user = "root",
								passwd = "Vinod@2505",
                                database = "frssdb",)
    
    global my_cursor
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS frssdb")
    # my_cursor.execute("SHOW DATABASES")
    # for db in my_cursor:
        # print(db)

    my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255) NOT NULL,username VARCHAR(255) PRIMARY KEY,password VARCHAR(255) NOT NULL,address VARCHAR(255) NOT NULL, phonenumber VARCHAR(255) NOT NULL,amountdue DECIMAL(8,2) DEFAULT 0,numberoforders INT(10))")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS admins (name VARCHAR(255) NOT NULL,username VARCHAR(255) PRIMARY KEY,password VARCHAR(255) NOT NULL,address VARCHAR(255) NOT NULL, phonenumber VARCHAR(255) NOT NULL,profit DECIMAL(8,2) DEFAULT 0,investment DECIMAL(8,2) DEFAULT 0)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS furnitures (id INT auto_increment primary key, name VARCHAR(255) NOT NULL , company VARCHAR(255) NOT NULL , price DECIMAL(8,2) , description VARCHAR(255) NOT NULL , type VARCHAR(255) NOT NULL , rented INT , photo VARCHAR(255) NOT NULL , interest_rate DECIMAL(4,2) , date_started DATE , date_ended DATE , username VARCHAR(255) , FOREIGN KEY (username) REFERENCES customers(username) , days_rented INT DEFAULT 0)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS past_orders (id INT auto_increment primary key , username VARCHAR(255) , furniture_id INT)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS feedbacks (id INT auto_increment primary key , type VARCHAR(255), review VARCHAR(255))")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS current_returns (id INT auto_increment primary key , username VARCHAR(255), furniture_id INT)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS graph (id INT auto_increment primary key , profit DECIMAL(8,2) DEFAULT 0 , investment DECIMAL(8,2) DEFAULT 0)")
    
    # ex = "INSERT INTO graph (profit, investment) VALUES (%s, %s)"
    # va = (0,0)
    # my_cursor.execute(ex, va)
    # mydb.commit()

    # my_cursor.execute("SELECT * FROM customers")
    # print(my_cursor.description)
    wallpaper_path = os.path.join(os.getcwd() , "Images\\bg.png")
    background_image = Image.open(wallpaper_path)
    background_image = background_image.resize((1600,900))
    background_image = ImageTk.PhotoImage(background_image)
    background_label = Label(root , image = background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    signinbutton = Button(root, text = 'Sign In', command = lambda : Signin(root), height=2, width=40, font=("Source Serif Pro", 12), padx=10, pady=1 , bg = "#66ffcc" )
    signinbutton.pack(side= LEFT, padx=230)
    signupbutton = Button(root, text = 'Sign Up', command = Signup, height=2, width=40, font=("Source Serif Pro", 12), padx=10, pady=1 , bg = "#66ffcc")
    signupbutton.pack(side= LEFT)
    root.mainloop()
    unittest.main()