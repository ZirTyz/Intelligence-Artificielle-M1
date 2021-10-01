import agent
import view
import House
from Thread import myThread


speed = 0.5
house = House.House(speed)
agent = agent.Agent(house, speed)
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

# agent.live()


# _thread.start_new_thread(
