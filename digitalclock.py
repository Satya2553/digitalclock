import tkinter as tk
from tkinter import Label,StringVar,Button
from datetime import datetime
from tkcalendar import Calendar
import calendar

mainWindow=tk.Tk()
mainWindow.title("DIGITAL CLOCK")

date_time_str=StringVar()
current_time = datetime.now()
day=current_time.strftime('%d')
month=current_time.strftime('%m')
year=current_time.strftime('%Y')



def update_date_time():
    day=datetime.today().strftime("%A")
    month=datetime.today().strftime("%B")
    year=datetime.today().strftime("%Y")
    time=datetime.today().strftime("%X")
    date=datetime.today().strftime("%d")
    
    date_time_full_str=month + " " + date + " " + year + "\n" + day + " " + time
    date_time_str.set(date_time_full_str)
    date_time_label.after(1000,update_date_time)


date_time_label=Label(mainWindow,textvariable=date_time_str,
                      width='60',
                      height='3',
                      bg='black',
                      fg='white',
                      font=("Times New Roman",40))

date_time_label.pack(anchor='center')


cal=Calendar(mainWindow,selectmode='day',year=int(year),month=int(month),day=int(day))
cal.pack(pady='10')
update_date_time()
# yy=int(year)
# mm=int(month)
# def previous():
#     mm=int(month)
# def next():
#     mm=int(month)
# previous=tk.Button(mainWindow,text="PREVIOUS",command=previous)
# next=tk.Button(mainWindow,text="NEXT",command=next)
# previous.pack()
# next.pack()
# calendar_label=Label(mainWindow,text=calendar.month(yy,mm),relief='groove',bg='black',fg='white',font=19)
# calendar_label.pack()
mainWindow.geometry('800x400')
mainWindow.resizable(False,False)
mainWindow.mainloop()