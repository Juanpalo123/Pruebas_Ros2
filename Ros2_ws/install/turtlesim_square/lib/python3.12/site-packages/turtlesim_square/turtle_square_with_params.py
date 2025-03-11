#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from geometry_msgs.msg import Twist
from example_interfaces.action import Fibonacci
import time

class TurtleSquareWithParams(Node):
    def __init__(self):
        super().__init__('turtle_square_with_params')

        # Declarar parámetros con valores predeterminados
        self.declare_parameter('linear_speed', 1.0)  # Velocidad lineal por defecto
        self.declare_parameter('angular_speed', 1.57)  # Velocidad angular por defecto (90 grados)

        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Crear el servidor de acción
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'draw_square',
            self.execute_callback
        )

        self.get_logger().info("TurtleSquare action with parameters ready. Call 'draw_square' to start drawing a square.")

    def execute_callback(self, goal_handle):
        self.get_logger().info("Received action request: Drawing a square")

        move_cmd = Twist()
        feedback_msg = Fibonacci.Feedback()

        # Obtener parámetros
        linear_speed = self.get_parameter('linear_speed').get_parameter_value().double_value
        angular_speed = self.get_parameter('angular_speed').get_parameter_value().double_value

        for i in range(4):
            # Actualizar el estado
            feedback_msg.sequence.append(i + 1)
            goal_handle.publish_feedback(feedback_msg)

            # Mover hacia adelante
            move_cmd.linear.x = linear_speed
            move_cmd.angular.z = 0.0
            self.publisher.publish(move_cmd)
            self.get_logger().info(f"Moving forward (Side {i + 1}/4) at speed {linear_speed}")
            time.sleep(2)

            # Detener
            move_cmd.linear.x = 0.0
            self.publisher.publish(move_cmd)
            time.sleep(1)

            # Girar 90 grados
            move_cmd.angular.z = angular_speed
            self.publisher.publish(move_cmd)
            self.get_logger().info(f"Turning 90 degrees at speed {angular_speed}")
            time.sleep(1)

            # Detener rotación
            move_cmd.angular.z = 0.0
            self.publisher.publish(move_cmd)
            time.sleep(1)

        self.get_logger().info("Square drawing completed")

        goal_handle.succeed()

        # Enviar el resultado
        result = Fibonacci.Result()
        result.sequence = feedback_msg.sequence
        return result

def main():
    rclpy.init()
    turtle_square_with_params = TurtleSquareWithParams()
    rclpy.spin(turtle_square_with_params)
    turtle_square_with_params.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
