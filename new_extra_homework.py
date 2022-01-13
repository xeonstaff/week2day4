#1
#Create a function that returns the sum of the two lowest positive numbers 
# given an array of minimum 4 positive integers. No floats or non-positive 
# integers will be passed.

test1=[5,4,3,2,1,1,2,3,4,5]
test2=[1,2,3,4,5,6,7,8,9]
test3=[0,100,500,1001,100001010101] 

def two_lowest(numa):
    numa.sort()
    return(numa[0]+numa[1])

print(two_lowest(test3)) #all 3 sample tests pass


#2
#Given an array of integers. Return an array, where the first element is 
# the count of positives numbers and the second element is sum of negative numbers. 
# 0 is neither positive nor negative.
#If the input array is empty or null, return an empty array.


test4=[-1,-2,-3,-4,-5,1,2,3,4,5]
test5=[1,2,3,4,5,6,7,8,9]
test6=[-1,-2,-3,-4,-5,-6,-7,-8,-9]
test7=[-100,-50,0,100,500]

def counting(numlist):
    pos_count=0
    neg_count=0
    for num in numlist:
        if num>0:
            pos_count+=num
        if num<0:
            neg_count+=num
    return(pos_count,neg_count)

print(counting(test7)) #passes 4 sample tests

