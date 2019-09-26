import tkinter as tk

HEIGHT = 700
WIDTH = 800
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root,bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

button = tk.Button(frame, text="intratech", bg='gray')
button.pack(side='left',fill='x' , expand=True)

label = tk.Label(frame, text = "이것이 레이블이다.", bg='yellow')
label.pack(side='left',fill='both',expand=True)

entry = tk.Entry(frame, bg='green')
entry.pack(side='left',fill='both',expand=True)

root.mainloop()