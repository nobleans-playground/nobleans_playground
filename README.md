# nobleans_playground
Holds a playground for webots for all the robleos to play in :)

## Launching the playground
```
ros2 launch nobleans_playground simulation.launch.py
```

## Spawning your own robot
To spawn your own robot, call the [SpawnProto](srv/SpawnProto.srv) service.

Example to spawn a sphere:
```
ros2 service call /spawn_proto nobleans_playground/srv/SpawnProto "{proto: 'Robot { children [ Shape { geometry Sphere { radius 100 } } ] }'}"
```
