x = 10
print("x gives me",x)
y = 2
print("y gives me", y)
z = y*x
print("z gives me",z)

a = 2
while a < x:
    print("a is",a)
    a+=1
    #This is a one line comment
    '''
    this is a
    multi line comment
    '''

list = [3,2,56,32,12,46,6,3,2]
for item in list:
    print(item)

for num in range(1,11) : #first number is inclusive, second is exclusive
    print("num is",num)

if x>y:
    print(x,"is more than",y)

if x==z:
    print(x,"equals",z)
else:
    print(x,"does not equals",z)

if x==y:
    print("x equals y")
elif x<y:
    print("x is less than y")
else:
    print("x is more than y")

