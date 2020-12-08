
"""
Purpose: Advent of Code challenge
Day: 7
Date created: 2020-12-07
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from utils import current_file, day_number, read_data

DEBUG: bool = True

# Import data
if DEBUG:
    raw_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """
else:
    # Current file filepath
    thisfile = current_file(__file__)
    
    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")


data = [i.strip() for i in raw_data.split("\n") if len(i.strip()) > 0]

def bag_qty_re(string):
    s = re.findall(r"([\d]+)\s([\w\s]+)", string)

    quantity = s[0][0]
    bag = s[0][1]

    return bag, int(quantity)


##################
# --- Part 1 --- #
##################

bags = {}
for line in data:
    bag, requirements = line.split("contain")

    # Clean up bag name.
    bag = re.sub(r"(\s*bags?\s*)", "", bag)


    # Skip item if 'no other' in requirements.
    if not "no other" in requirements:
        # Set bag name as key
        bags[bag] = []

        # Split by delimiter
        reqs = re.split(r",\s*", requirements)
    
        # Iterate new list of split values
        for r in reqs:
    
            # Clean up string by removing unnecessary words and non-word characters
            r = re.sub(r"\s*bags?.?", "", r.strip())

            # Use function to extract bag name and quantity
            bag_name, qty = bag_qty_re(r)

            # Set key and value of subdictionary to bag_name and quantity.
            bags[bag].append(bag_name)


target = "shiny gold"


targets = set()
for k in bags:
    if target in bags[k]:
        targets.add(k)
    if len(targets) > 0:
        for i in bags:
            tmp = targets.intersection(set(bags[i]))
            if len(tmp) > 0:
                targets.add(i)

total = len(targets)
print(f"The number of bags that eventually can hold {target} is: {total}")


##################
# --- Part 2 --- #
##################

# raw_data = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# """
# data = [i.strip() for i in raw_data.split("\n") if len(i.strip()) > 0]

def prod(iterable):
    """Product of values in array."""
    if len(iterable) == 0:
        return 1
    else:
        return iterable[0] * prod(iterable[1:])


bags = {}
for line in data:
    bag, requirements = line.split("contain")

    # Clean up bag name.
    bag = re.sub(r"(\s*bags?\s*)", "", bag)

    # Set bag name as key
    bags[bag] = {}

    # Split by delimiter
    reqs = re.split(r",\s*", requirements)

    # Iterate new list of split values
    for r in reqs:

        # Clean up string by removing unnecessary words and non-word characters
        r = re.sub(r"\s*bags?.?", "", r.strip())

        if r == "no other":
            bags[bag][r] = 0
        else:
            # Use function to extract bag name and quantity
            bag_name, qty = bag_qty_re(r)
    
            # Set key and value of subdictionary to bag_name and quantity.
            bags[bag][bag_name] = qty


bag_graph = {k:[] if list(bags[k].keys()) == ["no other"] else list(bags[k].keys()) for k in bags}

target = "shiny gold"

targets = [target]

components = []
for k1, v1 in bags.items():
    if k1 in targets:
        components.append([[k] * v for k, v in v1.items()])
        targets = list(v1.keys())

    for k2, v2 in v1.items():
        if k2 == k1:
            print(k1, v1, k2, v2)














def dfs(graph, source,path = []):
    if source not in path:
        path.append(source)
        if source not in graph:
            # leaf node, backtrack
            return path
        for neighbor in graph[source]:
            path = dfs(graph, neighbor, path)
    
    return path


def dfs_traversal(graph, start, visited, path):
    if start in visited:
        return visited, path
    visited.append(start)
    path.append(start)
    for n in graph[start]:
        visited, path = dfs_traversal(graph, n, visited, path)
        # if not n == "no other":
        #     visited, path = dfs_traversal(graph, n, visited, path)
    return visited, path

def conn_components(graph: dict):
    visited = []
    connected_components = []
    for n in graph:
        if not n in visited:
            tmp = []
            visited, tmp = dfs_traversal(graph, n, visited, tmp)
            connected_components.append(tmp)
    return connected_components

def conn_components(graph: dict):
    """This function takes graph as a parameter and then returns the list of 
    connected components
    """

    # graph_size = len(graph)
    # visited = graph_size * [False]
    # components_list = []

    # for i in range(graph_size):
    #     if not visited[i]:
    #         i_connected = dfs(graph, i, visited)
    #         components_list.append(i_connected)

    # return components_list
    graph_size = len(graph)
    components_list = []
    visited = []
    for comp in graph:
        if not comp in visited:
            i_connected = dfs(graph, comp, visited)
            components_list.append(i_connected)
    return components_list


conn_components(bag_graph)




# targets = set([target])
# kvs = list(zip(bags[target].keys(), bags[target].values()))
# total_bags = list(bags[target].values())


# targets = [target]
# for k1, v1 in bags.items():
#     if k1 == target:

#     for k2, v2 in v1.items():
#         if k2 == k1:
#             print(k1, v1, k2, v2)


# for k in bags:
#     tmp = targets.intersection(set(bags[k].keys()))
#     if len(tmp) > 0:
#         targets.add(k)
#         total_bags.append(list(bags[k].values()))



# matches = []
# for ki, vi in bags.items():
#     if target in vi:
#         if not vi in matches:
#             matches.append(ki)

#         for ko, vo in bags.items():
#             if ki in vo:
#                 total += 1

#     subitems1 = list(v1.keys())
#     print(subitems1)
#     if target in subitems1:
#         total += 1
#         target2 =
#         for k2, v2 in bags.items():
#             subitems2 = list(v2.keys())
#             if k1 in subitems2:
#                 total += 1

#     for k2, v2 in v1.items():
#         if target == k2:
#             print(k1, k2)
#             total += 1
#             for k3, v3 in bags.items():
#                 for k4, v4 in v3.items():
#                     if k1 == k4:
#                         print(k1, k4)
#                         total += 1





# ### ORIGINAL
# bags = {}
# for line in data:
#     bag, requirements = line.split("contain")
#     # Clean up main bag, set as key value
#     bag = re.sub(r"(\s*bags?\s*)", "", bag)

#     # Set bag name as key
#     # Set dictionary as type (this will hold all requirements for the bag).
#     bags[bag] = {}

#     # Check for delimiter in requirements
#     if "," in requirements:
#         # Split by delimiter
#         reqs = re.split(r",\s*", requirements)

#         # Iterate new list of split values
#         for r in reqs:

#             # Clean up string by removing unnecessary words and non-word characters
#             r = re.sub(r"\s*bags?.?", "", r.strip())

#             # Use function to extract bag name and quantity
#             bag_name, qty = bag_qty_re(r)

#             # Set key and value of subdictionary to bag_name and quantity.
#             bags[bag][bag_name] = qty
#     else:
#         # Otherwise, clean up unnecessary words and non-word characters.
#         r = re.sub(r"\s*bags?.?", "", requirements.strip())

#         # Check if result is `no other,` which won't require any additional bags.
#         if r == "no other":
#             bags[bag][r] = 0

#         # Otherwise, get the bag name and quantity
#         # then set new key and value for sub-dictionary.
#         else:
#             bag_name, qty = bag_qty_re(r)
#             bags[bag][bag_name] = qty





