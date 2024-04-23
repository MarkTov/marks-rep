dig1 = int(input("diget for a ticet"))
dig2 = int(input("diget for a ticet"))
dig3 = int(input("diget for a ticet"))
chislo = dig1 * 100 + dig2 * 10 + dig3 * 1
s = dig1 + dig2 + dig3
if s == 20:
    print("Your ticet is lucky")
else:
    print("Your ticet isn`t lucky, try next time")