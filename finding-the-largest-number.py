largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 45, 73, 56, 94, 64, 77, 51, 32]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print ('after', largest_so_far)
