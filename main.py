import _thread

import agent
import view
import House

house = House.House()
agent = agent.Agent(house)
view = view.View()

_thread.start_new_thread(agent.live())
_thread.start_new_thread(agent.live())
_thread.start_new_thread(view.refresh())
