def avg(my_list):
    my_num = 0
    for i in my_list:
        my_num = i + my_num
    average  = my_num / len(my_list)
    return average



print (avg([1,2,3,4,5]))



        