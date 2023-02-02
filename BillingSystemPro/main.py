
import datetime
import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
class Bill_App:

    def __init__(self,root):
        self.one_kg_cake_name = ["Ferrero Rocher Cake","Dark Ganche Cake","LoTus Biscuff Cake","Black Forest Cake",
                                 "Tiramisu Cake","Nutella Cake","Gooey Cake"]
        self.one_kg_cake_entry = []
        self.one_kg_cake_price = []
        self.cup_cake_name = ["Ferrero Rocher Cup Cake","Rainbow Cup Cake","Death By Choch Cup Cake",
                              "Red Velvet Cup Cake","Kit Kat Cup Cake","Mocha Menace Cup Cake","Bluberry Cup Cake"]
        self.cup_cake_entry = []
        self.cup_cake_price = []
        self.cake_jar_name = ["Bluberry Jar","Red Velvet Jar","Tiramisu Jar","Ferrero Rocher Jar","Kit Kat Jar",
                              "Lotus Biscuff Jar","Death By Choch Jar"]
        self.cake_jar_entry = []
        self.cake_jar_price = []
        self.root = root
        self.root.geometry("700x700+0+0")
        self.root.title("Billing App")
        # self.root.winfo_geometry()
        # self.root.title("Billing System")
        title = Label(self.root,text="Billing App",bd=12,relief=GROOVE,bg="#00ffff",fg="black",
                      font = ("times new roman",30,"bold"),pady=2).pack(fill=X)

########################################### Variables For Inputs #######################################################
        self.name = StringVar()
        self.phone = StringVar()
        self.billno = StringVar()
        ################### 1kg var ##########################
        self.ferrerorochercake = IntVar()
        self.darkganachecake = IntVar()
        self.lotuscake = IntVar()
        self.blackforestcake = IntVar()
        self.tiramisucake = IntVar()
        self.nutellacake = IntVar()
        self.gooeycake = IntVar()
        ################### cup cake var ##########################
        self.ferrerorochercup = IntVar()
        self.redcup = IntVar()
        self.kitkatcup = IntVar()
        self.rainbowcup = IntVar()
        self.deathbycup = IntVar()
        self.mochacup = IntVar()
        self.blueberrycup = IntVar()
        ################### cup cake var ##########################
        self.ferrerorocherjar = IntVar()
        self.redjar = IntVar()
        self.kitkatjar = IntVar()
        self.lotusjar = IntVar()
        self.deathbyjar = IntVar()
        self.tiramisujar = IntVar()
        self.blueberryjar = IntVar()

        self.one_kg_total_price = StringVar()
        self.cup_cake_total_price = StringVar()
        self.cake_jar_total_price = StringVar()

#####################################   customer details frame    ######################################################
        F1 = LabelFrame(self.root, text="Customer Datails", bd=12, relief=GROOVE, bg="#00ffff", fg="gold",
                        font=("times new roman", 15, "bold"), pady=2)
        F1.place(x=5, y=80, relwidth=1)

        cname_1b1 = Label(F1, text="Customer Name : ", bg="#00ffff",
                          font=("times new roman", 18, "bold")).grid(row=0,column=0, padx=5, pady=5)
        cname_txt = Entry(F1, width=20,textvariable=self.name ,font="arial 15", bd=7,
                          relief=SUNKEN).grid(row=0, column=1, pady=5, padx=5)

        cphone_1b1 = Label(F1, text="Phone Number : ", bg="#00ffff",
                           font=("times new roman", 18, "bold")).grid(row=0,column=2, padx=5, pady=5)
        cphone_txt = Entry(F1, width=20,textvariable=self.phone, font="arial 15", bd=7,
                           relief=SUNKEN).grid(row=0, column=3, pady=5, padx=5)

        cbill_1b1 = Label(F1, text="Bill Number : ", bg="#00ffff",
                          font=("times new roman", 18, "bold")).grid(row=0, column=4,   padx=5, pady=5)
        cbill_txt = Entry(F1, width=20,textvariable=self.billno, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                        column=5, pady=5, padx=5)

