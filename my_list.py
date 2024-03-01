#empry list called my_list
my_list = []
#append to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)           
my_list.append(30)
my_list.append(40)
print("after:append",my_list)
#insert 15 at second indexing 
my_list.insert(1,15)
print ("after insert:",my_list)
#extend my_list
my_list.extend([50, 60, 70])
print("after extend:",my_list)
#remove last element from my_list
my_list.remove(70)
print("after.remove:",my_list)
#sort my_list in ascending order
my_list=[50, 60,10, 20, 30, 40,15]
my_list.sort()
print(my_list)
#find and print the index of the value 30 in my_list
index_of_30= my_list.index(30)
print(index_of_30)
