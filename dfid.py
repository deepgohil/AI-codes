def dfs_recursive_with_limit(graph, current_node, end_node, visited, depth_limit):
    if current_node == end_node:
        print("End node {} found!".format(end_node))
        return True

    if depth_limit == 0:
        return False

    if current_node not in visited:
        print(current_node, end=' ')
        visited.add(current_node)

        for neighbor in graph[current_node]:
            if dfs_recursive_with_limit(graph, neighbor, end_node, visited, depth_limit - 1):
                return True

    return False

def dfid(graph, start_node, end_node):
    depth_limit = 0

    while True:
        print("\nTrying with depth limit:", depth_limit)
        visited_set = set()
        if dfs_recursive_with_limit(graph, start_node, end_node, visited_set, depth_limit):
            break
        depth_limit += 1

graph = {
    5: [3, 7],
    3: [4, 2],
    7: [8],
    2: [6],
    4: [8],
    8: [],
    6: []
}

start_node = 5
end_node_to_find = 4

dfid(graph, start_node, end_node_to_find)
