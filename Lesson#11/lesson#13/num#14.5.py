word = input("enter word ")
code = ""


for x in word:
    #code = str(ord(x))
    code += str(ord(x) + 1)
    code == chr(code)
print(f"new word {code}")