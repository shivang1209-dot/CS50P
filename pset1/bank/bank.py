str = input("Greeting: ").strip().lower()
print(str)
if str == "hello" or str == "hello,":
    print("$0")
elif str[0] == "h":
    print("$20")
else:
    print("$100")