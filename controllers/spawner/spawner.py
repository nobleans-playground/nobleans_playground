#!/usr/bin/env python3
"""spawner controller."""

# General idea here is to expose a ROS2 service that can spawn robots using the supervisor
from controller import Supervisor

# create the Supervisor instance.
supervisor = Supervisor()

# get the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

    print("Something")

# Enter here exit cleanup code.
print("Exit")
