def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print (gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    fraction = fraction.split("/")
    fraction[0], fraction[1] = int(fraction[0]), int(fraction[1])
    fuel = round((fraction[0] / fraction[1]) * 100)
    return fuel


def gauge(percentage):
    level = ""
    if percentage <= 1:
        level = "E"
    elif 1 < percentage < 99:
        level = f"{percentage}%"
    elif 99 <= percentage <= 100:
        level = "F"
    return level

if __name__ == "__main__":
    main()