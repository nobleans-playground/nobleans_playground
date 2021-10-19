#!/usr/bin/env python3
"""spawner controller."""

from controller import Supervisor


# create the Supervisor instance.
supervisor = Supervisor()

rootNode = supervisor.getRoot();
childrenField = rootNode.getField('children')
childrenField.importMFNodeFromString(-1, 'Robot { children [ Shape { geometry Sphere { radius 100 } } ] }')

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
    print("Something")

# Enter here exit cleanup code.
print("Exit")
