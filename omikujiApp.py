#s24013
#おみくじプログラム モジュール名「omikuji.py」
import random
import tkinter as tk

def omikuji():
    kuji = ["大吉","中吉","小吉","凶","大凶","半吉","末吉","大大吉"]
    lbl.config(text=random.choice(kuji))

root = tk.Tk()
root.geometry("400x200")


lbl = tk.Label(text="おみくじ", font=("Helvetica", 20))
btn = tk.Button(text="おみくじ", command=omikuji, font=("Helvetica", 20))
lbl.pack()
btn.pack()
tk.mainloop()
