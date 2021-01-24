#from graph import *
#import graph
import heapq

class SimpleGraph :
    def __init__(self) :
        self.edges = {} # this will contains the graph

    '''def neighbors(self, id) :
        children = self.edges[id]
        return children[0] # to return the children of the node
        '''
    def children(self, id) :
        children = self.edges[id]
        return children[0]

class PriorityQueue :
    def __init__(self) :
        # this queue class is just a wrapper arround the built-in collections.deque class
        self.elements = []

    def empty(self):
        # return True if len(self.elements) == 0
        return len(self.elements) == 0

    def put(self, item, priority) :
        # add element x to the right side of the deque
        heapq.heappush(self.elements, (priority, item))

    def get(self) :
        # remove and return elements from left side
        return heapq.heappop(self.elements)[1]


    
#def g_node (node):
def g_score (node): # receive node as a tuple
    return node[2] # return num_of_level which is in node[2] as  because node = ([ children ],{ tiles }, num_of_level)

# calculate heurisitc of each node
def heuristic (node, goal) : # receive node and goal as a dictionary ( means tiles )
    
    # define tiles to be as a key of each node and goal to get x and y axis
    tiles = ['Y3', 'Y2', 'Y1', ' ', 'R1', 'R2', 'R3']
    heuristics_value = 0
    for count in range(len(tiles)) :
        # if count == 3, means if it equal the available space
        if count == 3 :
            continue
        # to get each grid of each tile of node like : node[tiles[0]] == node['Y3']
        (x1, y1) = node[tiles[count]]
        # to get each grid of each tile of goal like : goal[tiles[4]] == node['R1']
        (x2, y2) = goal[tiles[count]]
        # to calculate the distance of each tile and store it in heuristic_value variable
        # abs means in math | x | = x, | -x | = x
        heuristics_value += abs( x1 - x2 )    
    
    return heuristics_value

def evaluation_function(node, goal) : # receive node and goal as a tuple
    # sent node as it is (means as a tuple) to g_score(), and to heuristic as a dictionary ( for tiles )
    return (g_score(node) + heuristic(node[1], goal[1]))


def a_star_search(graph, start, goal) :
    # to arrange open_list with lowest evaluation_function
    frontier = PriorityQueue()
    # only it's used in if statement to check if the state is in open_list or not
    open_list = set()
    # to add node in close_list
    close_list = set()

    # to return close_list as we written it in paper because set() return with no ordering
    closed_list_back = []
    # to return open_list as we written it in paper because set() return with no ordering
    open_list_back = []

    # to know the parent of the current state which Key is state, and value is parent
    came_from = {}
    # to calculate the cost
    #cost_so_far = {}
    
    # to know that the initial state has no parent
    came_from[start] = None
    # to define the cose of initial state equal 0
    #cost_so_far[start] = 0

    # it is not important in the code, but used to store each state with it's evaluation function
    evaluation_function_with_state = {}

    # to store g(start_state) in this variable, but it is not important because evaluation function calculate it automatically
    #g_start = g_score(graph.edges[start])
    
    # we can calculate evaluation function of start state as it is
    f_start = evaluation_function(graph.edges[start], graph.edges[goal])

    # to store the initial state with it's evaluation function
    evaluation_function_with_state[start] = f_start

    # variable current = start state
    current = start
    # add the current state in open_list
    open_list.add(current)
    open_list_back.append(current)
    # add the current state in Priority Queue with it's evaluation function
    frontier.put(current, f_start)

    while not frontier.empty() : # while open_list is not empty
        # to get the state with the lowest evaluation function
        current = frontier.get()
        
        if current == goal :
            return reconstruct_path(came_from, start, goal), closing_list(closed_list_back), opening_list(open_list_back), came_from

        # set() and list() use the same method remove() to remove state
        open_list.remove(current) # this is set()
        open_list_back.remove(current) # this is list()
        close_list.add(current)

        # to add the current state in the list to return it
        closed_list_back.append(current)

        for next_node in graph.children(current):
            if next_node not in close_list :
                # it is not important 
                evaluation_function_with_state[next_node] = evaluation_function(graph.edges[next_node], graph.edges[goal])
                if next_node in open_list :
                    pass
                else :
                    frontier.put(next_node, evaluation_function_with_state[next_node])
                    open_list.add(next_node)
                    open_list_back.append(next_node)
                    came_from[next_node] = current
            elif next_node in close_list :
                continue
                
    return False


def reconstruct_path(came_from, start, goal) :
    # current = goal
    current = goal
    # in this statement, path will be list, and containing the current
    path =  [current]
    # if the current state was the start state, this loop stops
    while current != start :
        '''
        current will be the node which made me visit this node
        '''
        current = came_from[current]
        # add the current node to the path list
        path.append(current)
    # to reverse the path to get the path from the initial state to the goal
    path.reverse() 
    # return the shortest path
    return path

def opening_list(open_list) :
    open_list.reverse()
    return open_list

def closing_list(close_list) :
    pass
    return close_list
    

# run a_star_search function

# to import graph from graph_file
'''
if you write import graph, you should write file_name.whatever
" whatever " : attribute, function, and so on
example :
print (graph.state_space_graph)
'''

'''
if you write from graph import *, you should write whatever
" whatever " : attribute, function, and so on
example :
print (state_space_graph)
'''

'''
from graph import *

example_graph = SimpleGraph()
example_graph.edges = state_space_graph


path = a_star_search(example_graph, 'A', 'P')
print (path)
'''

