# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pickle



class Auth:

    name = "data.bin"

    def __init__(self):
        self.telegram                   = None
        self.twitterAPIKey              = None
        self.twitterAPISecretKey        = None
        self.twitterAccessToken         = None
        self.twitterAccessTokenSecret   = None
        self.twitterFollows             = []
        self.telegramUsers              = []

    def save(self):
        fh = open(self.name, 'wb')
        pickle.dump(self.__dict__, fh)
        fh.close()

    def reprocess(self):
        self.telegram                   = input("telegramKey: ")
        self.twitterAPIKey              = input("Twitter API Key: ")
        self.twitterAPISecretKey        = input("Twitter secret API key: ")
        self.twitterAccessToken         = input("Twitter access token: ")
        self.twitterAccessTokenSecret   = input("Twitter access token secret: ")
        self.save()

    def process(self):
        try:
            fh = open(self.name, 'rb')
            auth = pickle.load(fh)
            fh.close()
            self.__dict__.update(auth)

        except Exception:
            self.reprocess()

    # Returns true if inserted, false if already exists
    def addFollow(self, user):
        try:
            self.twitterFollows.index(user)
            return False
        except ValueError:
            self.twitterFollows.append(user)
            self.save()
            return True

    def deleteFollow(self, user):
        try:
            self.twitterFollows.remove(user)
            self.save()
            return True
        except ValueError:
            return False

    def addTelegramUser(self, user):
        try:
            self.telegramUsers.index(user)
            return False
        except ValueError:
            self.telegramUsers.append(user)
            self.save()
            return True

    def deleteTelegramUser(self, user):
        try:
            self.telegramUsers.remove(user)
            self.save()
            return True
        except ValueError:
            return False


