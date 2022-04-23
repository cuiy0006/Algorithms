
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # 1: play1; -1: play2
        
        def can_win(player, left, right, score1, score2):
            if left == right:
                if player == 1:
                    score1 += nums[left]
                    if score1 >= score2:
                        return True
                    else:
                        return False
                else:
                    score2 += nums[left]
                    if score1 >= score2:
                        return False
                    else:
                        return True

            if player == 1:
                if not can_win(-player, left+1, right, score1+nums[left], score2) or \
                    not can_win(-player, left, right-1, score1+nums[right], score2):
                    return True
            else:
                if not can_win(-player, left+1, right, score1, score2+nums[left]) or \
                    not can_win(-player, left, right-1, score1, score2+nums[right]):
                    return True 
            return False
        
        return can_win(1, 0, len(nums)-1, 0, 0)
