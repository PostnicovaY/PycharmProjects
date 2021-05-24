for i in range(1, 21):
    if(i == 1):
        print(f'{i} процент')
    elif(i <= 4):
        print(f'{i} процента')
    else:
        print(f'{i} процентов')

#Решила написать дополнительно функцию склонения, если диапазон будет расширен

#def sklonenia(N):
#    if (N % 100 >=11 and N % 100 <= 14):
#        return "процентов"
#    elif N % 10 == 0:
#        return "процентов"
#    elif N % 10 == 1:
#        return "процент"
#    elif N % 10 <= 4:
#        return "процента"
#    else:
#        return "процентов"
#for i in range(1,121):
#    print(f"{i} {sklonenia(i)}")