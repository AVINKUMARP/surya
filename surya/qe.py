test_list = [2,3,4,5,6]
print("The original list is : " + str(test_list))
 
odd_sum = 0
even_sum = 0
 
for sub in test_list:
    for ele in str(sub):
        if int(ele) % 2 == 0:
            even_sum += int(ele)
        else:
            odd_sum += int(ele)
print("Odd digit sum : " + str(odd_sum))
print("Even digit sum : " + str(even_sum))