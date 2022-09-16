'''
NOTE :==> All EXAMPLES CODES ARE GIVEN UNDER COMMENT SECTON.

 1. Sequential Control : simple output or without any conditons
                       1.-----------------      |
                       2.-----------------      |
                       3.-----------------      |
                       4.-----------------      |
                                               \/

2. Selection Control : true or false

                      conditions
                           /\
                         /   \
                       /      \
                  If true    if false
               1.--------     1.----------
               2.--------     2.----------
               3.--------     3.----------

3. Iterative Control : Loops

                          |------->-----conditons----->----|-----|
                          |        -------------           |     |
                         /\         --------------   true \/     | false
                         |  in loop    -----------        |     \/
                        |-------<-----------<-------------|     |
                                                                |
                                                    <-<--<------|



'''
#EXAMPLES
# 1. sequential control:
print ("hello world")
print ("what are you doing?")
print ("I am learning python3.10")

#2. Selection Control :
a = int(input ("enter any number:"))
if a<50:
    print("It is smaller than 50")
elif a==50:
    print("it is equal to 50")
else:
    print ("It is bigger than 50")

#3. Iterative control:
b = 0
while b<=5:
    print (b)
    b=b+1



def sum (a,b):
    sum = a+b
    return sum