def dfs(graph, start, visited):
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack.extend(graph[current] - set(visited))
    return visited

def checking_connection(cities, storage, pipelines):
    graph = {city: set() for city in cities + storage}
    for pipe in pipelines:
        graph[pipe[0]].add(pipe[1])
        graph[pipe[1]].add(pipe[0])

    unreachable = []
    for store in storage:
        visited = dfs(graph, store, [])
        if len(visited) < len(graph):
            unreachable.append(store)

    return unreachable

cities = ['Львів', 'Стрий', 'Долина']
storage = ['Сховище_1', 'Сховище_2']
pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2']]

unreachable = checking_connection(cities, storage, pipelines)
print(unreachable)
