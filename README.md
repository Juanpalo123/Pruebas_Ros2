# ROS2 Programmed Assignment

![Imagen de Cabecera](figs/turtle.png)

## Description

Based on turtlesim, ROS2 tutorials and ROS book chapters 4-9


**Work**
- Create a node for turtlesim to draw a square (hint: publish and sleep)
- Make it a service
- Make it an action (add status update)
- Add parameter(s) and demo launch 
- Push the code to a repo at https://github.com/im2ag-m1-robotics-2025/

---

### Instalation

```
git clone https://github.com/tu-usuario/nombre-del-proyecto.git
```

## Create a node for turtlesim to draw a square

```
ros2 run turtlesim turtlesim_node   
```

```
ros2 run my_py_pkg turtle_square
```

## Make it a service

```
ros2 run turtlesim turtlesim_node   
```

Execute the service
```
ros2 run turtlesim_square draw_square_service
```

Call the service
```
ros2 service call /draw_square std_srvs/srv/Trigger
```

## Make it an action

```
ros2 run turtlesim turtlesim_node   
```

Execute the action
```
ros2 run turtlesim_square draw_square_action
```

Application of the action
```
ros2 action send_goal /draw_square example_interfaces/action/Fibonacci "{}"
```

## Add parameter(s)

```
ros2 run turtlesim turtlesim_node   
```

Execute the action with the parameters
```
ros2 run turtlesim_square turtle_square_with_params --ros-args -p linear_speed:=0.5 -p angular_speed:=1.57
```

Application of the action
```
ros2 action send_goal /draw_square example_interfaces/action/Fibonacci "{}"
```

## Demo launch

```
ros2 launch turtlesim_square demo_launch.py
```

Application of the action
```
ros2 action send_goal /draw_square example_interfaces/action/Fibonacci "{}"
```



