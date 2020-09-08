def prime(a):
    if (a > 1):
        for i in range(2, a):
            if (a % i == 0):
                print("{} IS NOT PRIME NUMBER".format(a))
                break
        else:
            print("{} IS PRIME NUMBER".format(a))
    else:
        print("{} IS NOT PRIME NUMBER".format(a))
i=1
while i==1:
    num=int(input("\nENTER ANY NATURAL NUMBER: "))
    prime(num)

    i = int(input("\nIF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))
