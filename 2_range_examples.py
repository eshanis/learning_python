#When you specify range, it usually starts with 0. But you can specify where to start like below example: starting at 1 and go upto 10
print("find product")
product = 1
for n in range(1,10):
    product = product * n

print(product)

print("-------------------------------------------------")
#you can also specify the increments: starting from 0 to 101 in increments of 10
print("convert to celsius")
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))
