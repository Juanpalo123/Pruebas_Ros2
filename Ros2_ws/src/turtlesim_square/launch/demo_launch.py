import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # Lanzar turtlesim
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen'
        ),

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
                {'linear_speed': float(os.environ.get('ROS_LINEAR_SPEED', '1.0'))},
                {'angular_speed': float(os.environ.get('ROS_ANGULAR_SPEED', '1.57'))}
            ],
            remappings=[('/turtle1/cmd_vel', '/turtle1/cmd_vel')]  
        ),

        # Mensaje informativo
        LogInfo(
            condition=None,
            msg="Launching TurtleSquareWithParams node with parameters."
        )
    ])
