class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records: list[Record]) -> Node|None:
    records.sort(key=lambda x: x.record_id)

    trees: list[Node] = []
    for i, rec in enumerate(records):
        if i != rec.record_id:
            raise ValueError("Record id is invalid or out of order.")
        if rec.record_id < rec.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        if rec.record_id == rec.parent_id != 0:
            raise ValueError("Only root should have equal record and parent id.")

        trees.append(Node(rec.record_id))
        if rec.record_id != rec.parent_id:
            trees[rec.parent_id].children.append(trees[rec.record_id])

    return trees[0] if trees else None
