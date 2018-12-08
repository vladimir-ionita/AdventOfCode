from utilities import FileUtilities


class Node:
    def __init__(self):
        self.children = []
        self.data = []

    def add_child(self, obj):
        self.children.append(obj)

    def __repr__(self):
        return "{} {}".format(len(self.children), len(self.data))


def build_subtree(data):
    child_numbers = data.pop(0)
    metadata_entries = data.pop(0)

    node = Node()
    for _ in range(child_numbers):
        child, data = build_subtree(data)
        node.add_child(child)

    node.data = data[:metadata_entries]
    data = data[metadata_entries:]

    return node, data


def get_sum(node):
    m_sum = sum(node.data)
    for c in node.children:
        m_sum += get_sum(c)
    return m_sum


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)
S = S[0].split()
S = list(map(int, S))

root, _ = build_subtree(S)
print(get_sum(root))
