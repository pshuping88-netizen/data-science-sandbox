#Question 1.5
#Data
from_ =     ["A","A","B","C","C","D","E"]
to_ =       ["B","C","D","D","E","F","F"]
distance_ = [ 4 , 2 , 5 , 8 , 10 , 6 , 3]

#Structured Data (Edge List)
road_network1 = []

for i in range(len(from_)):
    road_network1.append((from_[i],to_[i],distance_[i]))

print("From    To    Distance")
for road in road_network1:
    print(f"{road[0]}      {road[1]}      {road[2]}")

#Question 1.6
#Uniform-Cost Search
#-an algorithm that expands into the least costly path first

#Rebuilt structure with UCS logic in mind:
road_network2 = {
    "A":[("B",4),("C",2)],
    "B":[("D",5),("A",4)],
    "C":[("D",8),("E",10),("A",2)],
    "D":[("F",6),("B",5),("C",8)],
    "E":[("F",3),("C",10)],
    "F":[("D",6),("E",3)]
}

#(Current node, Total cost from A) <- Idea/Concept
start = "A"
goal = "F"

def uniform_cost_search(graph, start, goal):
    possible_paths = [(0, start, [start])]  #(cost to, current node, [path taken] ) eg (4, "B", ["A", "B"])
    lowest_cost = {}

    while possible_paths:
        possible_paths.sort() #Sorts all paths by cost arranging from lowest to highest

        cost_to, current_node, path_taken = possible_paths.pop(0) #Removes lowest cost path (set) and stores it

        if current_node == goal: #Goal conditions
            print("Goal reached:", path_taken)
            return cost_to

        if current_node in lowest_cost and lowest_cost[current_node] <= cost_to: #Compares cost value for the same node (best known path vs new cost)
            continue

        lowest_cost[current_node] = cost_to #Replaces old path to new best known

        for next_node, edge_cost in graph[current_node]:
            new_cost = cost_to + edge_cost #Builds path total cost in loop
            new_path = path_taken + [next_node] #Builds total path (nodes) in loop
            possible_paths.append((new_cost, next_node, new_path)) #Adds to list as a set. (Explored at while loop)
    return None
#UCS explores in increasing cost order, ensuring cheaper paths are always processed first.

total_cost = uniform_cost_search(road_network2,start,goal)
print(f"Total Cost to Goal {goal}: {total_cost}")
