#「turtle3.py」という名前で保存しましょう
#正方形を描く
from turtle import * #タートルグラフィックスを使う準備

shape("turtle") #カメの登場
col=["red","blue","green","brown","black"]
for i in range(5):
    color(col[i])
    forward(200)
    left(144)
    
done() #おしまい
