# Disjoint Sets
# Involve two main functions - find(), union()
"""
find(node k):
step - 1:
finds and returns the root node for the given node k

union(node x, node y):
step - 1: 
choose x or y as a parent and assign the other nodes to the corresponding parent
step - 2:
If other node is not connected to any other set - then directly change the parent
If node is connected to another set - then choose root node of another set and assign its parent as the chosen parent
"""


# Implementation of the disjoint sets as explained in this Explore card - https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3881/
# Such an amazing article which made the concept very clear - Lets implement my way to see my understanding of the concept

# Question: Given two nodes x and y, say whether x and y are connected return True if they are connected, False if they aren't

# Approach
# As there is a chance of disconncted concept, we can check to see if some elements can be grouped as a set - like a connected component - so the Disjoint sets concept

# number of vertices: starting from 0..9
n = 10
# Edges: list of tuples(node a, node b)
edges = [(0, 1), (1, 3), (0, 2), (4, 8), (5, 7), (5, 6)]
# Initialize the vertex/nodes list - indices represent the node and values signify the parent nodes in the graph connectivity 
parent_lst = [v for v in range(n)]
# Test format: list of tuples(node a, node b)
test = [(0, 3), (1, 5), (7, 8)]

def find(v):  
    if parent_lst[v] == v:
        return v
    return find(parent_lst[v])
    
def union(parent, v):   
    # check if node is independent
    if parent_lst[v] == v:
        parent_lst[v] = parent
    else:
        root = find(v)
        parent_lst[root] = parent   

# traverse edge list to group/union the nodes 
for edge in edges:
    parent, v = edge 
    union(parent, v)
    
# Now, its the time to check if certain nodes are connected
def isConnected(nodeA, nodeB):
    return find(nodeA) == find(nodeB)

def testFunctionality():
    for nodeA, nodeB in test:
        res = isConnected(nodeA, nodeB)
        print(f"Is node {nodeA} and node {nodeB} connected? {res}")

# Test - 1
print("Test 1 - Results")
print("parent list = ", parent_lst)
# 0-1-3 4-8 5-6 9
# |         |
# 2         7
testFunctionality()
print()

# 0-1-3 4-8-5-6 9
# |         |
# 2         7
union(8, 7)
print("parent list = ", parent_lst)
testFunctionality()
print()

# Test 2
print("Test 2 - Results")
parent_lst = [v for v in range(n)]
# 1-2-5-6-7 3-8-9 4
union(1, 2)
union(2, 5)
union(5, 6)
union(6, 7)
union(3, 8)
union(8, 9)
print("parent list = ", parent_lst)
print("isConnected(1, 5)? ", isConnected(1, 5))  # true
print("isConnected(5, 7)? ", isConnected(5, 7))  # true
print("isConnected(4, 9)? ", isConnected(4, 9))
print()

# 1-2-5-6-7 3-8-9-4
union(9, 4)
print("parent list = ", parent_lst)
print("isConnected(4, 9)? ", isConnected(4, 9))  # true
