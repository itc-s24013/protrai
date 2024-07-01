#s24013
#モノクロ画像に変換して、90°回転させた後、反転させる
#dispImageKadai02.py
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読み込んでモザイクに変換
    newImage = PIL.Image.open(path).convert("L").rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath) #dispPhotoを呼び出す

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile) #openFile関数が呼び出される
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
