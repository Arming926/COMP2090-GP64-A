print("still thinking")
class Group:
    """Group class to store group information and members"""
    def __init__(self, group_id, max_size=5):
        self.group_id = group_id
        self.members = []
        self.max_size = max_size

    def get_member_count(self):
        return len(self.members)

    def is_full(self):
        return self.get_member_count() >= self.max_size

    def add_member(self, student_name):
        if not self.is_full():
            self.members.append(student_name)
            return True
        return False

class MaxHeap:
    """Max-Heap implementation based on the number of group members"""
    def __init__(self):
        self.heap = []

    def insert(self, group):
        """Insert a group into the heap"""
        self.heap.append(group)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """Adjust heap structure from bottom to top"""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].get_member_count() > self.heap[parent_index].get_member_count():
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def extract_max(self):
        """Remove and return the group with the most members (root node)"""
        if len(self.heap) == 0:
            return None
        max_group = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self._heapify_down(0)
        return max_group

    def _heapify_down(self, index):
        """Adjust heap structure from top to bottom"""
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.heap[left_child].get_member_count() > self.heap[largest].get_member_count():
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child].get_member_count() > self.heap[largest].get_member_count():
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

def heap_sort_groups(groups):
    """
    Heap Sort Algorithm
    Sort groups by member count from LOWEST to HIGHEST
    Return sorted group list
    """
    heap = MaxHeap()
    for group in groups:
        heap.insert(group)

    sorted_list = []
    while len(heap.heap) > 0:
        sorted_list.append(heap.extract_max())

    # Reverse to get: fewest members → most members
    sorted_list.reverse()
    return sorted_list

if __name__ == "__main__":
    print("=== COMP2090SEF Task 2 (Part B) - Heap + Heap Sort Auto Grouping System ===")

    # Create 4 groups, max 5 members per group
    g1 = Group("Group-001", max_size=5)
    g2 = Group("Group-002", max_size=5)
    g3 = Group("Group-003", max_size=5)
    g4 = Group("Group-004", max_size=5)

    # Add existing members
    g1.add_member("Student A")
    g1.add_member("Student B")
    g2.add_member("Student C")
    g3.add_member("Student D")
    g3.add_member("Student E")
    g3.add_member("Student F")

    # Group list
    all_groups = [g1, g2, g3, g4]

    # Sort groups by Heap Sort
    sorted_groups = heap_sort_groups(all_groups)

    print("\n=== Sort Result (Fewest Members First) ===")
    for group in sorted_groups:
        print(f"{group.group_id} | Members: {group.get_member_count()}")

    print("\n=== Auto Grouping Demonstration ===")
    new_students = ["NewStudent1", "NewStudent2", "NewStudent3", "NewStudent4"]

    for student in new_students:
        target_group = sorted_groups[0]
        if target_group.add_member(student):
            print(f"{student} → joined {target_group.group_id}")
        # Re-sort after assignment
        sorted_groups = heap_sort_groups(all_groups)

    print("\n=== Final Group Member Count ===")
    for group in all_groups:
        print(f"{group.group_id}: {group.get_member_count()} members")
