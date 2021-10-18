import os
import pathlib
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch import LaunchDescription
from launch_ros.actions import Node
import launch
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher


def generate_launch_description():
    simulation_dir = get_package_share_directory('nobleans_playground')
    world = LaunchConfiguration('world')

    webots = WebotsLauncher(
        world=PathJoinSubstitution([simulation_dir, 'worlds', world])
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='nieuwe_erven.wbt',
            description='World file to be launched'
        ),
        webots,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
