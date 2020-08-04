

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()

print(plist)
plist.pop(0)
print(plist)
plist.remove("'")
print(plist)
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
print(plist)
new_phrase = ''.join(plist)
print(new_phrase)

