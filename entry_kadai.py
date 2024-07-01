#s24013 entry_kadai.py
#エントリーウィジェットで受け付けた金額を税込み(10%)価格として出力するプログラムを作成してください

import tkinter as tk #tkinterをtkと略して使用する

def dispLabel():
    a = int(entry.get()) #entryメソッドを使用して入力を受け付け変数aに格納
    print(f"{a}円の税込み価格を表示しました") #ログの出力
    lbl.config(text=f"{a}円は税込みで{int(a*1.1)}円")



root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200") #画面の大きさを決める

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
