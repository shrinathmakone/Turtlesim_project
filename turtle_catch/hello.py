import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class HelloTracer(Node):
    def __init__(self):
        super().__init__('hello_tracer')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1)  # Wait for publisher to connect
        self.trace_hello()

    def move(self, linear_x, angular_z, duration):
        msg = Twist()
        msg.linear.x = float(linear_x)
        msg.angular.z = float(angular_z)
        self.publisher.publish(msg)
        time.sleep(duration)
        # Stop
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher.publish(msg)
        time.sleep(0.5)

    def trace_hello(self):
        self.get_logger().info('Starting to trace "HELLO"...')
        
        # Example for 'H'
        self.move(2.0, 0.0, 1.0)   # Left vertical
        self.move(-1.0, 0.0, 1.0)  # Move to middle
        self.move(0.0, 1.57, 1.0)  # Turn 90 deg
        self.move(1.0, 0.0, 1.0)   # Crossbar
        # ... Add remaining letters using similar move logic ...