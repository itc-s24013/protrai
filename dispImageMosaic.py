#dispImageMosaic.py
#モノクロ画像に変換
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読み込んでモザイクに変換
    newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300))
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
