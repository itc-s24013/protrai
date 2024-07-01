#s24013
#app2.py
import tkinter as tk


def dispLabel():
    lbl.config(text="こんにちは")


root = tk.Tk()#画面を作る
root.geometry("400x200")#画面の大きさを決める


lbl = tk.Label(text="LABEL", font=("Helvetica", 20))#ラベルを作る
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20))#ボタンをつくる


lbl.pack()#画面にラベルを配置する
btn.pack()#画面にボタンを配置する

lbl2=tk.Label(text='ラベル2', font=("Helvetica", 20)).pack()
btn = tk.Button(text="何もしないボタン", command=dispLabel, font=("Helvetica", 20)).pack()#ボタンをつくる
tk.mainloop()#作ったウィンドウを表示する

