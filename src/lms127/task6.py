from to_do import TODO


def task6(base1, base2, height):
    result = 0.5 * (base1 + base2) * height
    return result


if __name__ == "__main__":
    result = task6(base1=10.0, base2=20.0, height=1.0)
    print(result)
