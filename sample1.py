import random

# list1 = [0,1,2,3,4,5]
list1 = ['gymfit', 'outfit', 'yogababe', 'fitness', 'clothes', 'gymgirl', 'girlsport', 'girloutdoors', 'girlyoga',
            'yoga']

for i in range(1,len(list1)+1):
    list2 = random.sample(list1, 1)
    #print ('list2',list2)
    list3 = [f for f in list1 if f not in list2]
    list1 = list3
    print (list2[0])