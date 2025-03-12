#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from geometry_msgs.msg import Twist
from example_interfaces.action import Fibonacci  
import time

class TurtleSquareAction(Node):
    def __init__(self):
        super().__init__('turtle_square_action')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Crear el servidor de acción
        self._action_server = ActionServer(
            self,
            Fibonacci,  
            'draw_square',
            self.execute_callback
        )

        self.get_logger().info("TurtleSquare action ready. Call 'draw_square' to start drawing a square.")

    def execute_callback(self, goal_handle):
        self.get_logger().info("Received action request: Drawing a square")

        move_cmd = Twist()
        feedback_msg = Fibonacci.Feedback()

        for i in range(4):
            # Actualizar el estado
            feedback_msg.sequence.append(i + 1)
            goal_handle.publish_feedback(feedback_msg)

            # Mover hacia adelante
            move_cmd.linear.x = 1.0
            move_cmd.angular.z = 0.0
            self.publisher.publish(move_cmd)
            self.get_logger().info(f"Moving forward (Side {i + 1}/4)")
            time.sleep(2)

            # Detener
            move_cmd.linear.x = 0.0
            self.publisher.publish(move_cmd)
            time.sleep(1)

            # Girar 90 grados
            move_cmd.angular.z = 1.57
            self.publisher.publish(move_cmd)
            self.get_logger().info("Turning 90 degrees")
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
    turtle_square_action = TurtleSquareAction()
    rclpy.spin(turtle_square_action)
    turtle_square_action.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
