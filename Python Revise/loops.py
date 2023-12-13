#for loop

print(1)
print(2)
print(3)

for i in range(1,8):#starts from 1, 8-1
    if(i==5):
        break
    print(i)


for i in range(1,8):#starts from 1, 8-1
    if(i==5):
        continue
    print(i)

for i in range(1,8,2):#starts from 1, 8-1, step size 2
    print(i)

for i in range(8,1,-2):#starts from 8, 1+1, step size -2
    print(i)

for i in range(5): #0 to 5-1
    # print(i+1)
    print(i)

print("-----while loop-----")
#while loop

i=1
while i<=5:
    print(i)
    i=i+1


# while(True):
#     print("Program not finishing")

while(True):
    num=int(input("Enter Number: "))
    print(num)
    if(num==5):
        break
