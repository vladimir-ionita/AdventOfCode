from utilities import FileUtilities


class Node:
    def __init__(self):
        self.children = []
        self.data = []

    def add_child(self, obj):
        self.children.append(obj)

    def value(self):
        value = 0
        if len(self.children) == 0:
            return sum(self.data)
        else:
            for i in self.data:
                index = i - 1
                if index < 0:
                    continue
                if index > len(self.children) - 1:
                    continue
                value += self.children[index].value()
        return value

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


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)
S = S[0].split()
S = list(map(int, S))

root, _ = build_subtree(S)
print(root.value())
