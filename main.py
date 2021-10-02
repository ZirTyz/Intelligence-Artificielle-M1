import agent
import view
import House
from Thread import myThread

# speed max = 1/60 (à cause du taux de rafraichissement)
# default = 1
speed = 1/2

# size max = 20 (à cause de l'offset dans l'affichage non dynamique)
# default = 5
size = 5

house = House.House(speed, size)
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

