#1
a = int(input()) #1-ші бүтін санды енгізу
b = int(input()) #2-ші бүтін санды енгізу
if a <= b : #Егер а b-дан кіші немесе тең болса
   for i in range(a, b+1):
      print(i) #кранға шығару


#2
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)


