class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.tweet = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if not self.d.get(userId):
            self.d[userId] = []
        self.tweet.append([userId, tweetId])
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if not self.d.get(userId):
            f = []
        else:
            f = self.d[userId]
        res = []
        for u,t in self.tweet[::-1]:
            if u == userId or u in f:
                res.append(t)
                if len(res) == 10:
                    break
        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if not self.d.get(followerId):
            self.d[followerId] = []
        self.d[followerId] += [followeeId]
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if not self.d.get(followerId):
            return
        if followeeId not in self.d[followerId]:
            return 
        self.d[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
