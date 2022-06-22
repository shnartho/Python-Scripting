from tkinter import *
import json
import sqlite3
import requests
import time

def connect():
    global cursor, db, dataset
    url = "http://api.worldbank.org/v2/countries?format=json&per_page=40"
    content = requests.get(url)
    dataset = content.json()[1]
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS COUNTRIES (id varchar(3), data json)")
    for country in dataset:
        cursor.execute('INSERT INTO COUNTRIES values (?, ?)',
                       [country['id'], json.dumps(country)])
        db.commit()
    print("Success!!")
    db.close()

connect()

def view_bangladesh():
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM COUNTRIES WHERE id='BGD';''')
        rows = cursor.fetchall()
        db.close()
        return rows

    except Exception as E:
        print('ERROR :', E)

def show_all():
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM COUNTRIES''')
        rows = cursor.fetchall()
        db.close()
        info.set("Viewing All Data")
        return rows

    except Exception as E:
        print('ERROR :', E)
        return False

show_all()

def delete_database():
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('''DROP TABLE COUNTRIES''')
        db.commit()
        db.close()
        info.set("Table Data Deleted")

    except Exception as E:
        print('ERROR :', E)

def bangladesh():
    for row in view_bangladesh():
        list_box.insert(END, row)
    info.set("Viewing Bangladesh")
    status()

def reinsert():
    connect()
    info.set("Data Reinserted")

def clear():
    status()
    info.set("Screen Clear")
    list_box.delete(0, END)

def about():
    list_box.insert(END, "Summery Project")
    list_box.insert(END, "This is a mini project called 'Summery Project'.This is lab 13. The teacher's name is Thomas. Thank you.")
    status()
    info.set("About Information")

def show():
    msg = show_all()
    print(msg)
    if not msg:
        info.set("Table Countries is empty")
    else:
        for row in show_all():
            list_box.insert(END, row)
        info.set("View Success")
        status()



def delete():
    delete_database()
    info.set("Database Deleted")


def status():
    info.set("Please wait")
    sbar.update()
    time.sleep(2)
    info.set("Done")

#tkinter
root = Tk()
root.wm_title("Summary project")
canvas = Canvas(root, height=700, width=1200)
canvas['bg'] = 'green'
canvas.pack()
#status of the tasks
info = StringVar()
info.set("Ready")
sbar = Label(root, textvariable=info, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
#setting frame
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
list_box = Listbox(frame, height=35, width=120)
list_box.grid(row=4, column=1, rowspan=5, columnspan=1)
scroll_bar = Scrollbar(frame, orient='vertical', bg='#7F00FF')
scroll_bar.grid(row=5, column=2, sticky='ns')
list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)
#buttons
Button(frame, text="Show All Data", width=12, bg='#99FFFF', command=show).grid(row=2, column=1)
Button(frame, text="Delete Table", width=12,bg='#99FFFF', command=delete).grid(row=3, column=1)
Button(frame, text="Bangladesh", width=7, bg='#7F00FF', command=bangladesh).grid(row=4, column=0)
Button(frame, text="Reinsert", width=7, bg='#7F00FF', command=reinsert).grid(row=5, column=0)
Button(frame, text="Clear", width=7, bg='#7F00FF', command=clear).grid(row=6, column=0)
Button(frame, text="About", width=7, bg='#7F00FF', command=about).grid(row=7, column=0)
Button(frame, text="Exit", width=7, bg='#7F00FF', command=root.destroy).grid(row=7, column=1)
#start
root.mainloop()
