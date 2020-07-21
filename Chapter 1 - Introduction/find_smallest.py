#find smallest value

smallest = None
for value in [1,2,3,4,55,6,7,-1,5,-1000]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest)
