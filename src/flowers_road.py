import csv
import os
from collections import defaultdict
from typing import List, Dict, Tuple


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, start: str, end: str, capacity: int):
        self.graph[start][end] = capacity
        if end not in self.graph:
            self.graph[end] = {}

    def dfs(
        self,
        graph: Dict[str, Dict[str, int]],
        source: str,
        sink: str,
        visited: Dict[str, bool],
        parent: Dict[str, str],
    ):
        stack = [source]
        visited[source] = True
        while stack:
            current = stack.pop()
            for neighbor, capacity in graph[current].items():
                if not visited[neighbor] and capacity > 0:
                    stack.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current
                    if neighbor == sink:
                        return True
        return False

    def ford_fulkerson(self, source: str, sink: str) -> int:
        parent = {}
        max_flow = 0
        while self.dfs(self.graph, source, sink, defaultdict(bool), parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] = self.graph[v].get(u, 0) + path_flow
                v = parent[v]
        return max_flow


def read_roads(
    filename: str,
) -> Tuple[List[str], List[str], List[Tuple[str, str, int]]]:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        farms = [farm.strip() for farm in data[0]]
        shops = [shop.strip() for shop in data[1]]
        lines = [(row[0].strip(), row[1].strip(), int(row[2])) for row in data[2:]]
    return farms, shops, lines


def build_graph(
    farms: List[str], shops: List[str], roads: List[Tuple[str, str, int]]
) -> Tuple[Graph, int, int]:
    graph = Graph()
    num_farms = len(farms)
    num_shops = len(shops)

    for road in roads:
        start, end, capacity = road
        graph.add_edge(start, end, capacity)

    return graph, num_farms, num_shops


def max_car_flow(filename: str) -> int:
    farms, shops, roads = read_roads(filename)
    graph, num_farms, num_shops = build_graph(farms, shops, roads)
    source = "source"
    sink = "sink"
    for farm in farms:
        graph.add_edge(source, farm, float("inf"))
    for shop in shops:
        graph.add_edge(shop, sink, float("inf"))
    max_flow = graph.ford_fulkerson(source, sink)
    return max_flow


filename = os.path.join(os.path.dirname(__file__), 'roads.csv')
max_flow = max_car_flow(filename)
print("Max car flow:", max_flow)
