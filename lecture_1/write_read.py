with open('diary.txt', 'w') as f:
    f.write("I am learning Python programming.\n")
    f.write("I am learning how to use APIs.\n")


with open('diary.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())