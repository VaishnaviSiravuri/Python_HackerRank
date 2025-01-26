num = int(input())

if(num % 2 != 0):
    print("Weird")
else:
    if(2 <= num <= 5):
        print("Not Weird")
    elif(6 <= num <= 20):
        print("Weird")
    else:
        print("Not Weird")
