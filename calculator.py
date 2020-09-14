calculate = True
while calculate:
    n1 = int(input("n1:"))
    n2 = int(input("n2:"))
    print("1 for sum\n2 for sub\n3 for multiplication\n4 for division")
    choice = int(input("enter your choice: "))
    if choice == 1:
        print(n1+n2)
    elif choice == 2:
        print(n1-n2)
    elif choice == 3:
        print(n1*n2)
    elif choice == 4:
        print(n1/n2)
    print("do you want to continue press 1 or any number to exit:")
    ch = int(input())
    if ch == 1:
        continue
    else:
        calculate = False
        break
    
