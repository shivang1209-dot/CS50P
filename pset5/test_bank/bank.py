def main():
    str = input("Greeting: ").strip()
    amt = value(str)
    print(f"${amt}")

def value(greeting):
    if greeting.lower() == "hello" or greeting.lower() == "hello,":
        amt = 0
    elif greeting[0].lower() == "h":
        amt = 20
    else:
        amt = 100
    return amt

if __name__ == "__main__":
    main()