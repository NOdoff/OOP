from stack import Stack

s = Stack()

num = input("Enter the numbers: ")

l_num = list(num.split(' '))
for value in l_num:
    s.push(value)

t_c = s.size()
print("Total Count: " + str(t_c))

sum = 0
product = 1
min = 10000000000000000000000000000000
max = 0
for item in range(0, s.size()):
    value = int(s.pop())
    if value < min:
        min = value
    if value > max:
        max = value
    sum += value
    product *= value
    print(str(sum))
    print(str(product))
    print(str(value))
mean = sum / t_c
print("Sum: " + str(sum))
print("Product: " + str(product))
print("Mean: " + str(mean))
print("Min: " + str(min))
print("Max: " + str(max))