############################################## Creat Fram For 1kg Cake #################################################
        F2 = LabelFrame(self.root, text="1kg Cake", bd=10, relief=GROOVE, bg="#00ffff", fg="gold",
                        font=("times new roman", 15, "bold"), pady=2)
        F2.place(x=5, y=175, width=325,height=380)

        cferrerorocher_1b1 = Label(F2, text="Ferrero Rocher : ", bg="#00ffff", font=("times new roman", 12,
                                "bold")).grid(row=0, column=2, padx=5, pady=5)
        cferrerorocher_txt = Entry(F2, width=12,textvariable=self.ferrerorochercake, font="arial 15", bd=7,
                                   relief=SUNKEN).grid(row=0, column=3, pady=5, padx=5)
        self.pferrerorocher = 1100

        cdarkganache_1b1 = Label(F2,  text="Dark Ganache  : ", bg="#00ffff",
                                   font=("times new roman", 12, "bold")).grid(row=1,
                                                                              column=2,
                                                                              padx=5,
                                                                              pady=5)
        cdarkganache_txt = Entry(F2, width=12,textvariable=self.darkganachecake, font="arial 15", bd=7,
                                 relief=SUNKEN).grid(row=1, column=3, pady=5,padx=5)
        self.pdarkganache = 800

        clotusbiscuff_1b1 = Label(F2, text="Lotus Biscuff    : ", bg="#00ffff",
                                 font=("times new roman", 12, "bold")).grid(row=2,
                                                                            column=2,
                                                                            padx=5,
                                                                            pady=5)
        clotusbiscuff_txt = Entry(F2, width=12,textvariable=self.lotuscake, font="arial 15", bd=7,
                                  relief=SUNKEN).grid(row=2, column=3, pady=5,padx=5)
        self.plotusbiscuff = 1100

        cblackforest_1b1 = Label(F2, text="Black Forest     : ", bg="#00ffff",
                                 font=("times new roman", 12, "bold")).grid(row=3,
                                                                            column=2,
                                                                            padx=5,
                                                                            pady=5)
        cblackforest_txt = Entry(F2,textvariable=self.blackforestcake, width=12, font="arial 15",
                                 bd=7, relief=SUNKEN).grid(row=3, column=3, pady=5,padx=5)
        self.pblackforest = 1000

        ctiramisu_1b1 = Label(F2, text="Tiramisu           : ", bg="#00ffff",
                                 font=("times new roman", 12, "bold")).grid(row=4,
                                                                            column=2,
                                                                            padx=5,
                                                                            pady=5)
        ctiramisu_txt = Entry(F2,textvariable=self.tiramisucake, width=12, font="arial 15", bd=7,
                              relief=SUNKEN).grid(row=4, column=3, pady=5,padx=5)
        self.ptiramisu = 1100

        cnutella_1b1 = Label(F2, text="Nutella cake     : ", bg="#00ffff",
                                 font=("times new roman", 12, "bold")).grid(row=5,
                                                                            column=2,
                                                                            padx=5,
                                                                            pady=5)
        cnutella_txt = Entry(F2,textvariable=self.nutellacake, width=12, font="arial 15", bd=7,
                             relief=SUNKEN).grid(row=5, column=3, pady=5,padx=5)
        self.pnutella = 900

        cgooey_1b1 = Label(F2, text="Goooey cake    : ", bg="#00ffff",
                                 font=("times new roman", 12, "bold")).grid(row=6,
                                                                            column=2,
                                                                            padx=5,
                                                                            pady=5)
        cgooey_txt = Entry(F2,textvariable=self.gooeycake, width=12, font="arial 15", bd=7,
                           relief=SUNKEN).grid(row=6, column=3, pady=5,padx=5)
        self.pgooey = 900

############################################## Creat Fram For Cup Cake #################################################
        F3 = LabelFrame(self.root, text="Cup Cake", bd=10, relief=GROOVE, bg="#00ffff", fg="gold",
                        font=("times new roman", 15, "bold"), pady=2)
        F3.place(x=335, y=175, width=325, height=380)

        cferrerorochercup_1b1 = Label(F3, text="Ferrero Rocher : ", bg="#00ffff",
                                   font=("times new roman", 12, "bold")).grid(row=0,
                                                                              column=2,
                                                                              padx=5,
                                                                              pady=5)
        cferrerorochercup_txt = Entry(F3,textvariable=self.ferrerorochercup, width=12, font="arial 15",
                                      bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5,padx=5)
        self.pferrerorochercup = 110

        crainbowcup_1b1 = Label(F3, text="Rainbow            : ", bg="#00ffff",
                                 font=("times new roman", 12, "bold")).grid(row=1,
                                                                            column=2,
                                                                            padx=5,
                                                                            pady=5)
        crainbowcup_txt = Entry(F3,textvariable=self.rainbowcup, width=12, font="arial 15", bd=7,
                                relief=SUNKEN).grid(row=1, column=3, pady=5,padx=5)
        self.prainbowcup = 110

        cdeathbycup_1b1 = Label(F3, text="Death By choco : ", bg="#00ffff",
                                  font=("times new roman", 12, "bold")).grid(row=2,
                                                                             column=2,
                                                                             padx=5,
                                                                             pady=5)
        cdeathbycup_txt = Entry(F3,textvariable=self.deathbycup, width=12, font="arial 15", bd=7,
                                relief=SUNKEN).grid(row=2, column=3, pady=5,padx=5)
        self.pdeathbycup = 110

        credvelvetcup_1b1 = Label(F3, text="Red Velvet        : ", bg="#00ffff",
                                 font=("times new roman", 12, "bold")).grid(row=3,
                                                                            column=2,
                                                                            padx=5,
                                                                            pady=5)
        credvelvetcup_txt = Entry(F3,textvariable=self.redcup, width=12, font="arial 15", bd=7,
                                  relief=SUNKEN).grid(row=3, column=3, pady=5,padx=5)
        self.predvelvetcup = 110

        ckitkatcup_1b1 = Label(F3, text="Kit Kat               : ", bg="#00ffff",
                              font=("times new roman", 12, "bold")).grid(row=4,
                                                                         column=2,
                                                                         padx=5,
                                                                         pady=5)
        ckitkatcup_txt = Entry(F3,textvariable=self.kitkatcup, width=12, font="arial 15", bd=7,
                               relief=SUNKEN).grid(row=4, column=3, pady=5,padx=5)
        self.pkitkatcup = 110

        cmochacup_1b1 = Label(F3, text="Mocha Menace : ", bg="#00ffff",
                             font=("times new roman", 12, "bold")).grid(row=5,
                                                                        column=2,
                                                                        padx=5,
                                                                        pady=5)
        cmochacup_txt = Entry(F3,textvariable=self.mochacup, width=12, font="arial 15", bd=7,
                              relief=SUNKEN).grid(row=5, column=3, pady=5,padx=5)
        self.pmochacup = 110

        cblueberrycup_1b1 = Label(F3, text="Blueberry           : ", bg="#00ffff",
                           font=("times new roman", 12, "bold")).grid(row=6,
                                                                      column=2,
                                                                      padx=5,
                                                                      pady=5)
        cblueberrycup_txt = Entry(F3,textvariable=self.blueberrycup, width=12, font="arial 15", bd=7,
                                  relief=SUNKEN).grid(row=6, column=3, pady=5,padx=5)
        self.pblueberrycup = 110

