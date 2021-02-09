import pyautogui, time
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
root = tk.Tk()

#Canvas
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

#Variable
user = tk.StringVar()
passw = tk.IntVar()
cepat = tk.IntVar()


#Tampilan Teks Spambot
tampilan = tk.Label(root, text='SpamBot', fg='black', font=('helvetica', 24, 'italic', 'bold'))
canvas1.create_window(150, 20, window=tampilan)

#InputTeksSpam
label2 = tk.Label(root, text= 'Teks', fg='black', font=('helvetica', 12))
label2.pack()
canvas1.create_window(50, 50, window=label2)
entry1 = tk.Entry(root, bd=5, textvariable=user)
entry1.pack()   
canvas1.create_window(200, 50, window=entry1)


#InputJumlahSpam
label3 = tk.Label(root, text = 'Jumlah (angka)', fg='black', font=('helvetica', 12))
label3.pack()
canvas1.create_window(70, 80, window=label3)
entry2 = tk.Entry(root, bd=5, textvariable=passw)
entry2.pack()
canvas1.create_window(200, 80, window=entry2)

#InputKecepatanSpam
label17 = tk.Label(root, text='Kecepatan', fg='black', font=('helvetica', 12))
label17.pack()
canvas1.create_window(60, 110, window=label17)

#KecepatanSpam(RadioButton)
selected = tk.IntVar()
rad1 = tk.Radiobutton(root, text='Cepat', font=('helvetica', 12, 'bold', 'italic') ,value=0.01, variable=selected)
rad2 = tk.Radiobutton(root, text='Lambat', font=('helvetica', 12, 'bold', 'italic') ,value=2, variable=selected)

canvas1.create_window(170, 110, window=rad1)
canvas1.create_window(175, 135, window=rad2)

#Klik kolom chat segera!...
label7 = tk.Label(root, text='Setelah klik Proccess, klik kolom chat segera!...', fg='black', font=('helvetica', 9, 'bold', 'italic'))
canvas1.create_window(150, 170, window=label7)

#ProgressBar
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(root, length=150, style='black.Horizontal.TProgressbar')

#bar['value'] = 100
bar['value'] = 10
root.update_idletasks()
time.sleep(1)

bar['value'] = 20
root.update_idletasks()
time.sleep(1)

bar['value'] = 30
root.update_idletasks()
time.sleep(1)

bar['value'] = 40
root.update_idletasks()
time.sleep(1)

bar['value'] = 50
root.update_idletasks()
time.sleep(1)

bar['value'] = 60
root.update_idletasks()
time.sleep(1)

bar['value'] = 70
root.update_idletasks()
time.sleep(1)

bar['value'] = 80
root.update_idletasks()
time.sleep(1)

bar['value'] = 90
root.update_idletasks()
time.sleep(1)

bar['value'] = 100

bar.pack(pady = 10)

#canvas1.create_window(150, 135, window=bar)

def hello ():

    #BlankSpace
    label10 = tk.Label(root, text='                                ',)
    canvas1.create_window(150, 200, window=label10)
    label11 = tk.Label(root, text='                                ')
    canvas1.create_window(150, 230, window=label11)

    #PROGRESS-BAR
    bar['value'] = 10
    root.update_idletasks()
    time.sleep(1)

    bar['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    bar['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    bar['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    bar['value'] = 80
    root.update_idletasks()
    time.sleep(1)

    bar['value'] = 100
    root.update_idletasks()
    time.sleep(1)

    bar.pack(pady = 10)
    time.sleep(3)
    #MainScript
    x = 0

    for x in range(int(passw.get())) :
        time.sleep(selected.get())

        pyautogui.typewrite(user.get())
        pyautogui.press('enter')

    #Tampilan teks yang di input oleh user
    berhasil1 = tk.Label(root, text='Teks : ',fg='black', font=('helvetica', 12))
    canvas1.create_window(50, 200, window=berhasil1)
    berhasil2 = tk.Label(root, text='Jumlah : ',fg='black', font=('helvetica', 12))
    canvas1.create_window(50, 230, window=berhasil2)

    #Hasil input oleh user
    label1 = tk.Label(root, text=user.get(), fg='black', font=('helvetica', 12))
    canvas1.create_window(150, 200, window=label1)
    label4 = tk.Label(root, text=passw.get(), fg='black', font=('helvetica', 12))
    canvas1.create_window(150, 230, window=label4)

    #Berhasil
    messagebox.showinfo('SpamBot', 'Spam Berhasil!')

#Tombol Proccess!
button1 = tk.Button(text='Process!',command=hello, bg='brown',fg='white').pack(pady = 10)
canvas1.create_window(150, 160, window=button1)

#Developers
label9 = tk.Label(root, text = 'Made by feboyfierlyan', fg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(150, 280, window=label9)

#MenuButton
menu = tk.Menu(root)
root.config(menu=menu)
#filemenu = tk.Menu(menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label = 'File', menu = filemenu)

def quit():
    time.sleep(3)
    root.quit()

filemenu.add_command(label = 'Exit', command=quit())
#helpmenu = tk.Menu(menu)
filemenu.add_separator()
helpmenu = tk.Menu(menu)
menu.add_cascade(label = 'Help', menu = helpmenu)

def about():
    messagebox.showinfo('About', 'Dibuat oleh @feboyfierlyan404')

helpmenu.add_command(label = 'About', command=about)
helpmenu.add_separator()

root.title("SpamBotV2")
root.mainloop()
