import random


def main():
    lvl = get_level()
    score = 10
    for i in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        z = x + y
        first_try = True
        error = 3
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                break
            except ValueError:
                if first_try:
                    score -= 1
                    first_try = False
                error -= 1
                if error == 0:
                    print(z)
                    break
                print("EEE")
                continue
        if answer != z:
            if first_try:
                    score -= 1
            while answer != z:
                try:
                    error -= 1
                    if error == 0:
                        break
                    print("EEE")
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    error -= 1
                    print("EEE")
                    continue
            print(z)
    print(f"Score: {score}")

def get_level():
    lvl = 0
    while True:
        try:
            lvl = int(input("Level: "))
            if 0 >= lvl or lvl > 3 :
                raise ValueError
            break
        except ValueError:
            pass
    return lvl

def generate_integer(level):
    lbound = [0,10,100]
    ubound = [9,99,999]
    return random.randint(lbound[level - 1], ubound[level - 1])


if __name__ == "__main__":
    main()