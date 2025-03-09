#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info("Drawing a square with turtlesim...")
        self.draw_square()

    def draw_square(self):
        move_cmd = Twist()

        for _ in range(4):
            # Move forward
            move_cmd.linear.x = 1.0  # Set linear speed
            move_cmd.angular.z = 0.0
            self.publisher.publish(move_cmd)
            self.get_logger().info("Moving forward")
            time.sleep(2)  # Move for 2 seconds

            # Stop
            move_cmd.linear.x = 0.0
            self.publisher.publish(move_cmd)
            time.sleep(1)

            # Rotate 90 degrees
            move_cmd.angular.z = 1.57  # Approx. 90 degrees (in radians)
            self.publisher.publish(move_cmd)
            self.get_logger().info("Turning 90 degrees")
            time.sleep(1)

            # Stop
            move_cmd.angular.z = 0.0
            self.publisher.publish(move_cmd)
            time.sleep(1)

        self.get_logger().info("Finished drawing a square")

def main():
    rclpy.init()
    turtle_square = TurtleSquare()
    rclpy.spin(turtle_square)
    turtle_square.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
