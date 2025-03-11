import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo, PushRosNamespace
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declarar los parámetros para la velocidad lineal y angular
        DeclareLaunchArgument('linear_speed', default_value='1.0', description='Velocidad lineal de la tortuga'),
        DeclareLaunchArgument('angular_speed', default_value='1.57', description='Velocidad angular de la tortuga'),

        # Lanzar el nodo TurtleSquareWithParams con los parámetros necesarios
        Node(
            package='turtlesim_square',  # Reemplaza con el nombre de tu paquete
            executable='turtle_square_with_params',  # Reemplaza con el nombre de tu ejecutable
            name='turtle_square_with_params',
            output='screen',
            parameters=[
                {'linear_speed': '$(arg linear_speed)'},
                {'angular_speed': '$(arg angular_speed)'}
            ],
            remappings=[('/turtle1/cmd_vel', '/turtle1/cmd_vel')]  # Asegúrate de que este remapeo sea necesario
        ),

        # Mensaje informativo
        LogInfo(
            condition=None,
            msg="Launching TurtleSquareWithParams node with parameters."
        )
    ])
