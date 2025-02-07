class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data: list) -> None:
        self.root = None

        for data in tree_data:
            self.insert(data)

    def insert(self, data: str) -> None:
        newnode = TreeNode(data)

        if self.root is None:
            self.root = newnode
            return

        current = self.root
        while current is not None:
            if data <= current.data:
                if current.left is None:
                    current.left = newnode
                    break
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = newnode
                    break
                current = current.right

    def data(self) -> TreeNode:
        return self.root

    def sorted_data(self, reverse=False) -> list[str]:
        sorted_bst = self.inorder_traversal()
        return sorted_bst[::-1] if reverse else sorted_bst

    def inorder_traversal(self):
        stack: list[TreeNode] = []
        current = self.root
        answer: list[str] = []

        while stack or current:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            answer.append(current.data)

            current = current.right

        return answer
