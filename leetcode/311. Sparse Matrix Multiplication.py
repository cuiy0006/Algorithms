class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        row_dic = {}
        col_dic = {}
        
        for i in range(len(mat1)):
            row_dic[i] = set()
            for j in range(len(mat1[0])):
                if mat1[i][j] != 0:
                    row_dic[i].add(j)
        
        for j in range(len(mat2[0])):
            col_dic[j] = set()
            for i in range(len(mat2)):
                if mat2[i][j] != 0:
                    col_dic[j].add(i)
        
        res = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in row_dic[i] & col_dic[j]:
                    res[i][j] += mat1[i][k] * mat2[k][j]
        
        return res
