import numpy as np

class Node:
    def __init__(self, point, left=None, right=None, parent=None):
        self.point = point
        self.left = left
        self.right = right
        self.parent = parent
def build_unbalanced_kd_tree(points, depth=0, parent=None):
    if len(points) == 0:
        return None

    if depth == 0 and parent is None:
        root = Node(point=points[0])
    else:
        root = Node(point=points[0], parent=parent)

    k = len(points[0])
    axis = depth % k

    left_points = [p for p in points[1:] if p[axis] < root.point[axis]]
    right_points = [p for p in points[1:] if p[axis] >= root.point[axis]]

    root.left = build_unbalanced_kd_tree(left_points, depth + 1, root)
    root.right = build_unbalanced_kd_tree(right_points, depth + 1, root)

    return root


def build_balanced_kd_tree(points, depth=0, parent=None):
    if len(points) == 0:
        return None

    k = len(points[0])
    axis = depth % k

    points_sorted = sorted(points, key=lambda x: x[axis])
    median_index = len(points_sorted) // 2

    if len(points_sorted) % 2 == 0:
        median_index -= 1

    median_point = points_sorted[median_index]

    if parent is None:
        root = Node(point=median_point)
    else:
        root = Node(point=median_point, parent=parent)

    root.left = build_balanced_kd_tree(points_sorted[:median_index], depth + 1, root)
    root.right = build_balanced_kd_tree(points_sorted[median_index + 1:], depth + 1, root)

    return root



def print_tree(node):
    if node is None:
        return

    if node.parent:
        print(f"Parent: {node.parent.point}, Point: {node.point}, Left: {node.left.point if node.left else None}, Right: {node.right.point if node.right else None}")
    else:
        print(f"Root: {node.point}, Left: {node.left.point if node.left else None}, Right: {node.right.point if node.right else None}")

    print_tree(node.left)
    print_tree(node.right)

def main():
    dimensionality = int(input("Enter the dimensionality of the points (2 or 3): "))
    if dimensionality not in [2, 3]:
        print("Invalid dimensionality.")
        return

    print("Select KD tree type:")
    print("1. Unbalanced KD Tree")
    print("2. Balanced KD Tree")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if dimensionality == 2:
            points = np.array([[6,2], [7,1], [2,9], [3,6], [4,8], [8,4], [5,3], [1,5], [9,5]])
        else:
            points = np.array([[6,2,9], [7,1,2], [2,9,6],[3,6,1], [4,8,5], [8,4,4], [5,3,7], [1,5,1], [9,5,4]])
        print("Unbalanced KD Tree:")
        kd_tree = build_unbalanced_kd_tree(points)
        print_tree(kd_tree)
    elif choice == 2:
        if dimensionality == 2:
            points = np.array([[6,2], [7,1], [2,9], [3,6], [4,8], [8,4], [5,3], [1,5], [9,5]])
        else:
            points = np.array([[6,2,9], [7,1,2], [2,9,6],[3,6,1], [4,8,5], [8,4,4], [5,3,7], [1,5,1], [9,5,4]])
        print("Balanced KD Tree:")
        kd_tree = build_balanced_kd_tree(points)
        print_tree(kd_tree)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
