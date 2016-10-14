# Python-Range-function
Creates a list of index numbers that will be used in a for loop
(use "git add py43of63.py to include in what will be committed)

 
 
#print'PYTHON Lesson 43 of 63'


'''Start IDLE and use the Python range() function with one
parameter to display the following:
0
1
2
3'''


#Drill 1
my_list=('0', '1', '2', '3')

my_list_len=len(my_list) #lenght of list

for i in range(0, my_list_len):

    
     print(my_list[i])

    





#Use the Python range() function with 3 parameters to display the following:



#Drill 2
my_list= ['0', '1', '2', '3']

my_list = [int(x) for x in my_list]

my_list_len=len(my_list)


my_list.sort()


my_list.sort(reverse=True)

for i in range(0, my_list_len):


     print(my_list[i])



#Drill 3
my_list= ['8', '6', '4', '2']


my_list = [int(x) for x in my_list]

my_list_len=len(my_list)


my_list.sort()


my_list.sort(reverse=True)

for i in range(0, my_list_len):


     print(my_list[i])


  

  
