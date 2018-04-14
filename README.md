# Swarm-Simulation
This is my attempt at simulating a swarm algorithm to map an environment.

## Progress
For now the robots start off moving linearly and then make random turns at intervals. I am also still working on the obstacle avoidance and communication part of the swarm system.

![myfile 2](https://user-images.githubusercontent.com/15849927/38327454-e2be3c36-3865-11e8-999c-105b8c07c62e.gif)


## Usage

- Clone repository to your catkin workspace
```
git clone https://github.com/MrGrayCode/Swarm-Simulation.git
```

- Source workspace
```
source ~/catkin_ws/devel/setup.bash
```

- Launch environment
```
roslaunch launch/environment.launch
```

- Run simulation script
```
python scripts/sim.py
```

