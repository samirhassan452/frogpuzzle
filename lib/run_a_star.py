from a_star_algorithm import *
from state_space_graph import *
from graph import *
import time

example_graph = SimpleGraph()
example_graph.edges = state_space_graph


path , close_list, open_list, came_from = a_star_search(example_graph, 'A', 'P')

#print(path)

'''
for i in range(len(path)):
    
    #path_graph = state_space_graph[path[i]]
    print (state_space_graph[path[i]])
'''

'''
for i in range(len(path)):
    
    path_graph_path = path_graph[path[i]]
    print (path_graph_path)
 
    #### Delay for 1 seconds ####
    time.sleep(1)
    if (path[i] == 'P'):
        time.sleep(0)

'''







'''print ("Path From Start State to Goal :")
print (path)

print ("Closing List :")
print (close_list)

# used slicing to reverse the list
# we do not use list.reverse() because it reverses the list in place

lists = ['A', 'B', 'C']
listss = [1, 2, 3]

lists.reverse()
print (lists)

but if I write (listss.reverse())
output : None


print ("Opening List :")
print (open_list)


print (came_from)
'''
