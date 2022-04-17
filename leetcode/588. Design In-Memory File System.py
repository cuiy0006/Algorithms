from enum import Enum

class FileSystemType(Enum):
    FILE = 0
    DIR = 1

class FileSystemObject:
    def __init__(self, t: FileSystemType, name: str):
        self.type = t
        self.name = name
        
class FileObject(FileSystemObject):
    def __init__(self, name: str, content: str):
        FileSystemObject.__init__(self, FileSystemType.FILE, name)
        self.content = content

class DirObject(FileSystemObject):
    def __init__(self, name: str):
        FileSystemObject.__init__(self, FileSystemType.DIR, name)
        self.subdir = {}


class FileSystem:

    def __init__(self):
        self.root_dir = DirObject('/')

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(self.root_dir.subdir.keys())

        path_lst = path[1:].split('/')
        curr = self.root_dir
        for p in path_lst:
            curr = curr.subdir[p]
        
        if curr.type == FileSystemType.FILE:
            return [curr.name]
        else:
            return sorted(curr.subdir.keys())


    def mkdir(self, path: str) -> None:
        if path == '/':
            return
        path_lst = path[1:].split('/')
        curr = self.root_dir
        for p in path_lst:
            if p not in curr.subdir:
                curr.subdir[p] = DirObject(p)
            curr = curr.subdir[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_lst = filePath[1:].split('/')
        curr = self.root_dir
        for p in path_lst[:-1]:
            curr = curr.subdir[p]
        filename = path_lst[-1]
        if filename not in curr.subdir:
            curr.subdir[filename] = FileObject(filename, content)
        else:
            curr.subdir[filename].content += content


    def readContentFromFile(self, filePath: str) -> str:
        path_lst = filePath[1:].split('/')
        curr = self.root_dir
        for p in path_lst[:-1]:
            curr = curr.subdir[p]
        filename = path_lst[-1]
        return curr.subdir[filename].content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
