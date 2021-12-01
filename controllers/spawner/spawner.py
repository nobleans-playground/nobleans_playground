#!/usr/bin/env python3
"""spawner controller."""

from controller import Supervisor
from nobleans_playground.srv import SpawnProto

import rclpy
from rclpy.node import Node


class WebotsSpawner(Node):

    def __init__(self, supervisor):
        super().__init__('webots_spawner')

        # create the Supervisor instance.
        self.supervisor = supervisor

        self.srv = self.create_service(SpawnProto, 'spawn_proto', self.spawn_proto)

    def set_supervisor(self, supervisor):
        self.supervisor = supervisor

    def spawn_proto(self, request, response):
        root_node = self.supervisor.getRoot()
        children_field = root_node.getField('children')
        children_field.importMFNodeFromString(-1, request.proto)
        self.get_logger().debug(request.proto)

        response.success = True
        return response


if __name__ == '__main__':
    rclpy.init()
    supervisor = Supervisor()
    webots_spawner = WebotsSpawner(supervisor)
    timestep = int(supervisor.getBasicTimeStep())
    while supervisor.step(timestep) != -1:
        rclpy.spin_once(webots_spawner)
    rclpy.shutdown()
