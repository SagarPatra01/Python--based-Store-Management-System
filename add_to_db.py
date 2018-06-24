from tkinter import *
import sqlite3
import tkinter.messagebox
import ast

#conn = sqlite3.connect('E:\Projects\Python\Store Management Software\Database\store.db')
conn = sqlite3.connect('store.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS `inventory` ( `id`	INTEGER PRIMARY KEY AUTOINCREMENT, `name`	TEXT,"
          " `stock`	 INTEGER, `cp` INTEGER, `sp` INTEGER, `totalcp`	INTEGER, `totalsp` INTEGER,"
          "  `assumed_profit` INTEGER, `vendor` TEXT, `vendor_phoneno`	INTEGER );")

result = c.execute("SELECT max(id) from inventory")
for r in result:
    id = r[0]


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text='Add To Database', font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=450, y=0)

        self.name_1 = Label(master, text='Enter Product Name', font=('arial 18 bold'))
        self.name_1.place(x=0, y=70)

        self.stock_1 = Label(master, text='Enter Stocks', font=('arial 18 bold'))
        self.stock_1.place(x=0, y=120)

        self.cp_1 = Label(master, text='Enter Cost Price', font=('arial 18 bold'))
        self.cp_1.place(x=0, y=170)

        self.sp_1 = Label(master, text='Enter Selling Price', font=('arial 18 bold'))
        self.sp_1.place(x=0, y=220)

        self.vendor_1 = Label(master, text='Enter Vendor Name', font=('arial 18 bold'))
        self.vendor_1.place(x=0, y=270)

        self.vendor_phone_1 = Label(master, text='Enter Vendor Phone Number', font=('arial 18 bold'))
        self.vendor_phone_1.place(x=0, y=320)

        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=70)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=120)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=170)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=220)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=270)

        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=320)

        self.add_btn = Button(master, text='Add to Database', width=25, height=2, bg='steelblue', fg='white',
                              command=self.get_items)
        self.add_btn.place(x=530, y=370)

        self.clr_btn = Button(master, text='Clear all Fields', width=18, height=2, bg='lightgreen', fg='white',
                              command=self.clear_all)
        self.clr_btn.place(x=380, y=370)

        self.tBox = Text(master, width=60, height=17)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, 'ID has reached upto: ' + str(id))

    def get_items(self, *args, **kwargs):

        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_e.get()

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Empty fields", "Please fill all the entries")
        else:
            self.totalcp = ast.literal_eval(self.cp) * ast.literal_eval(self.stock)
            self.totalsp = ast.literal_eval(self.sp) * ast.literal_eval(self.stock)
            self.assumed_profit = float(self.totalsp - self.totalcp)
            sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit," \
                  "  vendor, vendor_phoneno ) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (
            self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor,
            self.vendor_phone))
            conn.commit()
            self.tBox.insert(END, "\n\nInserted " + str(self.name) + " into the database.")
            tkinter.messagebox.showinfo("Sucess", "Succesfully saved to Database")

    def clear_all(self, *args, **kwargs):

        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)


root = Tk()

b = Database(root)
root.geometry('1368x768+0+0')
root.title("Add To Database")
root.mainloop()
