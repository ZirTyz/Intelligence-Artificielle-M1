import threading

class myThread(threading.Thread):
    def __init__(self, threadID, name, _function):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.function = _function

    def run(self):
        print("Starting " + self.name)
        self.function()
        print("Exiting " + self.name)