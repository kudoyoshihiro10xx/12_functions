# 2分課題: 2つの整数の和を返す関数addを作る

def add(a: int, b: int) -> int:
    return a + b




# 2分課題: 2つの整数の差を返す関数を作る

def sub(a: int, b: int) -> int:
    return a - b


# if以下のみsample05でtureなので表示される。その他ではfaluseになる
if __name__ == "__main__":
    y1 = add(a=3, b=4)

    print(y1)

    y1 = sub(a=3, b=4)

    print(y1)
