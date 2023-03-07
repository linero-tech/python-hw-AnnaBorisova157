from to_do import TODO


def task3(number):
    if number < 0:
        return 0
    elif number == 0 or number == 1:
        return 1
    else:
        fact = 1
        while (number > 1):
            fact *= number
            number -= 1
    return fact



if __name__ == "__main__":
    print(task3(number=5))  # 120
    print(task3(number=7))  # 5040
    print(task3(number=3))  # 6