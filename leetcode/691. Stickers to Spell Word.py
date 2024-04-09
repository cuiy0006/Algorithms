class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers_dics = []
        for sticker in stickers:
            sticker_dic = defaultdict(int)
            for c in sticker:
                sticker_dic[c] += 1
            stickers_dics.append(sticker_dic)

        res = sys.maxsize
        dp = {}
        def helper(idx, target):
            if target == '':
                return 0
            if (idx, target) in dp:
                return dp[(idx, target)]
            if idx >= len(stickers):
                return sys.maxsize

            sticker_dic = stickers_dics[idx].copy()
            target_lst = list(target)
            for i, c in enumerate(target_lst):
                if c in sticker_dic:
                    sticker_dic[c] -= 1
                    if sticker_dic[c] == 0:
                        del sticker_dic[c]
                    target_lst[i] = ''

            new_target = ''.join(target_lst)
            res = helper(idx+1, target)
            if new_target != target:
                res = min(res, helper(idx, new_target) + 1)
            dp[(idx, target)] = res
            return res

        res = helper(0, target)
        if res == sys.maxsize:
            return -1
        return res

