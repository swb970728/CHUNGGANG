Sample_list=[8,2,3,-1,7]
def multi(Sample_list):
    result=1
    for i in Sample_list:
        result=i*result
    return result
a=multi(Sample_list)
print (a)
