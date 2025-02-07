from typing import Optional

TreeType = Optional[dict[str, "TreeType"]]
ZipNode_type = Optional["ZipNode"]


class ZipNode:
    def __init__(
        self, value: int, left: ZipNode_type, right: ZipNode_type, parent: ZipNode_type
    ) -> None:
        self.parent = parent
        self._value = value
        self.left_node: ZipNode = left
        self.right_node: ZipNode = right

    def value(self) -> int:
        return self._value

    def left(self):
        return self.left_node

    def right(self):
        return self.right_node

    def set_value(self, value: int):
        self._value = value
        return self

    def set_left(self, tree):
        self.left_node = Zipper.from_tree(tree, parent=self)
        return self

    def set_right(self, tree):
        self.right_node = Zipper.from_tree(tree, parent=self)
        return self

    def up(self):
        return self.parent

    def to_tree(self) -> dict:
        root_node = self
        while root_node.up() is not None:
            root_node = root_node.up()
        return root_node.serialize()

    def serialize(self) -> dict:
        return {
            "value": self.value(),
            "left": None if self.left_node is None else self.left_node.serialize(),
            "right": None if self.right_node is None else self.right_node.serialize(),
        }


class Zipper:
    @staticmethod
    def from_tree(tree: TreeType, parent=None) -> ZipNode:
        if tree is None:
            return None

        z_node = ZipNode(tree["value"], None, None, parent)
        z_node.left_node = Zipper.from_tree(tree["left"], z_node)
        z_node.right_node = Zipper.from_tree(tree["right"], z_node)
        return z_node
