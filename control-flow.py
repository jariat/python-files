if True:
    print("this statement is true")
if 2<1:
    print("Two is less than one") 
elif 1<2:
    print("one is not greater than two")

else:
    print("one is equal to two")  
#while iteration
num = 1
while num <= 10:
    print(num)
    num += 1

loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False

a = True
while a:
    print("a is: %s" % a)
    a = False
#for statement
for i in range(1,11):
    print(i)


