from __future__ import print_function


class Node:

    def __init__(self, name):
        self.name = name
        self.next_nodes = []

    def __hash__(self):
        return self.name

    def __eq__(self, other_node):
        return self.name == hash(other_node)

    def __str__(self):
        return f"{self.name}: {[str(node) for node in self.next_nodes]}"

    def __repr__(self):
        return f"V{self.name}"
