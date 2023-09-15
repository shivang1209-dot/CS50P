str = input("File Name: ").lower().strip()
if str.endswith(".jpg") or str.endswith(".jpeg"):
    print("image/jpeg")
elif str.endswith(".gif"):
    print("image/gif")
elif str.endswith(".png"):
    print("image/png")
elif str.endswith(".zip"):
    print("application/zip")
elif str.endswith(".pdf"):
    print("application/pdf")
elif str.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")
