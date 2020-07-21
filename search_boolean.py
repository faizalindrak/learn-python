#Search using variable in boolean
found = False
print('before,',found)
for value in [9,4,5,7,6,1,8,4,6,3]:
    if value == 3:
        found = True
    print(found, value)
print('after,',value)