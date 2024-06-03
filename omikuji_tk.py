#s24013
#omikuji.pyをGUIで動かすプログラム
import tkinter as tk

root=tk.Tk()
import random
root.geometry("500x800")
root.title("GUI式おみくじ")
kuji = ["大吉","中吉","小吉","凶","大凶"]
lbl=tk.Label(text=random.choice(kuji))
lbl.pack()
root.mainloop()




