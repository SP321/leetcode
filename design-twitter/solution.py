class Twitter:

    def __init__(self):
        self.tweets=defaultdict(deque)
        self.followed_users=defaultdict(set)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        if len(self.tweets[userId])>10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets=self.tweets[userId]
        for i in self.followed_users[userId]:
            tweets=heapq.merge(tweets,self.tweets[i])
            tweets=heapq.nlargest(10,tweets)
        return [i[1] for i in sorted(tweets,reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed_users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed_users[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)