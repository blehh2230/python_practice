def freq(list):
    frequency={}
    for ele in list:
        if ele in frequency:
            frequency[ele]+=1
        else:
            frequency[ele]=1
    return frequency

list=[1,2,4,2,5,1,4,4,2,1,3]
result=freq(list)
print("the frequency of elements are",result)