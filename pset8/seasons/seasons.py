import re
import sys
import inflect
from datetime import date
p = inflect.engine()


def main():
    try:
        dob = input("Date of birth: ")
        year, month, day = valid_date(dob)
        date_of_birth = date(int(year), int(month), int(day))
        today = date.today()
        get_minutes(date_of_birth, today)
    except:
        sys.exit("Invalid date")


def get_minutes(a, b):
    no_of_days = b - a
    minutes = no_of_days.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


def valid_date(s):
    if re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", s):
        year, month, day = s.split("-")
        return year, month, day


if __name__ == "__main__":
    main()

