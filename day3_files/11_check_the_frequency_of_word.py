f=open("File1.txt","r")
data=f.read()
words=data.split()
count=0
for word in words:
    if word=="learning":
        count+=1
print("the word learning occurs",count,"times")
f.close()