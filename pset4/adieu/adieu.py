import inflect

a = inflect.engine()
names = []
try:
    while True:
        names.append(input("Input: "))
except EOFError:
    print("\nAdieu, adieu, to", a.join(names))