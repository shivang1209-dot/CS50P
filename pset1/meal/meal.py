def main():
    str = input("What Time Is It? d").strip()
    time = convert(str)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(t):
    h, m = t.split(":")
    h = float(h)
    m = float(m)
    m = m / 60
    return h + m

if __name__ == "__main__":
    main()