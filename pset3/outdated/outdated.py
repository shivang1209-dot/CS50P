def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    month = ""
    day = ""
    year = ""
    while True:
        date = input("Enter Date: ")
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            month, day, year = date.replace(",", "").split()
            if month in months:
                month = months.index(month) + 1
            else:
                continue
        try:
            day = int(day)
            year = int(year)
            month = int(month)
            if day > 31 or month > 12:
                continue
        except ValueError:
            continue
        break

    print(f"{year}-{month:02}-{day:02}")

main()
