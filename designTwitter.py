class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.user_tweets = defaultdict(deque)
        self.post = 0

    def postTweet(self, userId, tweetId):
        self.post += 1
        tweets = self.user_tweets[userId]
        tweets.append(((self.post), tweetId))
        if len(tweets) > 10:
            tweets.popleft()
        

    def getNewsFeed(self, userId):
        h = []
        u = self.user_tweets[userId]
        h.extend(u)
        heapify(h)
        for user in self.following[userId]:
            tweets = self.user_tweets[user]
            for x in range(len(tweets) - 1, -1, -1):
                if len(h) < 10:
                    heappush(h, tweets[x])
                else:
                    if h[0][0] < tweets[x][0]:
                        heappushpop(h, tweets[x])
                    else:
                        break
        return [heappop(h)[1] for x in range(len(h))][::-1]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId != followeeId:
                self.following[followerId].discard(followeeId)