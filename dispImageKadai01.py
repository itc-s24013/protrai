#s24013
#選択した画像を表示し、そのパスをラベルとシェルに表示する画像アプリバージョン2.0
#dispImageKadai01.py
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath) #dispPhotoを呼び出す
        print(fpath)
        lbl = tk.Label(text=fpath)
        lbl.pack()

root = tk.Tk()
root.geometry("400x400")

lbl = tk.Label(text="画像アプリバージョン2.0", font=("Helvetica", 20))
btn = tk.Button(text="ファイルを開く", command = openFile) #openFile関数が呼び出される
imageLabel = tk.Label()
lbl.pack()
btn.pack()
imageLabel.pack()
tk.mainloop()
