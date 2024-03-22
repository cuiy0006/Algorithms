class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.post_map = defaultdict(list)
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_map[userId].append((self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        self.follow_map[userId].add(userId)
        for followee in self.follow_map[userId]:
            for i in range(len(self.post_map[followee])-1, -1, -1):
                ts, post = self.post_map[followee][i]
                if len(h) < 10:
                    heappush(h, (ts, post))
                else:
                    if ts < h[0][0]:
                        break
                    else:
                        heappop(h)
                        heappush(h, (ts, post))
        res = []
        while len(h) != 0:
            res.append(heappop(h)[1])
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_map[followerId]:
            return
        self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)