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

EJECUTAR EL SERVICIO
```
ros2 run turtlesim_square draw_square_service
```

LLAMAR AL SERVICIO
```
ros2 service call /draw_square std_srvs/srv/Trigger
```

## Make it an action

```
ros2 run turtlesim turtlesim_node   
```

EJECUTA LA ACCION
```
ros2 run turtlesim_square draw_square_action
```

SOLICITUD DE ACCION
```
ros2 action send_goal /draw_square example_interfaces/action/Fibonacci "{}"
```

## Add parameter(s)

```
ros2 run turtlesim turtlesim_node   
```


## Demo launch