############################################## Creat Fram For jars #####################################################
        F4 = LabelFrame(self.root, text="Cup Cake Jar", bd=10, relief=GROOVE, bg="#00ffff", fg="gold",
                        font=("times new roman", 15, "bold"), pady=2)
        F4.place(x=665, y=175, width=325, height=380)

        jblueberry_1b1 = Label(F4, text="Blueberry           : ", bg="#00ffff",
                               font=("times new roman", 12, "bold")).grid(row=0,
                                                                          column=2,
                                                                          padx=5,
                                                                          pady=5)
        jblueberry_txt = Entry(F4,textvariable=self.blueberryjar, width=12, font="arial 15", bd=7,
                               relief=SUNKEN).grid(row=0, column=3, pady=5,padx=5)
        self.pblueberryjar = 300

        jredvelvet_1b1 = Label(F4, text="Red Velvet        : ", bg="#00ffff",
                               font=("times new roman", 12, "bold")).grid(row=1,
                                                                          column=2,
                                                                          padx=5,
                                                                          pady=5)
        jredvelvet_txt = Entry(F4,textvariable=self.redjar, width=12, font="arial 15", bd=7,
                               relief=SUNKEN).grid(row=1, column=3, pady=5,padx=5)
        self.predvelvetjar = 300

        jtiramisu_1b1 = Label(F4, text="Tiramisu              : ", bg="#00ffff",
                               font=("times new roman", 12, "bold")).grid(row=2,
                                                                          column=2,
                                                                          padx=5,
                                                                          pady=5)
        jtiramisu_txt = Entry(F4,textvariable=self.tiramisujar, width=12, font="arial 15", bd=7,
                              relief=SUNKEN).grid(row=2, column=3, pady=5,padx=5)
        self.ptiramisujar = 250

        jferrerorocher_1b1 = Label(F4, text="Ferrero Rocher : ", bg="#00ffff",
                              font=("times new roman", 12, "bold")).grid(row=3,
                                                                         column=2,
                                                                         padx=5,
                                                                         pady=5)
        jferrerorocher_txt = Entry(F4,textvariable=self.ferrerorocherjar, width=12, font="arial 15", bd=7,
                                   relief=SUNKEN).grid(row=3, column=3, pady=5,padx=5)
        self.pferrerorocherjar = 250
        jkitkat_1b1 = Label(F4, text="Kit Kat               : ", bg="#00ffff",
                            font=("times new roman", 12, "bold")).grid(row=4,
                                                                       column=2,
                                                                       padx=5,
                                                                       pady=5)
        jkitkat_txt = Entry(F4,textvariable=self.kitkatjar, width=12, font="arial 15", bd=7,
                            relief=SUNKEN).grid(row=4, column=3, pady=5,padx=5)
        self.pkitkatjar = 280

        jlotus_1b1 = Label(F4, text="Lotus biscoff     : ", bg="#00ffff",
                           font=("times new roman", 12, "bold")).grid(row=5,
                                                                      column=2,
                                                                      padx=5,
                                                                      pady=5)
        jlotus_txt = Entry(F4,textvariable=self.lotusjar, width=12, font="arial 15", bd=7,
                           relief=SUNKEN).grid(row=5, column=3, pady=5,padx=5)
        self.plotusjar = 250

        jdeathby_1b1 = Label(F4, text="Death By choco : ", bg="#00ffff",
                             font=("times new roman", 12, "bold")).grid(row=6,
                                                                        column=2,
                                                                        padx=5,
                                                                        pady=5)
        jdeathby_txt = Entry(F4,textvariable=self.deathbyjar, width=12, font="arial 15", bd=7,
                             relief=SUNKEN).grid(row=6, column=3, pady=5,padx=5)
        self.pdeathbyjar = 250
