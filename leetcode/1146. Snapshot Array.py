class SnapshotArray:

    def __init__(self, length: int):
        self.id_to_changes = {} # {id: {idx: value}}
        self.array = [0 for _ in range(length)]
        self.curr_idx = 0

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        if self.curr_idx not in self.id_to_changes:
            self.id_to_changes[self.curr_idx] = {}
        changes = self.id_to_changes[self.curr_idx]
        changes[index] = val


    def snap(self) -> int:
        snap_id = self.curr_idx
        self.curr_idx += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        id = snap_id
        while id >= 0 and (id not in self.id_to_changes or index not in self.id_to_changes[id]):
            id -= 1

        if id < 0:
            return 0
        
        return self.id_to_changes[id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
