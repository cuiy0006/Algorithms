from heapq import heappop
from heapq import heappush
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.tweets = {}
        self.cnt = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.cnt, tweetId))
        self.cnt += 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        tmp = []
        lst = set()
        if userId in self.dic:
            lst = self.dic[userId]
        lst.add(userId)
        
        for uid in lst:
            if uid in self.tweets:
                for msg in self.tweets[uid]:
                    heappush(tmp, msg)
                    if len(tmp) == 11:
                        heappop(tmp)
            
        while len(tmp) != 0:
            res.append(heappop(tmp)[1])
        res.reverse()
        
        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.dic:
            self.dic[followerId] = set()
        self.dic[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.dic:
            return
        else:
            if followeeId in self.dic[followerId]:
                self.dic[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
