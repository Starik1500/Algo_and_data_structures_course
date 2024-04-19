def dfs(graph, start, visited):
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current] - visited)
    return visited


def checking_connection(cities, storage, pipelines):
    graph = {city: [] for city in cities}
    unreachable = []
    for pipe in pipelines:
        graph[pipe[0]].append(pipe[1])
        graph[pipe[1]].append(pipe[0])

    for store in storage:
        if len(dfs(graph, store)) < len(graph):
            unreachable.append(
                [store, [city for city in cities if city not in dfs(graph, store)]]
            )
    return unreachable


def reading_from_file():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        cities = lines[0].strip().split(",")
        storage = lines[1].strip().split(",")
        pipelines = lines[2].strip().split(",")
    return cities, storage, pipelines


def writing_to_the_file(unreachable):
    with open("output.txt", "w") as file:
        if unreachable:
            file.write()
            for store, cities in unreachable:
                file.write(f"{store}, {', '.join(cities)}\n")
        else:
            file.write(".")


cities, storage, pipelines = reading_from_file()
unreachable = checking_connection(cities, storage, pipelines)
writing_to_the_file(unreachable)
