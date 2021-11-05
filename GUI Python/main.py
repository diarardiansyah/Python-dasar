import tkinter

main_window = tkinter.Tk()
main_window.title('Membuat GUI sederhana \nwith python')

def event_click():
    text3 = tkinter.Label(main_window, text="Diar ardiansyah sangat ganteng sekali")
    text3.pack()

text1 = tkinter.Label(main_window, text="Halo guys selamat malam semua \nsemoga sehat sehat selalu ya")
button1 = tkinter.Button(main_window, text="click disini bosqyuhh", command=event_click)


text1.pack()
button1.pack()
main_window.mainloop()