#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger
import time

class TurtleSquareService(Node):
    def __init__(self):
        super().__init__('turtle_square_service')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.srv = self.create_service(Trigger, 'draw_square', self.draw_square_callback)
        self.get_logger().info("TurtleSquare service ready. Call 'draw_square' to start drawing a square.")

    def draw_square_callback(self, request, response):
        self.get_logger().info("Received request: Drawing a square")
        self.draw_square()
        response.success = True
        response.message = "Finished drawing a square"
        return response

    def draw_square(self):
        move_cmd = Twist()

        for _ in range(4):
            # Move forward
            move_cmd.linear.x = 1.0
            move_cmd.angular.z = 0.0
            self.publisher.publish(move_cmd)
            self.get_logger().info("Moving forward")
            time.sleep(2)

            # Stop
            move_cmd.linear.x = 0.0
            self.publisher.publish(move_cmd)
            time.sleep(1)

            # Rotate 90 degrees
            move_cmd.angular.z = 1.57
            self.publisher.publish(move_cmd)
            self.get_logger().info("Turning 90 degrees")
            time.sleep(1)

            # Stop rotation
            move_cmd.angular.z = 0.0
            self.publisher.publish(move_cmd)
            time.sleep(1)

        self.get_logger().info("Square drawing completed")

def main():
    rclpy.init()
    turtle_square_service = TurtleSquareService()
    rclpy.spin(turtle_square_service)
    turtle_square_service.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
