
my_list = [9, 0, 6, 8, 6, 7, 7, 8, 7, 7]
count=0

for digit in range(len(my_list)-1):
    if my_list[digit]== my_list[digit+1]:
        count+=1
        
print(count)
