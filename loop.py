# print("hello world")
# for i in range(1 ,11):
#     print(i)
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# prime number
num = int(input("Enter a number: "))
i = 1
while i < num:
    if num % i == 0:
        print(num, "is not a prime number")
        break
    
else:
    print(num, "is a prime number")
