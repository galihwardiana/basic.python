"""loop inside loop
    the inner loop will be executed one time for each iteration of the outer loop"""
for i in range (2):
    for j in range (5):
        print ("{}{}". format(i,j), end=" ")
    print()