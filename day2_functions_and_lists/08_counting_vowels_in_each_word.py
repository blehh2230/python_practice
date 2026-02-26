def counter(sentence):
    count=[]
    vowels="aeiouAEIOU"
    words=sentence.split()
    for i in words:
        temp=0
        for j in i:
            if j in vowels:
                temp+=1
        count.append(temp)
    return count

sentence=input("enter a sentence: ")
print("the number of vowels in each word is:",counter(sentence))


