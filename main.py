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

thread1.start()
thread2.start()

view.refresh()
house.alive = False
agent.alive = False

thread1.join()
thread2.join()

