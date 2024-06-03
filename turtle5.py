#s24013
#赤い線で十字架を描くプログラム
from turtle import * #タートルグラフィックスを使う準備

shape("turtle") #カメの登場
col=["tomato"]
for i in range(4):
    color(col)
    forward(100) #半径100の円を描くこと
    left(90)
    forward(100)
    right(90)
    forward(100)
    left(90)
    forward(10)
done() #おしまい
