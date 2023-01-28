#Write your code here.
number = eval(input())
number = [str(x) for x in number]
for i in range(len(number)):
    temp = ""
    while number[i]:
        if len(number[i])<3:
            temp = number[i][-1:-4:-1] + temp
        else:
            temp = number[i][-1:-4:-1] + "," +temp
        number[i] = number[i][:-4]
        
print(number)
