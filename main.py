import _thread

import agent
import view

agent = agent.Agent()
view = view.View()

_thread.start_new_thread(agent.live())
_thread.start_new_thread(view.refresh())
