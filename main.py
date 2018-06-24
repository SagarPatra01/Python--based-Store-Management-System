from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

#conn = sqlite3.connect('E:\Projects\Python\Store Management Software\Database\store.db')
conn = sqlite3.connect('store.db')

c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS `transactions` ( `id`	INTEGER PRIMARY KEY AUTOINCREMENT, `product_name`	TEXT,"
          "`quantity`	INTEGER, `amount`	INTEGER, `date`	TEXT);")
date = datetime.datetime.now().date()
product_list = []
product_quantity = []
product_price = []
product_id = []

labels_list = []


class Application:
    def __init__(self, master, *args, **kwargs):

        self.chaneisThere = 1

        self.master = master
        self.left = Frame(master, width=700, height=768, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text='Store Management', font=('arial 40 bold'), bg='white')
        self.heading.place(x=0, y=0)

        self.date_1 = Label(self.right, text="Today's Date: " + str(date), font=('arial 16 bold'), bg='lightblue')
        self.date_1.place(x=0, y=0)

        self.tproduct = Label(self.right, text="Products", font=('arial 19 bold'), bg='lightblue')
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 19 bold'), bg='lightblue')
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 19 bold'), bg='lightblue')
        self.tamount.place(x=500, y=60)

        self.enterid = Label(self.left, text='Enter ID', font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0, y=80)

        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=190, y=80)
        self.enteride.focus()


        self.search_btn = Button(self.left, text='Search', width=22, height=2, bg='orange', command=self.ajax)
        self.search_btn.place(x=350, y=120)

        self.productname = Label(self.left, text='', font=('arial 18 bold'), bg='white', fg='steelblue')
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text='', font=('arial 18 bold'), bg='white', fg='steelblue')
        self.pprice.place(x=0, y=290)

        self.total_label = Label(self.right, text='', font=('arial 40 bold'), bg='lightblue', fg='white')
        self.total_label.place(x=0, y=600)

        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.ajax)
        self.master.bind("<space>", self.generate_bill)



    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id,))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
        self.productname.configure(text="Product's Name: " + str(self.get_name))
        self.pprice.configure(text="Price: " + str(self.get_price))

        self.quantity_1 = Label(self.left, text='Enter Quantity', font=('arial 18 bold'), bg='white')
        self.quantity_1.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        self.discount_1 = Label(self.left, text='Enter Discount', font=('arial 18 bold'), bg='white')
        self.discount_1.place(x=0, y=410)

        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)

        self.add_to_btn = Button(self.left, text='Add To Cart', width=22, height=2, bg='orange',
                                 command=self.add_to_cart)
        self.add_to_btn.place(x=350, y=450)

        self.change_1 = Label(self.left, text='Given Amount', font=('arial 18 bold'), bg='white')
        self.change_1.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.change_e.place(x=190, y=550)

        self.change_butn = Button(self.left, text='Calculate Change', width=22, height=2, bg='orange', command=self.change)
        self.change_butn.place(x=350, y=590)

        #generate bill
        self.bill_btn = Button(self.left, text='Generate Bill', width=100, height=2, bg='red', fg='white', command=self.generate_bill)
        self.bill_btn.place(x=0, y=640)

    def add_to_cart(self, *args, **kwargs):
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Out of Stock", "Less in Stocks.")
        else:
             self.final_price = float(self.quantity_value)*float(self.get_price) - (float(self.discount_e.get()))
             product_list.append(self.get_name)
             product_price.append(self.final_price)
             product_quantity.append(self.quantity_value)
             product_id.append(self.get_id)

             self.x_index = 0
             self.y_index = 100
             self.counter = 0
             for self.p in product_list:
                 self.tempName = Label(self.right, text=str(product_list[self.counter]),
                                       font=('arial 18 bold'), bg='lightblue', fg='white')
                 self.tempName.place(x=0, y=self.y_index)
                 labels_list.append(self.tempName)

                 self.tempqt = Label(self.right, text=str(product_quantity[self.counter]),
                                       font=('arial 18 bold'), bg='lightblue', fg='white')
                 self.tempqt.place(x=300, y=self.y_index)
                 labels_list.append(self.tempqt)


                 self.tempprice = Label(self.right, text=str(product_price[self.counter]),
                                       font=('arial 18 bold'), bg='lightblue', fg='white')
                 self.tempprice.place(x=500, y=self.y_index)
                 labels_list.append(self.tempprice)



                 self.y_index += 40
                 self.counter += 1

                 self.total_label.configure(text="Total: Rs= "+str(sum(product_price)))

                 self.quantity_1.place_forget()
                 self.quantity_e.place_forget()
                 self.discount_1.place_forget()
                 self.discount_e.place_forget()

                 self.productname.configure(text='')
                 self.pprice.configure(text='')
                 self.add_to_btn.destroy()

                 self.enteride.focus()
                 self.enteride.delete(0, END)

    def change(self, *args, **kwargs):
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))
        self.to_give = self.amount_given - self.our_total
        self.c_ammount = Label(self.left, text="Change: Rs= " + str(self.to_give), font=('arial 18 bold'), fg='red', bg='white')
        self.c_ammount.place(x=0, y=600)
        self.chaneisThere = 0

    def generate_bill(self, *args, **kwargs):
            directory = "C:/Projects/Python/Store Management Software/Invoice/" + str(date) + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)

            #Template for Bill
            company = "\t\t\t\tSagar  Market Pvt. Ltd.\n"
            address = "\t\t\t\tITER, SOA University, Jagamohan Nagar\n"
            phone = "\t\t\t\t\t0123456789\n"
            sample = "\t\t\t\t\tInvoice\n"
            dt = "\t\t\t\t\t" + str(date)

            table_header = "\n\n\t\t-----------------------------------------\n\t\tSN.\tProducts\tQty\tAmount\n\t\t" \
                           "-----------------------------------------"
            final = company + address + phone +sample + dt + "\n" + table_header
            file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
            f = open(file_name, 'w')
            f.write(final)

            r=1
            i=0
            for t in product_list:
                f.write("\n\t\t" + str(r) + "\t" + str(product_list[i] + ".......")[:7] + "\t" +
                        str(product_quantity[i] )+ "\t" + str(product_price[i]))
                i += 1
                r += 1
            f.write("\n\t\t\tTotal: Rs. " + str(sum(product_price)))
            f.write("\n\t\t\tThanks for Visiting. ")

            os.startfile(file_name, "print")  #PRINTING COMMAND LINE
            f.close()

            #decrease stocks
            self.x = 0

            initial = "SELECT * FROM inventory WHERE id=?"
            result = c.execute(initial, (product_id[self.x],))

            for i in product_list:
                for r in result:
                    self.old_stock = r[2]

                self.new_stock = int(self.get_stock) - int(product_quantity[self.x])
                sql = "UPDATE inventory SET stock=? WHERE id=?"
                c.execute(sql,(self.new_stock, product_id[self.x]))
                conn.commit()

                sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES(?, ?, ?, ?)"
                c.execute(sql2, (product_list[self.x], product_quantity[self.x], product_price[self.x], date))
                conn.commit()
                self.x += 1

            for a in labels_list:
                a.destroy()
            del(product_list[:])
            del(product_quantity[:])
            del(product_price[:])
            del(product_id[:])
            self.total_label.configure(text='')
            if self.chaneisThere == 0:
                self.c_ammount.configure(text='')
            self.change_e.delete(0, END)
            self.enteride.focus()

            tkinter.messagebox.showinfo("Success", "Happy Shopping")







root = Tk()
b = Application(root)
root.geometry('1368x768+0+0')
root.mainloop()