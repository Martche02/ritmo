class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {"0": None, "1": None, "2": None}

class TernaryTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, sequence):
        current_node = self.root
        for char in sequence:
            if current_node.children[char] is None:
                current_node.children[char] = TreeNode(char)
            current_node = current_node.children[char]
        current_node.value = sequence

    def search(self, sequence):
        current_node = self.root
        for char in sequence:
            if current_node.children[char] is None:
                return False
            current_node = current_node.children[char]
        return current_node.value == sequence
def ts(sequence, transformation_type):
    """Transforma uma sequência de acordo com o tipo de transformação especificado."""
    if transformation_type == 1:
        # Troca 0 por 1, e 1 por 2
        return sequence.replace("0", "X").replace("1", "0").replace("X", "1")
    elif transformation_type == 2:
        # Troca 0 por 2, e 2 por 0
        return sequence.replace("0", "X").replace("2", "0").replace("X", "2")
    else:
        return sequence