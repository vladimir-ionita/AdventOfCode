from utilities import FileUtilities
import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def print_list(head):
    end_point = head.prev.data

    the_list = []
    while head.data != end_point:
        the_list.append(head.data)
        head = head.next

    print(the_list)
    return the_list


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)
S = S[0]

# Parse the input
words = S.split()
players_total = int(words[0])
marble_max = int(words[6])  # * 100   # (uncomment for second part)

# Setup
marble_points = 0
player = 0

# Create list head
curr_marble = Node(marble_points)
curr_marble.next = curr_marble
curr_marble.prev = curr_marble
# head = curr_marble

M = collections.defaultdict(int)
while marble_points <= marble_max:
    # print_list(head)
    player += 1
    if player > players_total:
        player = 1

    marble_points += 1
    new_marble = Node(marble_points)

    if marble_points % 23 != 0:
        new_marble.next = curr_marble.next.next
        new_marble.prev = curr_marble.next
        new_marble.next.prev = new_marble
        curr_marble.next.next = new_marble

        curr_marble = new_marble
    else:
        M[player] += marble_points
        for _ in range(7):
            curr_marble = curr_marble.prev
        M[player] += curr_marble.data

        curr_marble.prev.next = curr_marble.next
        curr_marble.next.prev = curr_marble.prev
        curr_marble = curr_marble.next

print(max(M.items(), key=lambda x: x[1]))
