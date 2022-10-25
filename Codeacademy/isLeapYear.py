def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            return False
        return True

year = int(input("Year: "))

if is_leap_year(year):
    print("It is!")
else:
    print("Nope.")
