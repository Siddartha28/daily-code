#given an array, count number of even and odd and print odd and even count 
array=[1,2,3,4,5]
ecount=0
ocount=0
for i in array:
    if i%2==0:
        ecount=ecount+1
    else:
        ocount=ocount+1
print("evencount:",ecount)
print("oddcount:",ocount)