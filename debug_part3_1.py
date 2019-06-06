def numbers_greater_than_twenty(list):
	counter=0
	new_list=[]
	while counter<len(list):
		item=list[counter]
		if item>20:
			new_list.append(item)
		counter=counter+1
	return new_list
num_list=[12,312,42,123,5,12,53,75,123,62,9]
number_list_20=numbers_greater_than_twenty(num_list)

print "initial_list",number_list_20

print "list that doesen't contain numbers greater than 20",num_list