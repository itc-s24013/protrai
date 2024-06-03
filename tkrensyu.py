#GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ

root = tk.Tk() #初めのおまじない

root.geometry("500x800") #運動のサイズを決める
root.title("ハローアプリ")
lbl = tk.Label(text="こんにちは世界") #いつもの
llbl = tk.Label(text="初めてのGUIアプリ")
lbl.pack() #lblを配置させる必要があるよ
llbl.pack()
root.mainloop() #終わりのおまじない
