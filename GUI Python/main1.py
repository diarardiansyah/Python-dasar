import tkinter
from tkinter.constants import RIGHT 

windows = tkinter.Tk()
windows.title('Tampilan GUI form nasabah bank')
windows.geometry('500x200')

frame1 = tkinter.Frame(master=windows)
frame1['relief'] = tkinter.GROOVE
frame1['borderwidth'] = 1
frame1.pack(side=tkinter.LEFT, fill=tkinter.Y)

frame2 = tkinter.Frame(master=windows)
frame2['relief'] = tkinter.RIDGE
frame2.pack(side=tkinter.RIGHT)

list = {
    0: "Nama lengkap",
    1: "Nomor rekeking",
    3: "NIK",
    4: "Jenis kelamin",
    5: "Tempat tanggal lahir"
}

i = 5
for i in list:
    label = tkinter.Label(master=frame1)
    label['text'] = list[i], ':'
    label.grid(row=i, column=0, sticky=tkinter.W)

    entry = tkinter.Entry(master=frame2)
    entry['width'] = 50
    entry.grid(row=i, column=1, sticky=tkinter.W)
    i = i+1


button = tkinter.Button(master=frame2)
button['text'] = 'Submit'
button.grid(row=11, column=0, sticky=tkinter.W)

button1 = tkinter.Button(master=frame2)
button1['text'] = 'Close'
button1.grid(row=11, column=1, sticky=tkinter.W)

windows.mainloop()