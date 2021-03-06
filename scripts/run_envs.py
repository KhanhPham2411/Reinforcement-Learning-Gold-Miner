import gym
import numpy as np
from MinerGymEnv import MinerGymEnv


MAP_MAX_X = 21
MAP_MAX_Y = 9
mapID = np.random.randint(1, 6) #Choosing a map ID from 5 maps in Maps folder randomly
posID_x = np.random.randint(MAP_MAX_X) #Choosing a initial position of the DQN agent on X-axes randomly
posID_y = np.random.randint(MAP_MAX_Y)
request = ("map" + str(mapID) + "," + str(posID_x) + "," + str(posID_y) + ",50,100")

env = MinerGymEnv(HOST=None,PORT=None)
env.send_map_info(request)
env.reset()
for _ in range(1000):
    ob, reward, terminate,note = env.step(env.action_space.sample())
    if terminate:
        env.reset()

    env.render()
env.close()