for w in "hello":
    print("corecter:", w)
    
s = "Odesssssa"
new_s = ""
prev_w = ""
for w in s:
    if w != prev_w:
        new_s += w
        prev_w = w
print("New word", new_s)