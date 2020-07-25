planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

for i in range(5):
    print("Doing important work. i =", i)

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,areax in enumerate(areas) :
    print("room"+str(index)+": "+str(areax))

i = 0
while i < 10:
    print(i, end=' ')
    i += 1