


class Obserable():
    def __init__(self):
        self.readers = []

    def register(self, reader):
        self.readers.append(reader)

    def unregister(self, reader):
        self.readers
        
    def inform():
        pass


class Observer():
    def __init__(self):

    def subscribe(self, news):
  
    def unsubscribe(self, ):
    
    def update(self, ):
        pass

class News():
    def __init__(self):
        pass

class Reader():
    def __init__(self):
        self.name = None
        self.news = None

    def reader(self, name):
        self.name = name

    def subscribe(self, news):
        self.news = news
        news.register(self)

    def unsubscribe(self, news):
        self.news = news
        news.unregister(self)

    def update(self):
        self.read()

    def read(self):
        if self.news.isLastNews():
            print(self.name + ' read latest news')
        else:
            print(self.name + ' read old news')
