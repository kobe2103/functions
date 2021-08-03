years = input('請輸入年份: ')
def is_leap(years):
    if int(years) % 4 != 0:
        return False
    elif int(years) % 100 != 0:
        return True
    elif int(years) % 400 != 0:
        return False
    elif int(years) % 3200 != 0:
        return True
    else:
        return False
print(is_leap(years))