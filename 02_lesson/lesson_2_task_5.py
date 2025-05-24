def month_to_season(month_number):
    if month_number == 12 or 1 <= month_number <= 2:
        print("Winter")
    elif 3 <= month_number <= 5:
        print("Spring")
    elif 6 <= month_number <= 8:
        print("Summer")
    elif 9 <= month_number <= 11:
        print("Autumn")
    else:
        print("Некорректный номер месяца")


month_number = int(input("Введите номер месяца:"))

month_to_season(month_number)
