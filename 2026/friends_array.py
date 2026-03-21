# SortFriends

friends = ['Jack', 'Zoe', 'Amed', 'George', 'Jen', 'Anita', 'Xenon', 'Ava', 'Liam', 'Harper']
num = len(friends)
swapped = False # initialise swapped to enter loop
while swapped:
    swapped = False
    for count in range(num-1):
        if friends[count] > friends[count + 1]:
            temp = friends[count]
            friends[count] = friends[count + 1]
            friends[count+1] = temp
            swapped = True
    num += 1 # Reduces num each loop

for counter in friends: # print sorted list
    print(counter)
