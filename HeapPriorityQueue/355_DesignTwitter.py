class Twitter:
    def __init__(self):
        self.user_info = {}   
        self.time = 0     

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.user_info:
            self.user_info[userId] = {'tweets':[], 'followees':set()}
        heapq.heappush(self.user_info[userId]['tweets'], [self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_info:
            return []
        tweets = []
        # get tweets of each of its followees
        for followee in list(self.user_info[userId]['followees']):
            if followee in self.user_info:
                tweets += self.user_info[followee]['tweets']
        # add tweets of the user
        tweets += self.user_info[userId]['tweets']
        # heapify
        heapq.heapify(tweets)
        # get top 10
        return [tweet for time, tweet in heapq.nlargest(10, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_info:
            self.user_info[followerId] = {'tweets':[], 'followees': set()}
        self.user_info[followerId]['followees'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_info and followeeId in self.user_info[followerId]['followees']:
            self.user_info[followerId]['followees'].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
