import random
print("\n\nWelcome to the PYTHON QUIZ PROGRAM...")
ans="y"
while ans=="y":
    print("\n\nSelect a level:\n\neasy\nhard\nvery hard")
    a=input("\nEnter your choice: ")

    if a=="easy":
        s=0
        print("\nChoose the field no.:\n\nMultiplication(1)\nAddition(2)\nSubstraction(3)")
        b=int(input())
        print()

        if b==1:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(0,20),random.randint(0,20)
                print("\nQ",i,".  ",k,"X",m,"?")
                c=int(input("Ans:   "))
                if c==k*m:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k*m)
                    s-=1

        if b==2:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(0,20),random.randint(0,20)
                print("\nQ",i,".  ",k,"+",m,"?")
                c=int(input("Ans:   "))
                if c==k+m:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k+m)
                    s-=1

        if b==3:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(0,20),random.randint(0,20)
                print("\nQ",i,".  ",k,"-",m,"?")
                c=int(input("Ans:   "))
                if c==k-m:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k-m)
                    s-=1

    if a=="hard":
        s=0
        print("\nChoose the field no.:\nMultiplication(1)\nAddition(2)\nSubstraction(3)")
        b=int(input())
        print()

        if b==1:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(0,100),random.randint(0,100)
                print("\nQ",i,".  ",k,"X",m,"?")
                c=int(input("Ans:   "))
                if c==k*m:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k*m)
                    s-=1

        if b==2:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(0,100),random.randint(0,100)
                print("\nQ",i,".  ",k,"+",m,"?")
                c=int(input("Ans:   "))
                if c==k+m:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k+m)
                    s-=1

        if b==3:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(0,100),random.randint(0,100)
                print("\nQ",i,".  ",k,"-",m,"?")
                c=int(input("Ans:   "))
                if c==k-m:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k-m)
                    s-=1

    if a=="very hard":
        s=0
        print("\nChoose the field no.:\nMultiplication(1)\nAddition(2)\nSubstraction(3)")
        b=int(input())
        print()

        if b==1:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(100,200),random.randint(100,200)
                z=random.randint(0,20)
                print("\nQ",i,".  ",z,"X",k,"X",m,"?")
                c=int(input("Ans:   "))
                if c==k*m*z:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k*m*z)
                    s-=1

        if b==2:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(100,10000),random.randint(100,10000)
                z=random.randint(0,20)
                print("\nQ",i,".  ",k,"+",z,"+",m,"?")
                c=int(input("Ans:   "))
                if c==k+m+z:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k+m+z)
                    s-=1

        if b==3:
            print("\nAnswer the following questions:\n")
            for i in range(1,6):
                k,m=random.randint(100,1000),random.randint(100,1000)
                z=random.randint(0,20)
                print("\nQ",i,".  ",k,"-",m,"-",z,"?")
                c=int(input("Ans:   "))
                if c==k-m-z:
                    print("Coprrect!!! pt.+2")
                    s+=2
                else:
                    print("Wrong answer!!! pt.-1")
                    print("Correct ans is: ",k-m-z)
                    s-=1

    print("\n\nYour score = ",s,"Out of 10\n")
    ans=input("Do you want to continue? (y/n): ")
