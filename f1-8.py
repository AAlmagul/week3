def spy_game():
    list1= [1,2,4,0,0,7,5]
    list2= [1,0,2,4,0,5,7]
    sum1=0
    sum2=0
    for i in range(len(list1)):
        if list1[i]==0 and list1[i+1]==0 and list1[i+2]==7:
            sum1+=1
    for i in range(len(list2)):
        if list2[i]==0 and list2[i+1]==0 and list2[i+2]==7:
            sum2+=1
    if sum1>0 :
        print('True')
    else :
        print('False')
    if sum2>0 :
        print('True')
    else :
        print('False')
spy_game()
