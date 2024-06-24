#s24013
#時間を秒単位でウィンドウに表示するプログラム

import datetime
import tkinter as tk #GUIでアプリを作ることができるモジュール

#時間を処理する部分を関数で実装
def update_time():
    now=datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    lbl.config(text=current_time)
    root.after(1000, update_time)#1秒ごとに(update_time)を呼び出す
    
#Tkinterのウィンドウを作成
root = tk.Tk() #初めのおまじない

root.title("時計アプリ")#ウィンドウにつく名前

lbl = tk.Label()
lbl.config(text="", font=("Helvetica",20))#font=("フォント名",フォントサイズ)
lbl.pack()

#関数の呼び出し
update_time()


root.mainloop() #終わりのおまじない
