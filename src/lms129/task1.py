from to_do import TODO


def task1(a, b):
    result = 0
    for i in range (a,b+1):
        if a >= b:
            result = 0
        else:
            result += i
    return result

if __name__ == "__main__":
       print(task1(a=1, b=5)) #15
       print(task1(a=3, b=3)) #0
       print(task1(a=4, b=4)) # 0
