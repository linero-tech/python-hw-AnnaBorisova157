from to_do import TODO


def task2(number):
    if number < 2:
        return False
    for i in range (2, int ( number ** 0.5 + 1)):
        if number % i == 0:
            return False
    else:
        return True



if __name__ == "__main__":
    print(task2(number=5))  # True
    print(task2(number=1))  # False
    print(task2(number=3))  # True