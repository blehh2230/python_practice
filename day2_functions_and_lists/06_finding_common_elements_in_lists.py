def compare(l1,l2):
    common=[]
    for item in l1:
        if item in l2:
            common.append(item)
    return common

l1=[45,87,5,7,4,3,6]
l2=[7,8,3,2,13,18]
common=compare(l1,l2)
print("the common elements are:\n",common)