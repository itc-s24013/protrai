#s24013 def4.py
#戻り値のない関数(おみくじ)
#戻り値は関数の外で用意する

import random

#ランダムでkujiの中の一つを返す関数
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

kekka = omikuji()
print("結果は", kekka, "です")
