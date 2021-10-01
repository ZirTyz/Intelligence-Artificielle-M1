import threading

import agent
import view
import House

class myThread(threading.Thread):
   def __init__(self, threadID, name, _function):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.function = _function
   def run(self):
      print ("Starting " + self.name)
      self.function()
      print ("Exiting " + self.name)

house = House.House()
agent = agent.Agent(house)
view = view.View(house)

thread1 = myThread(1, "Thread House", house.live)
thread2 = myThread(2, "Thread Agent", agent.live)
thread3 = myThread(3, "Thread View", view.refresh)


thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.start()

#agent.live()


# _thread.start_new_thread(

