import tkinter
import serial
from tkinter import messagebox
from tkinter import PhotoImage

top = tkinter.Tk()

ser = serial.Serial('COM4', 9600)


def helloCallBack():
   #messagebox.showinfo( "Hello Python", "Hello World")
   print(1)


def toggle(n, tog=[0]):
    print(n)
    string = '';
    code = [1,3,5,7,'s', 'f', 'h','k', 'a','d','g','j']
    if isinstance(code[n-1], int)==True:
        if tog[0]:
            print('off')
            string = str(code[n-1] +1)
            print(string)
            ser.write(string.encode('utf-8'))
        else:
            print('on')
            string = str(code[n-1])
            print(string)
            ser.write(string.encode('utf-8'))
    else:
        if tog[0]:
            print('off')
            string = code[n-1]
            print(string)
            ser.write(string.encode('utf-8'))          
        else:
            print('on')
            string = code[n+3]
            print(string)
            ser.write(string.encode('utf-8'))
    tog[0] = not tog[0]
 
img = PhotoImage(file='C:\\Users\\Marian\\Pictures\\IMG_2649.gif')


h=300
w=300

button1 = tkinter.Button(top, text ="A", command = lambda:toggle(1), image=img, height=h, width=w)
button2 = tkinter.Button(top, text ="B", command = lambda:toggle(2), image=img, height=h, width=w)
button3 = tkinter.Button(top, text ="C", command = lambda:toggle(3), image=img, height=h, width=w)
button4 = tkinter.Button(top, text ="D", command = lambda:toggle(4), image=img, height=h, width=w)
button5 = tkinter.Button(top, text ="E", command = lambda:toggle(5), image=img, height=h, width=w)
button6 = tkinter.Button(top, text ="F", command = lambda:toggle(6), image=img, height=h, width=w)
button7 = tkinter.Button(top, text ="G", command = lambda:toggle(7), image=img, height=h, width=w)
button8 = tkinter.Button(top, text ="H", command = lambda:toggle(8), image=img, height=h, width=w)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=0, column=3)
button5.grid(row=1, column=0)
button6.grid(row=1, column=1)
button7.grid(row=1, column=2)
button8.grid(row=1, column=3)


#add functions (commands) for undo and reset
