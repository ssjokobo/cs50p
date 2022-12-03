class Jar:
    def __init__(self, capacity=12):
        # check max
        if capacity >= 0:
            self.cap = capacity
            self.in_jar = 0
        else:
            raise ValueError

    def __str__(self):
        # empty string
        cookies_in_jar = ""
        # filling cookie emojis
        for _ in range(self.in_jar):
            cookies_in_jar += "🍪"
        return cookies_in_jar

    def deposit(self, n):
        # check capacity
        if self.in_jar + n <= self.cap:
            self.in_jar += n
        else:
            raise ValueError

    def withdraw(self, n):
        # check not empty
        if self.in_jar - n >= 0:
            self.in_jar -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.in_jar