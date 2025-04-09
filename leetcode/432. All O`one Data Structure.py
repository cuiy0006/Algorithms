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
        """Helper to remove a node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        # Optional: Clear pointers of removed node
        # node.next = node.prev = None

    def _insert_after(self, node: Node, new_node: Node):
        """Helper to insert new_node right after node."""
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def inc(self, key: str) -> None:
        """Increments the count of key by 1."""
        if key not in self.key_to_node:
            # === New Key ===
            # Default frequency is 1
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
            # === Existing Key ===
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
            if not current_node.keys:
                self._remove_node(current_node)


    def dec(self, key: str) -> None:
        """Decrements the count of key by 1."""
        if key not in self.key_to_node: # Should not happen based on problem statement, but good practice
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
                # (which is equivalent to inserting after current_node.prev)
                target_node = Node(target_freq)
                self._insert_after(current_node.prev, target_node)

            # Add key to the target node and update map
            target_node.keys.add(key)
            self.key_to_node[key] = target_node

        # If the current node became empty (and it's not the sentinel), remove it
        if not current_node.keys and current_node != self.root:
            self._remove_node(current_node)


    def getMaxKey(self) -> str:
        """Returns one key with the maximal count."""
        # Max frequency node is always before the root sentinel
        max_node = self.root.prev
        if max_node == self.root: # List is empty
            return ""
        # Return any key from the set
        return next(iter(max_node.keys))


    def getMinKey(self) -> str:
        """Returns one key with the minimum count."""
        # Min frequency node is always after the root sentinel
        min_node = self.root.next
        if min_node == self.root: # List is empty
            return ""
        # Return any key from the set
        return next(iter(min_node.keys))
