class Node:
    """Node in the doubly linked list. Represents a specific frequency."""
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()  # Set of keys with this frequency
        self.next = None   # Pointer to the node with the next higher frequency
        self.prev = None   # Pointer to the node with the next lower frequency

class AllOne:

    def __init__(self):
        """Initializes the data structure."""
        self.root = Node(0)  # Sentinel node with frequency 0
        self.root.next = self.root # Point to itself initially (empty list)
        self.root.prev = self.root # Point to itself initially
        self.key_to_node = {} # Maps key (string) -> Node

    def _remove_node(self, node: Node):
        node.next.prev, node.prev.next = node.prev, node.next

    def _insert_after(self, node: Node, new_node: Node):
        node.next.prev, node.next, new_node.next, new_node.prev = new_node, new_node, node.next, node

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            target_freq = 1
            # Check if a node with frequency 1 already exists (must be after root)
            if self.root.next.freq == 1:
                target_node = self.root.next
            else:
                # Create a new node for frequency 1 and insert it after root
                target_node = Node(target_freq)
                self._insert_after(self.root, target_node)

            # Add key to the target node and update map
            target_node.keys.add(key)
            self.key_to_node[key] = target_node

        else:
            current_node = self.key_to_node[key]
            current_freq = current_node.freq
            target_freq = current_freq + 1

            # Remove key from current node's set
            current_node.keys.remove(key)

            # Determine the target node for the incremented frequency
            # Check if the next node has the correct frequency
            if current_node.next.freq == target_freq:
                target_node = current_node.next
            else:
                # Create a new node and insert it after the current node
                target_node = Node(target_freq)
                self._insert_after(current_node, target_node)

            # Add key to the target node and update map
            target_node.keys.add(key)
            self.key_to_node[key] = target_node

            # If the current node became empty, remove it
            if len(current_node.keys) == 0:
                self._remove_node(current_node)


    def dec(self, key: str) -> None:
        if key not in self.key_to_node:
             return

        current_node = self.key_to_node[key]
        current_freq = current_node.freq

        # Remove key from current node's set
        current_node.keys.remove(key)

        if current_freq == 1:
            # Key's count becomes 0, remove it from the map
            del self.key_to_node[key]
        else:
            # Key's count decreases, move it to the node with frequency - 1
            target_freq = current_freq - 1

            # Determine the target node for the decremented frequency
            # Check if the previous node has the correct frequency
            if current_node.prev.freq == target_freq:
                target_node = current_node.prev
            else:
                # Create a new node and insert it before the current node
                target_node = Node(target_freq)
                self._insert_after(current_node.prev, target_node)

            # Add key to the target node and update map
            target_node.keys.add(key)
            self.key_to_node[key] = target_node

        # If the current node became empty, remove it
        if not current_node.keys:
            self._remove_node(current_node)


    def getMaxKey(self) -> str:
        max_node = self.root.prev
        if max_node == self.root:
            return ""
        return next(iter(max_node.keys))


    def getMinKey(self) -> str:
        min_node = self.root.next
        if min_node == self.root:
            return ""
        return next(iter(min_node.keys))