############################################ Bill Details ##############################################################

        F5 = LabelFrame(self.root, text="Bill Details", bd=12, relief=GROOVE, bg="#00ffff", fg="gold",
                        font=("times new roman", 15, "bold"), pady=2)
        F5.place(x=5, y=560,width=985,height=150)

        t1kg_1b1 = Label(F5, text="1kg Cake       : ", bg="#00ffff",
                             font=("times new roman", 12, "bold")).grid(row=1,
                                                                        column=1,
                                                                        padx=5,
                                                                        pady=5)
        t1kg_txt =Entry(F5,textvariable=self.one_kg_total_price,bg="white",bd=2 ,
                             font=("times new roman", 12, "bold")).grid(row=1,
                                                                        column=2,
                                                                        padx=5,
                                                                        pady=5)

        tcupcake_1b1 = Label(F5, text="Cup Cake       : ", bg="#00ffff",
                         font=("times new roman", 12, "bold")).grid(row=2,
                                                                    column=1,
                                                                    padx=5,
                                                                    pady=5)
        tcupcake_txt = Entry(F5,textvariable=self.cup_cake_total_price,bg="white",bd=2,
                         font=("times new roman", 12, "bold")).grid(row=2,
                                                                    column=2,
                                                                    padx=5,
                                                                    pady=5)

        tcupcakejar_1b1 = Label(F5, text="Cup Cake Jar : ", bg="#00ffff",
                             font=("times new roman", 12, "bold")).grid(row=3,
                                                                        column=1,
                                                                        padx=5,
                                                                        pady=5)
        tcupcakejar_txt =Entry(F5,textvariable=self.cake_jar_total_price,bg="white",bd=2,
                             font=("times new roman", 12, "bold")).grid(row=3,
                                                                        column=2,
                                                                        padx=5,
                                                                        pady=5)
############################################# Bill Area ################################################################

        F6 = LabelFrame(self.root, text="Bill Area ", bd=5, relief=GROOVE, fg="gold",
                        font=("times new roman", 15, "bold"), pady=1)
        F6.place(x=995, y=175, width=360, height=530)
        bill_title = Label(F6,text="Bill Area", bd=5, relief=GROOVE, fg="black",
                        font=("times new roman", 15, "bold"), pady=1).pack(fill=X)
        scrol_y = Scrollbar(F6,orient=VERTICAL)
        self.txtarea = Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        btn_F = Frame(F5,bd=7,relief=GROOVE)
        btn_F.place(x=580,width=370,height=105)
        submit_btn = Button(btn_F,text="Submit",command=self.bill_area,bg="red",fg="Black",pady=15,padx=15,
                            font=("times new roman",18,"bold")).grid(row=0,column=0,pady=5,padx=5)

        save_btn = Button(btn_F,command=self.generate_invoice, text="Save", bg="red", fg="Black", pady=15, padx=15,
                            font=("times new roman", 18, "bold")).grid(row=0, column=1, pady=5, padx=5)

        clear_btn = Button(btn_F,text="Clear",command = self.clear ,bg="red",fg="Black",pady=15,padx=15,
                            font=("times new roman",18,"bold")).grid(row=0,column=2,pady=5,padx=5)
        self.bill_area()
####################################### Create Bill Area ###############################################################
    def bill_area(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t      Welcome To Boston \n")
        self.txtarea.insert(END,"\tShop No. 1, Legent Building,\n   Millat Nagar Rd, Lokhandwala Complex,\n "
                                " Andheri West, Mumbai Maharashtra 400053\n" )
        self.txtarea.insert(END,"=========================================\n")
        self.txtarea.insert(END,f"Customer Name : {self.name.get()}")
        # self.txtarea.insert(END,"\t\t\t     ")
        now = datetime.datetime.now()
        self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END,"\t\t\t      " +now.strftime("%Y-%m-%d"))
        # self.txtarea.insert(END,"\t\t\t       ")
        # now = datetime.now()
        # time = now.strftime("%H:%M:%S")
        # self.txtarea.insert(END,time)
        self.txtarea.insert(END,f"\nBill No. : {self.billno.get()}")
        self.txtarea.insert(END,"\n=========================================\n")
        self.txtarea.insert(END," Product ")
        self.txtarea.insert(END,"\t\t  Qty  ")
        self.txtarea.insert(END,"\t  Price  ")
        self.txtarea.insert(END,"\t  Total")
        self.txtarea.insert(END,"\n=========================================\n")
        self.txtarea.insert(END, "1kg Cake\n")
        print(self.ferrerorochercake.get())
        print("yes")
