class Twitter:

    def __init__(self):
        self.time=0
        self.followun=defaultdict(set)
        self.neew=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.neew[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed=self.neew[userId][:]
        for x in self.followun[userId]:
            feed.extend(self.neew[x])
        feed.sort(key=lambda x:-x[0])
        return [x for _,x in feed[:10]]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followun[followerId].add(followeeId)

        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followun[followerId].discard(followeeId)
        
