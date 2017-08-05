class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for path in paths:
            p, file = path.split(' ', 1)
            fileNamelst = file.split(' ')
            for fileName in fileNamelst:
                name, content = fileName.split('(')
                if content in dic:
                    dic[content].append(p + '/' + name)
                else:
                    dic[content] = [p + '/' + name]
        res = []
        for val in dic.values():
            if len(val) > 1:
                res.append(val)
        return res                    
