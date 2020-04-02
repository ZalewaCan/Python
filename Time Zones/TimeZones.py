offset = [-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
time_h = int(input('What\'s time now, enter hour: '))
time_m = int(input('And minute now: '))
print("[0]GMT -12 ", "[1]GMT -11", "[2]GMT -10 ", "[3]GMT -9 ", "[4]GMT -8  ", "[5]GMT -7 ", "[6]GMT -6  ", "[7]GMT -5")
print("[8]GMT -4  ", "[9]GMT -3 ", "[10]GMT -2 ", "[11]GMT -1", "[12]GMT    ", "[13]GMT +1", "[14]GMT +2 ", "[15]GMT +3")
print("[16]GMT +4 ", "[17]GMT +5", "[18]GMT +6 ", "[19]GMT +7", "[20]GMT +8 ", "[21]GMT +9", "[22]GMT +10", "[23]GMT +11")
print("[24]GMT +12")
desired_tz = int(input("What's desired time zone "))
time_adjusted_h = time_h + offset[desired_tz]
if time_adjusted_h < 0:
    print('Time in new time zone is: ', time_adjusted_h + 12, ':', time_m)
else:
    print('Time in new time zone is: ', time_adjusted_h, ':', time_m)

