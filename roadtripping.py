paths_file = open('paths.txt')
roads = dict()

for line in paths_file:
    road = line.strip().split(' -> ')
    if road[0] in roads:
        roads[road[0]].append(road[1])
    else:
        roads[road[0]] = [road[1]]

print(roads)

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

answer = find_shortest_path(roads, 'A', 'Z')
output = ''
for city in answer:
    output += city
print(output)