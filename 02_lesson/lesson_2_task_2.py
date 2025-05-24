# Согласно справке год високосный,
# если год делится на 4 без остатка + не делится на 100 без остатка
# если год делится на 400 без остатка.


year = int(input("Введите год:"))


def is_year_leap(year: int):
    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False


result = is_year_leap(year)


is_year_leap(year)
print(f"год {year}:{result}")
