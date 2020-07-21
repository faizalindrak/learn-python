#average the loop
counter = 0
total = 0
print ('before', counter, total)
for sesuatu in [1,2,3,45,78,56,7,9,12,33,46,75,61,34,8,1,6]:
    counter = counter + 1
    total = total + sesuatu
    print(counter, total)
print('after', counter, total, round(total/counter,2))