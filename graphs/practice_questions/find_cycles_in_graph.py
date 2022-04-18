adj_list = {
    "0": ["1","2"],
    "1": ["2"],
    "2": ["3"],
    "3": []
}

def detect_cycle(start_node, adj_list):
    if not adj_list or len(adj_list) == 0:
        return False

    stack = []
    visited = set()

    stack.append(start_node)
    print(stack)
    print(visited)

    while stack:
        curr_node = stack.pop()

        if curr_node in visited:
            return True
        
        visited.add(curr_node)

        for child in adj_list[curr_node]:
            if child not in stack:
                stack.append(child)
        
        print(stack)
        print(visited)

    return False

print(detect_cycle("0", adj_list))