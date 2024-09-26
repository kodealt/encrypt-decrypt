#use of 2d arrays to create a pointing system to a "pixel"
#userInput = input("input x and y for pointer, n < 5, sep with commas (,).\n> ").replace(' ', '').split(',')
#pointerx, pointery = int(userInput[0]), int(userInput[1])

pointerx = 2
pointery = 4

screen = [['◦', '◦', '◦', '◦', '◦'], ['◦', '◦', '◦', '◦', '◦'], ['◦', '◦', '◦', '◦', '◦'], ['◦', '◦', '◦', '◦', '◦'], ['◦', '◦', '◦', '◦', '◦']]
#screen = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
for y, array in enumerate(screen, start=1):
  for x, j in enumerate(array, start=1):
    print("•" if x == pointerx and y == pointery else j, end =' ')
  if y == pointery:
    print('<', end='')
  print()
for i in range(1,6):
  print("^" if i == pointerx else " ", end=" ") 
print()


