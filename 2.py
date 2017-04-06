Sample_list=[1,2,3,4,5,6,7,8,9]
b=[]
def even(Sample_list):
    for i in Sample_list:
        if i%2==0:
            b.append(i)
even(Sample_list)
print(b)