############################################### For 1kg Cake ###########################################################
        if (self.ferrerorochercake.get() > 0) or (self.darkganachecake.get() > 0) or (self.lotuscake.get() > 0) or\
                (self.blackforestcake.get() > 0) or (self.nutellacake.get() > 0) or (self.tiramisucake.get() > 0) or \
                (self.gooeycake.get() > 0):
            # self.txtarea.insert(END,"1kg Cake\n")
            self.one_kg_t = 0
            if self.ferrerorochercake.get() > 0 :
                self.txtarea.insert(END,"Ferrero Rocher")
                self.txtarea.insert(END, f"\t\t  {self.ferrerorochercake.get()}")
                self.txtarea.insert(END, f"\t  {self.pferrerorocher}")
                self.txtarea.insert(END, f"\t    {self.ferrerorochercake.get() * self.pferrerorocher}\n")
            if self.darkganachecake.get() > 0 :
                self.txtarea.insert(END,"Dark Ganache")
                self.txtarea.insert(END, f"\t\t  {self.darkganachecake.get()}")
                self.txtarea.insert(END, f"\t  {self.pdarkganache}")
                self.txtarea.insert(END, f"\t    {self.darkganachecake.get() * self.pdarkganache}\n")
            if self.lotuscake.get() > 0 :
                self.txtarea.insert(END,"Lotus Biscuff")
                self.txtarea.insert(END, f"\t\t  {self.lotuscake.get()}")
                self.txtarea.insert(END, f"\t  {self.plotusbiscuff}")
                self.txtarea.insert(END, f"\t    {self.lotuscake.get() * self.plotusbiscuff}\n")
            if self.blackforestcake.get() > 0 :
                self.txtarea.insert(END,"Black Forest")
                self.txtarea.insert(END, f"\t\t  {self.blackforestcake.get()}")
                self.txtarea.insert(END, f"\t  {self.pblackforest}")
                self.txtarea.insert(END, f"\t    {self.blackforestcake.get() * self.pblackforest}\n")
            if self.nutellacake.get() > 0 :
                self.txtarea.insert(END,"Nutella")
                self.txtarea.insert(END, f"\t\t  {self.nutellacake.get()}")
                self.txtarea.insert(END, f"\t  {self.pnutella}")
                self.txtarea.insert(END, f"\t    {self.nutellacake.get() * self.pnutella}\n")
            if self.tiramisucake.get() > 0 :
                self.txtarea.insert(END,"Tiramisu")
                self.txtarea.insert(END, f"\t\t  {self.tiramisucake.get()}")
                self.txtarea.insert(END, f"\t  {self.ptiramisu}")
                self.txtarea.insert(END, f"\t    {self.tiramisucake.get() * self.ptiramisu}\n")
            if self.gooeycake.get() > 0 :
                self.txtarea.insert(END,"Gooey")
                self.txtarea.insert(END, f"\t\t  {self.gooeycake.get()}")
                self.txtarea.insert(END, f"\t  {self.pgooey}")
                self.txtarea.insert(END, f"\t    {self.gooeycake.get() * self.pgooey}\n")
            self.txtarea.insert(END, "=========================================\n")
        self.one_kg_t = int((self.ferrerorochercake.get() * self.pferrerorocher)+(
                self.darkganachecake.get() * self.pdarkganache)+( self.lotuscake.get() * self.plotusbiscuff)+(
                self.blackforestcake.get() * self.pblackforest)+(self.nutellacake.get() * self.pnutella)+(
                self.tiramisucake.get() * self.ptiramisu)+(self.gooeycake.get() * self.pgooey))
        self.one_kg_total_price.set(str(self.one_kg_t))
        # self.txtarea.insert(END, "=========================================\n")
        self.txtarea.insert(END,"Total")
        self.txtarea.insert(END,f"\t\t\t\t    {self.one_kg_t}\n")
        self.txtarea.insert(END, "\n=========================================\n")
        self.txtarea.insert(END, "Cup Cake\n")

