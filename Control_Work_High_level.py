word = input("word for deliting duplicats  ")
new_s = ""
prev_w = ""
for w in word:
    if w != prev_w:
        new_s += w
        prev_w = w
print("New word", new_s)  


