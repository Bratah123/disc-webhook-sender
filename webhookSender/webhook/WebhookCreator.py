class WebhookCreator:
    def __init__(self, url, message="", avatar_url=None, username=None):
        self.url = url
        self.message = message
        if avatar_url is None:
            avatar_url = "https://media.discordapp.net/attachments/631249406775132182/728001813730689194/322c936a8c8be1b803cd94861bdfa868.png"
        self.avatar_url = avatar_url
        if username is None:
            username = "Discord" # Default Username is Discord
        self.username = username

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, url):
        self.url = url

    @property
    def message(self):
        return self.message

    @message.setter
    def message(self, message):
        self.message = message

    @property
    def avatar_url(self):
        return self.avatar_url

    @avatar_url.setter
    def avatar_url(self, url):
        self.avatar_url = url

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        self.username = username
