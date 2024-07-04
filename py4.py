
for i in range(1,8):
    for j in range(1,8):
        if   j==1 or j==7 or (i==j and i<5) or (i+j==8 and i<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
