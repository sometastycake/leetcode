# https://leetcode.com/problems/design-twitter

from collections import defaultdict
from typing import List


class Node:

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class ListType:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}  # Nodes by values
        self.values = set()

    def add(self, value: int) -> None:
        node = Node(value)
        self.values.add(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.nodes[value] = node

    def remove(self, value: int) -> None:
        if value not in self.nodes:
            return
        node = self.nodes[value]
        self.values.discard(value)
        if node is self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif node is self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        del self.nodes[value]


class Twitter:

    def __init__(self):
        self.followers = defaultdict(ListType)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        followers = self.followers[userId].values
        for i in range(len(self.tweets) - 1, -1, -1):
            user, tweet = self.tweets[i]
            if user == userId or user in followers:
                tweets.append(tweet)
            if len(tweets) == 10:
                break
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].remove(followeeId)
