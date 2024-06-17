#s24013 def4_kadai.py
#メインの処理をmain()関数に行わせるコード
#

import random
def kuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

def main():
    kekka = kuji()
    print("結果は", kekka, "です")

if __name__ == "__main__":
    main()

