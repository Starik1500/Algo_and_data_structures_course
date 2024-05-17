import unittest
import os
import sys
import csv

test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(
    os.path.join(os.path.dirname(test_file_path), os.pardir)
)
src_path = os.path.join(common_parent_path, "src")
sys.path.append(src_path)
from collections import defaultdict
from typing import List, Dict, Tuple
from flowers_road import Graph, read_roads, build_graph, max_car_flow


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge("A", "B", 10)
        self.graph.add_edge("B", "C", 5)
        self.graph.add_edge("A", "C", 15)
        self.graph.add_edge("C", "D", 10)

    def test_add_edge(self):
        self.assertIn("B", self.graph.graph["A"])
        self.assertEqual(self.graph.graph["A"]["B"], 10)

    def test_dfs(self):
        visited = defaultdict(bool)
        parent = {}
        result = self.graph.dfs(self.graph.graph, "A", "D", visited, parent)
        self.assertTrue(result)
        self.assertEqual(parent["D"], "C")

    def test_Ford_Fulkerson(self):
        max_flow = self.graph.ford_fulkerson("A", "D")
        self.assertEqual(max_flow, 10)


class TestReadRoads(unittest.TestCase):
    def test_read_roads(self):
        filename = "test_roads.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["A", "B", "C"])
            writer.writerow(["D", "E", "F"])
            writer.writerow(["A", "B", "10"])
            writer.writerow(["B", "C", "5"])
            writer.writerow(["A", "C", "15"])
            writer.writerow(["C", "D", "10"])

        farms, shops, roads = read_roads(filename)
        self.assertEqual(farms, ["A", "B", "C"])
        self.assertEqual(shops, ["D", "E", "F"])
        self.assertEqual(
            roads, [("A", "B", 10), ("B", "C", 5), ("A", "C", 15), ("C", "D", 10)]
        )


class TestBuildGraph(unittest.TestCase):
    def test_build_graph(self):
        farms = ["A", "B"]
        shops = ["C", "D"]
        roads = [("A", "C", 10), ("B", "D", 5)]
        graph, num_farms, num_shops = build_graph(farms, shops, roads)
        self.assertEqual(num_farms, 2)
        self.assertEqual(num_shops, 2)
        self.assertIn("C", graph.graph["A"])
        self.assertEqual(graph.graph["A"]["C"], 10)


class TestMaxCarFlow(unittest.TestCase):
    def test_max_car_flow(self):
        filename = "test_roads.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["A", "B"])
            writer.writerow(["C", "D"])
            writer.writerow(["A", "C", "10"])
            writer.writerow(["B", "D", "5"])
            writer.writerow(["A", "D", "15"])
            writer.writerow(["C", "D", "10"])

        max_flow = max_car_flow(filename)
        self.assertEqual(max_flow, 30)


if __name__ == "__main__":
    unittest.main()