########################################### For Cup Cake ###############################################################
        if (self.ferrerorochercup.get() > 0) or (self.rainbowcup.get() > 0) or (self.deathbycup.get() > 0) or (
                self.redcup.get() > 0) or (self.kitkatcup.get() > 0) or (self.mochacup.get() > 0) or (
                self.blueberrycup.get() > 0):
            # self.txtarea.insert(END,"Cup Cake\n")
            self.cup_cake_t = 0
            if self.ferrerorochercup.get() > 0 :
                self.txtarea.insert(END,"Ferrero Rocher")
                self.txtarea.insert(END, f"\t\t  {self.ferrerorochercup.get()}")
                self.txtarea.insert(END, f"\t  {self.pferrerorochercup}")
                self.txtarea.insert(END, f"\t    {self.ferrerorochercup.get() * self.pferrerorochercup}\n")
            if self.rainbowcup.get() > 0 :
                self.txtarea.insert(END,"Rainbow")
                self.txtarea.insert(END, f"\t\t  {self.rainbowcup.get()}")
                self.txtarea.insert(END, f"\t  {self.prainbowcup}")
                self.txtarea.insert(END, f"\t    {self.rainbowcup.get() * self.prainbowcup}\n")
            if self.deathbycup.get() > 0 :
                self.txtarea.insert(END,"Death By")
                self.txtarea.insert(END, f"\t\t  {self.deathbycup.get()}")
                self.txtarea.insert(END, f"\t  {self.pdeathbycup}")
                self.txtarea.insert(END, f"\t    {self.deathbycup.get() * self.pdeathbycup}\n")
            if self.redcup.get() > 0 :
                self.txtarea.insert(END,"Red Velvet")
                self.txtarea.insert(END, f"\t\t  {self.redcup.get()}")
                self.txtarea.insert(END, f"\t  {self.predvelvetcup}")
                self.txtarea.insert(END, f"\t    {self.redcup.get() * self.predvelvetcup}\n")
            if self.kitkatcup.get() > 0 :
                self.txtarea.insert(END,"Kitkat")
                self.txtarea.insert(END, f"\t\t  {self.kitkatcup.get()}")
                self.txtarea.insert(END, f"\t  {self.pkitkatcup}")
                self.txtarea.insert(END, f"\t    {self.kitkatcup.get() * self.pkitkatcup}\n")
            if self.mochacup.get() > 0 :
                self.txtarea.insert(END,"Mocha")
                self.txtarea.insert(END, f"\t\t  {self.mochacup.get()}")
                self.txtarea.insert(END, f"\t  {self.pmochacup}")
                self.txtarea.insert(END, f"\t    {self.mochacup.get() * self.pmochacup}\n")
            if self.blueberrycup.get() > 0 :
                self.txtarea.insert(END,"Blueberry")
                self.txtarea.insert(END, f"\t\t  {self.blueberrycup.get()}")
                self.txtarea.insert(END, f"\t  {self.pblueberrycup}")
                self.txtarea.insert(END, f"\t    {self.blueberrycup.get() * self.pblueberrycup}\n")
            self.txtarea.insert(END, "=========================================\n")
        self.cup_cake_t = int((self.ferrerorochercup.get() * self.pferrerorochercup) + (
                self.rainbowcup.get() * self.prainbowcup) + (self.deathbycup.get() * self.pdeathbycup) + (
                self.redcup.get() * self.predvelvetcup) + (self.kitkatcup.get() * self.pkitkatcup) + (
                self.mochacup.get() * self.pmochacup) + (self.blueberrycup.get() * self.pblueberrycup))
        self.cup_cake_total_price.set(str(self.cup_cake_t))
        # self.txtarea.insert(END, "=========================================\n")
        self.txtarea.insert(END,"Total")
        self.txtarea.insert(END,f"\t\t\t\t    {self.cup_cake_t}\n")
        self.txtarea.insert(END, "\n=========================================\n")
        self.txtarea.insert(END, "Cup Cake Jar\n")

############################################## For Cup Cake jars #######################################################
        if (self.ferrerorochercup.get() > 0) or (self.lotusjar.get() > 0) or (self.deathbyjar.get() > 0) or (
                self.redjar.get() > 0) or (self.kitkatjar.get() > 0) or (self.tiramisujar.get() > 0) or (
                self.blueberryjar.get() > 0):
            # self.txtarea.insert(END, "Cup Cake Jar\n")
            self.cup_cake_jar_t = 0
            if self.ferrerorocherjar.get() > 0:
                self.txtarea.insert(END, "Ferrero Rocher")
                self.txtarea.insert(END, f"\t\t  {self.ferrerorocherjar.get()}")
                self.txtarea.insert(END, f"\t  {self.pferrerorocherjar}")
                self.txtarea.insert(END, f"\t    {self.ferrerorocherjar.get() * self.pferrerorocherjar}\n")
            if self.lotusjar.get() > 0:
                self.txtarea.insert(END, "Lotus")
                self.txtarea.insert(END, f"\t\t  {self.lotusjar.get()}")
                self.txtarea.insert(END, f"\t  {self.plotusjar}")
                self.txtarea.insert(END, f"\t    {self.lotusjar.get() * self.plotusjar}\n")
            if self.deathbyjar.get() > 0:
                self.txtarea.insert(END, "Death By")
                self.txtarea.insert(END, f"\t\t  {self.deathbyjar.get()}")
                self.txtarea.insert(END, f"\t  {self.pdeathbyjar}")
                self.txtarea.insert(END, f"\t    {self.deathbyjar.get() * self.pdeathbyjar}\n")
            if self.redjar.get() > 0:
                self.txtarea.insert(END, "Red Velvet")
                self.txtarea.insert(END, f"\t\t  {self.redjar.get()}")
                self.txtarea.insert(END, f"\t  {self.predvelvetjar}")
                self.txtarea.insert(END, f"\t    {self.redjar.get() * self.predvelvetjar}\n")
            if self.kitkatjar.get() > 0:
                self.txtarea.insert(END, "Kitkat")
                self.txtarea.insert(END, f"\t\t  {self.kitkatjar.get()}")
                self.txtarea.insert(END, f"\t  {self.pkitkatjar}")
                self.txtarea.insert(END, f"\t    {self.kitkatjar.get() * self.pkitkatjar}\n")
            if self.tiramisujar.get() > 0:
                self.txtarea.insert(END, "Tiramisu")
                self.txtarea.insert(END, f"\t\t  {self.tiramisujar.get()}")
                self.txtarea.insert(END, f"\t  {self.ptiramisujar}")
                self.txtarea.insert(END, f"\t    {self.tiramisujar.get() * self.ptiramisujar}\n")
            if self.blueberryjar.get() > 0:
                self.txtarea.insert(END, "Blueberry")
                self.txtarea.insert(END, f"\t\t  {self.blueberryjar.get()}")
                self.txtarea.insert(END, f"\t  {self.pblueberryjar}")
                self.txtarea.insert(END, f"\t    {self.blueberryjar.get() * self.pblueberryjar}\n")
            self.txtarea.insert(END, "=========================================\n")
        self.cup_cake_jar_t = int((self.ferrerorocherjar.get() * self.pferrerorocherjar) + (
                    self.lotusjar.get() * self.plotusjar) + (self.deathbyjar.get() * self.pdeathbyjar) + (
                                      self.redjar.get() * self.predvelvetjar) + (
                                      self.kitkatjar.get() * self.pkitkatjar) + (
                                      self.tiramisujar.get() * self.ptiramisujar) + (
                                      self.blueberryjar.get() * self.pblueberryjar))
        self.cake_jar_total_price.set(str(self.cup_cake_jar_t))
        # self.txtarea.insert(END, "=========================================\n")
        self.txtarea.insert(END, "Total")
        self.txtarea.insert(END, f"\t\t\t\t    {self.cup_cake_jar_t}\n")
        self.txtarea.insert(END, "\n=========================================\n")
        self.txtarea.insert(END, "Grand Total")
        self.txtarea.insert(END,f"\t\t\t\t    {self.one_kg_t + self.cup_cake_t + self.cup_cake_jar_t}\n\n")
        self.txtarea.insert(END, "\n-----------------------------------------\n")
        self.txtarea.insert(END,f"\t       Customer Copy\n")
        self.txtarea.insert(END,f"\t    Thanks For Visiting\n\t      The Boston Cafe\n")

