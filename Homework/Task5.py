# see Tom's solutions under assets

def solution(graph):
    target = len(graph) - 1
    output = []
    data = [[0]]
    
    while len(data) > 0:
        path = data.pop(0)
        current_node = path[-1]
        
        if target == current_node:
            output.append(path)
            continue
        
        for neighbor in graph[current_node]:
            new_path = path.copy()
            new_path = path.copy()
            new_path.appent(neighbor)
            data.append(new_path)
    
    return sorted(output)