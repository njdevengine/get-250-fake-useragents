#short script gets you 250 fake useragents from the user-agents package
from fake_useragent import UserAgent
ua = UserAgent()
agents = []
for i in range(0,20000):
    x = ua.random
    agents.append(x)
fake_agents = list(set(agents))
