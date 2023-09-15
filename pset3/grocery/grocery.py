def main():
    display_list()


def display_list():
    list = {}
    while True:
        try:
            item = input().upper()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
        except EOFError:
            for x, y in sorted(list.items()):
                        print(y, x)
            break
main()