import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()

def validate(ip):
    try:
        a,b,c,d = ip.split(".")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if(a <= 255 and b <= 255 and c <= 255 and d <= 255):
            return True
        else:
            return False

    except ValueError:
        return False

if __name__ == "__main__":
    main()