from tkinter import *
import sqlite3
from tkinter import messagebox
root = Tk()
conn = sqlite3.connect('facebook.db')
c = conn.cursor()
# c.execute ('''CREATE TABLE user(
#     first_name text,
#     last_name text,
#     age integer,
#     address text,
#     city text,
#     zipcode integer,
#     password integer,
#     Gender text
# )''')
# print("table created successfully")

f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)

age =Entry(root, width = 30)
age.grid(row= 2,column = 1)

address = Entry (root, width=30)
address.grid(row = 3, column= 1)

city = Entry(root, width = 30)
city.grid(row = 4,column= 1)


zipcode = Entry(root, width = 30)
zipcode.grid(row = 5,column= 1)

password = Entry(root, width=30)
password.grid(row = 6,column = 1)

gender=Entry (root, width=30)
gender.grid(row = 7,column = 1)

delete_box = Entry (root,width = 30)
delete_box.grid(row = 14,column = 1, pady= 5)

f_name_label = Label(root,text ='First name')
f_name_label.grid(row = 0,column = 0)


l_name_label = Label(root,text ='Last name')
l_name_label.grid(row = 1,column = 0)

age_label = Label(root,text='Age')
age_label.grid(row= 2,column = 0)

address_label = Label(root,text ='address')
address_label.grid(row = 3,column = 0)

city_label = Label(root,text ='city')
city_label.grid(row = 4,column = 0)


zipcode_label = Label(root,text ='Zipcode')
zipcode_label.grid(row = 5,column = 0)

password_label= Label(root, text='Password')
password_label.grid(row= 6,column= 0)

gender_label = Label(root, text= 'Gender')
gender_label.grid(row= 7,column = 0)

delete_label = Label(root, text = 'Delete ID')
delete_label.grid(row = 14, column = 0 , pady = 5)



def submit():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute('INSERT INTO user VALUES(:f_name, :l_name,:age, :address,:city,:zipcode,:password,:gender)',{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'age':city.get(),
        'address':address.get(),
        'city':city.get(),
        'zipcode':zipcode.get(),
        'password':password.get(),
        'gender':gender.get()
    })

    messagebox.showinfo('user','Inserted Successfully')
    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    password.delete(0,END)
    gender.delete(0,END)

def query ():
    conn = sqlite3.connect('facebook.db')
    c=conn.cursor()
    c.execute('select *, oid from user')
    records=c.fetchall()

    print_records=''
    for record in records:
        print_records+=str(record[0])+' '+str(record[1])+' '+'\t'+str(record[8])+"\n"
    
    
    query_label = Label(root, text = print_records)
    query_label.grid(row = 18, column=0,columnspan= 2)
    
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()

    c.execute('DELETE from user WHERE oId = ' + delete_box.get())
    print('Deleted Successfully')

    delete_box.delete(0,END)
    conn.commit()
    conn.close()

def edit():
    global editor
    editor = Toplevel()
    editor.title('update Data')
    editor.geometry('300x400')
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    global record_id
    record_id = delete_box.get()
    c.execute('select * FROM user WHERE oid=' + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global age_editor
    global address_editor
    global city_editor
    global zipcode_editor
    global password_editor
    global gender_editor

    
    f_name_editor = Entry(editor, width = 30)
    f_name_editor.grid(row = 0, column = 1, padx = 20)

    l_name_editor = Entry(editor, width = 30)
    l_name_editor.grid(row = 1, column = 1)

    age_editor= Entry(editor, width = 30)
    age_editor.grid(row = 2,column= 1)    

    address_editor = Entry (editor, width=30)
    address_editor.grid(row = 3, column= 1)

    city_editor = Entry(editor, width = 30)
    city_editor.grid(row = 4,column= 1)

    zipcode_editor = Entry(editor, width = 30)
    zipcode_editor.grid(row = 5,column= 1)

    password_editor = Entry(editor, width = 30)
    password_editor.grid(row = 6, column = 1)

    gender_editor = Entry(editor, width = 30)
    gender_editor.grid(row= 7, column = 1)

    f_name_label = Label(editor,text ='First name')
    f_name_label.grid(row = 0,column = 0)

    l_name_label = Label(editor,text ='Last name')
    l_name_label.grid(row = 1,column = 0)

    age_label = Label(editor, text='age')
    age_label.grid(row=2,column = 0)

    address_label = Label(editor,text ='address')
    address_label.grid(row = 3,column = 0)

    city_label = Label(editor,text ='city')
    city_label.grid(row = 4,column = 0)

    zipcode_label = Label(editor,text ='Zipcode')
    zipcode_label.grid(row = 5,column = 0)

    password_label = Label(editor, text = 'Password')
    password_label.grid(row = 6, column = 0)

    gender_label = Label (editor, width = 30)
    gender_label.grid(row = 7, column = 0)

    for record in records:
        f_name_editor.insert (0,record[0])
        l_name_editor.insert (0,record[1])
        age_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        city_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
        password_editor.insert(0,record[6])
        gender_editor.insert(0,record[7])
    
    edit_btn = Button (editor, text ='SAVE', command = update)
    edit_btn.grid (row= 10,column = 0,columnspan=2,pady=10,padx=10,ipadx=125)
    conn.commit()
    conn.close()


def update():
    conn= sqlite3.connect('facebook.db')
    c=conn.cursor()
    rec=delete_box.get()
    c.execute('''UPDATE user SET
    first_name = :first,
    last_name = :last,
    age= :age,
    address = :address,
    city = :city,
    zipcode = :zipcode,
    password = :password,
    gender= :gender
    WHERE oid = :oid''',
    {'first':f_name_editor.get(),
    'last' :l_name_editor.get(),
    'age':age_editor.get(),
    'address':address_editor.get(),
    'city':city_editor.get(),
    'zipcode':zipcode_editor.get(),
    'password':password_editor.get(),
    'gender':gender_editor.get(),
    'oid':record_id
            })
    conn.commit()
    conn.close()
    editor.destroy()

submit_btn= Button(root,text='Add records',command = submit)
submit_btn.grid(row=11,column = 0,columnspan = 2,pady=10,padx=10,ipadx=100)

query_btn = Button(root,text= 'Show records', command =query)
query_btn.grid(row = 12, column = 0 ,columnspan= 2 , padx= 10,pady=10,ipadx=100)


delete_btn = Button (root, text = 'Delete', command = delete )
delete_btn.grid(row= 15, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)


update_btn = Button (root, text = ' Update', command = edit)
update_btn.grid(row = 16, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)

conn.commit()
conn.close()
root.mainloop()