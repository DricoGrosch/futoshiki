
from src.agent import Agent
from src.environment import Environment

env = Environment(random_start=False)
env.print_matrix()
agent=Agent(env)
agent.build_winning_track()



