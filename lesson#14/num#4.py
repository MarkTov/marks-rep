a = int(input("input character for a "))
b = int(input("input character for b "))
c = int(input("input character for c "))

if a == b and b == c and a == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)