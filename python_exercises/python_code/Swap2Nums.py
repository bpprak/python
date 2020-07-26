num1 = input("Enter num1 value:")
num2 = input("Enter num2 value:")

print("value of num1 before swapping:", num1)
print("value of num1 before swapping:", num2)


temp = num1
num1= num2
num2 = temp


print("value of num1 after swapping:", num1)
print("value of num1 after swapping:", num2)

#Approach:2

num1, num2 = num2, num1


