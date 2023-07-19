def sum_of (arr):
    sum=0
    for i in str(arr):
        i=int(i)
        sum+=i
    if sum>=10:
        return sum_of(sum)
    if(sum<10):
        if(sum==1):
            return 1
        else:
            return 0

a=int(input())
print(sum_of(a))