############################## For Save Customers Bills ################################################################
    def generate_invoice(self):
        now = datetime.datetime.now()
############################### Create Bill File And Bill Number #######################################################
        last_file = os.listdir(f"C:\\Users\\Admin\\PycharmProjects\\BillingSystemPro\\bills")
        if last_file == []:
            file_name = str(1)
            self.billno.set("1")
        else:
            file_name = last_file[len(last_file) - 1]
            file_name = file_name.split(".")
            file_name = str(int(file_name[0]) + 1)
            self.billno.set(f"{file_name}")

        self.bill_area()
########################### Create List For Collect Entry's Of 1kg Cake ################################################
        self.one_kg_cake_entry = [self.ferrerorochercake.get(), self.darkganachecake.get(), self.lotuscake.get(),
                                  self.blackforestcake.get(), self.tiramisucake.get(), self.nutellacake.get(),
                                  self.gooeycake.get()]
########################### Create List For Collect Entry's Of Cup Cake ################################################
        self.cup_cake_entry = [self.ferrerorochercup.get(),self.rainbowcup.get(),self.deathbycup.get(),
                               self.redcup.get(),self.kitkatcup.get(),self.mochacup.get(),
                               self.blueberrycup.get()]
########################### Create List For Collect Entry's Of Cake Jar ################################################
        self.cake_jar_entry = [self.blueberryjar.get(),self.redjar.get(),self.tiramisujar.get(),
                               self.ferrerorocherjar.get(),self.kitkatjar.get(),self.lotusjar.get(),
                               self.deathbyjar.get()]
########################### Create List For Collect Prices Of 1kg Cake #################################################
        self.one_kg_cake_price = [self.pferrerorocher,self.pdarkganache,self.plotusbiscuff,self.pblackforest,
                                  self.ptiramisu,self.pnutella,self.pgooey]
########################### Create List For Collect Prices Of Cup Cake #################################################
        self.cup_cake_price = [self.pferrerorochercup,self.prainbowcup,self.pdeathbycup,self.predvelvetcup,
                               self.pkitkatcup,self.pmochacup,self.pblueberrycup]
########################### Create List For Collect Prices Of Cake Jar #################################################
        self.cake_jar_price = [self.pblueberryjar,self.predvelvetjar,self.ptiramisujar,self.pferrerorocherjar,
                               self.pkitkatjar,self.plotusjar,self.pdeathbyjar]
############################### Create Bill Pdf ########################################################################
        c = canvas.Canvas(f"C:\\Users\\Admin\\PycharmProjects\\BillingSystemPro\\bills\\{file_name}.pdf",
                          pagesize=(200, 300), bottomup=0)
######################################### Create Bill Structure ########################################################
        c.setFillColorRGB(0.1,0.1,0.1)
        c.line(70, 22, 180, 22)
        c.line(5, 50, 195, 50)
        c.line(15, 120, 185, 120)
        c.line(15, 240, 185, 240)
        c.line(35, 108, 35, 250)
        c.line(110, 108, 110, 250)
        c.line(138, 108, 138, 250)
        c.line(155, 108, 155, 250)
        c.line(15, 250, 185, 250)

        c.translate(9, 45)
        c.scale(1, -1)
###################################### Get Image For Logo ##############################################################
        self.file_name = os.path.basename("C:\\Users\\Admin\\PycharmProjects\\BillingSystemPro\\img_1.png")
        c.drawImage(self.file_name, 0, 0, width=50, height=35)
        c.scale(1, -1)
        c.translate(-9, -45)

        self.company_name = "The Boston Cafe & Patisserie"
        c.setFont("Times-Bold", 10)
        c.drawCentredString(125, 20, self.company_name)

