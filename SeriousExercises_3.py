number = [1,6,8,1,2,1,5,6]

num = int(input("Which number ?"))

print(num, " appears ", number.count(num)," times in my list")# co dung count()





timeappear = 0
for nums in number :
    if nums == num :
        timeappear += 1
    else :
        a = 1
print(num, " appears ", timeappear, " times in my list")# khong dung count()