"""
整数のみを要素に持つリストの総和を返す関数 caluculation_sum を実行
"""


# 使い方イメージ

def calculation_sum(numbers):
    total = 0
    for number in numbers:
        total += number

    return total


if __name__ == '__main__':
    numbers = [34, 12, 59, 4]
    total = calculation_sum(numbers)
    print(total)
