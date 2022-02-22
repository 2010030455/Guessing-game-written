import random
num=random.randint(1,100)
exit=0
while(exit==0):
    user=int(input("enter the guessing number = "))
    if(num>user):
        print("TOO LOW")
    elif(num<user):
        print("TOO HIGH")
    else:
        print("correct answer")
        exit=1