############################################## Set Address In The Bill #################################################
        c.setFont("Times-Bold", 5)
        self.address0 = "Shop No. 1, Legent Building,"
        self.address1 = "Millat Nagar Rd, Lokhandwala Complex,"
        self.address2 = "Andheri West, Mumbai Maharashtra 400053"
        c.drawCentredString(125, 30, self.address0)
        c.drawCentredString(125, 35, self.address1)
        c.drawCentredString(125, 40, self.address2)


        c.drawCentredString(125, 45, "GST No : 22AAAAA0000A1Z5")

        c.setFont("Times-Bold", 8)
        c.drawCentredString(100, 59, " BILL ")

        c.setFont("Times-Bold", 5)

        c.drawRightString(70, 70, "Bill No. : ")
        c.drawString(76, 70, self.billno.get())

        c.drawRightString(70, 80, "Date : ")
        c.drawRightString(100, 80,now.strftime("%Y-%m-%d"))

        c.drawRightString(70, 90, "Customer Name : ")
        c.drawString(76, 90, self.name.get())

        c.drawRightString(70, 100, "Phone No. : ")
        c.drawRightString(100, 100, self.phone.get())

        c.roundRect(15, 108, 170, 160, 10, stroke=1, fill=0)


########################################### Create Index IN Bill #######################################################
        c.drawCentredString(25, 118, "S.No.")
        c.drawCentredString(75, 118, "Orders")
        c.drawCentredString(125, 118, "Price")
        c.drawCentredString(148, 118, "Qty.")
        c.drawCentredString(173, 118, "Total")
        c.drawCentredString(75, 246, "Grand Orders")

############################## Get Products From Entry's ANd Set In The Index With Price ###############################
        x = 40
        y = 126
        a = 0
        for i in range(0,len(self.one_kg_cake_name)):
            # print(self.one_kg_cake_entry)
            if self.one_kg_cake_entry[i] > 0:
                c.drawString(145,y,f"{self.one_kg_cake_entry[i]}")
                c.drawString(118,y,f"{self.one_kg_cake_price[i]}")
                c.drawString(165,y,f"{self.one_kg_cake_entry[i] * self.one_kg_cake_price[i]}")
                c.drawString(x,y,self.one_kg_cake_name[i])
                a = f"{i+1}"
                c.drawString(25,y,a)
                y = y + 5
        a = int(a)
        for i in range(0,len(self.cup_cake_name)):
            # print(self.cup_cake_entry)
            if self.cup_cake_entry[i] > 0:
                c.drawString(145, y, f"{self.cup_cake_entry[i]}")
                c.drawString(118, y, f"{self.cup_cake_price[i]}")
                c.drawString(165, y, f"{self.cup_cake_entry[i] * self.cup_cake_price[i]}")
                c.drawString(x,y,self.cup_cake_name[i])
                a = f"{a+1}"
                c.drawString(25,y,a)
                a = int(a)
                y = y + 5
        a = int(a)
        for i in range(0, len(self.cake_jar_name)):
            # print(self.cake_jar_entry)
            if self.cake_jar_entry[i] > 0:
                c.drawString(145, y, f"{self.cake_jar_entry[i]}")
                c.drawString(118, y, f"{self.cake_jar_price[i]}")
                c.drawString(165, y, f"{self.cake_jar_entry[i] * self.cake_jar_price[i]}")
                c.drawString(x, y, self.cake_jar_name[i])
                a = f"{a + 1}"
                c.drawString(25, y, a)
                a = int(a)
                y = y + 5


############################################### Set Total Payble Amount ################################################
        self.Grand_total = f"{self.one_kg_t + self.cup_cake_t + self.cup_cake_jar_t}"
        c.drawString(165,246,self.Grand_total)

        c.drawString(30, 260, "This is system generated invoice!!")

        # c.drawRightString(180, 228, self.aus.get())
        c.drawRightString(180, 265, "Signature")
        c.showPage()
        c.save()


    def clear(self):
################################################ Variables For Inputs ##################################################
        self.name.set(" ")
        self.phone.set(" ")
        self.billno.set(" ")
##################################################### 1kg var ##########################################################
        self.ferrerorochercake.set(0)
        self.darkganachecake.set(0)
        self.lotuscake.set(0)
        self.blackforestcake.set(0)
        self.tiramisucake.set(0)
        self.nutellacake.set(0)
        self.gooeycake.set(0)
################################################### cup cake var #######################################################
        self.ferrerorochercup.set(0)
        self.redcup.set(0)
        self.kitkatcup.set(0)
        self.rainbowcup.set(0)
        self.deathbycup.set(0)
        self.mochacup.set(0)
        self.blueberrycup.set(0)
################################################### cup cake var #######################################################
        self.ferrerorocherjar.set(0)
        self.redjar.set(0)
        self.kitkatjar.set(0)
        self.lotusjar.set(0)
        self.deathbyjar.set(0)
        self.tiramisujar.set(0)
        self.blueberryjar.set(0)
        self.bill_area()


root =  Tk()
obj = Bill_App(root)
root.mainloop()