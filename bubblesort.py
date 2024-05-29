#bubble, scratch
list = []
do = True
while do:
    do = False
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            do = True

print(list)
