def check(word):
    with open("File1.txt", "r") as f:
        line_num = 1
        for line in f:
            if word in line:
                return line_num
            line_num += 1
    return -1

print("The word occurs in line", check("good"))



