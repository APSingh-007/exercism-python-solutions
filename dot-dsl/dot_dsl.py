from dataclasses import dataclass

NODE, EDGE, ATTR = ("Node", "Edge", "Attribute")


@dataclass
class Node:
    name: str
    attrs: dict


@dataclass
class Edge:
    src: str
    dst: str
    attrs: dict


def check_types(name: str, values: tuple, types: tuple) -> None:
    message = f"{name} is malformed"

    if len(values) != len(types):
        raise ValueError(message)
    for item, type in zip(values, types):
        if not isinstance(item, type):
            raise ValueError(message)


class Graph:
    def __init__(self, data=None) -> None:
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.attrs: dict[str:str] = {}

        if data is None:
            data = []
        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

        for entry in data:
            if not isinstance(entry, tuple):
                raise TypeError("Graph data malformed")
            if len(entry) < 3:
                raise TypeError("Graph item incomplete")
            self.fill_entry(entry)

    def fill_entry(self, entry: tuple) -> None:
        type_of_entry, *values = entry

        if type_of_entry == NODE:
            check_types(NODE, values, (str, dict))
            name, attrs = values
            self.nodes.append(Node(name=name, attrs=attrs))

        elif type_of_entry == EDGE:
            check_types(EDGE, values, (str, str, dict))
            src, dst, attrs = values
            self.edges.append(Edge(src=src, dst=dst, attrs=attrs))

        elif type_of_entry == ATTR:
            check_types(ATTR, values, (str, str))
            key, value = values
            self.attrs[key] = value

        else:
            raise ValueError("Unknown item")
