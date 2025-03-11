class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split('/')
        stack = []
        for folder in folders:
            if folder == '.' or folder == '':
                continue
            if folder == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(folder)
        
        return '/' + '/'.join(stack)
