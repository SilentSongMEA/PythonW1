sumAv=0
counts=0
number0=int(input(f"Enter number {counts}: "))
while number0>=0 :
    counts=counts+1
    sumAv=sumAv+number0
    number0=int(input(f"Enter number {counts} : "))

print(sumAv/counts)     