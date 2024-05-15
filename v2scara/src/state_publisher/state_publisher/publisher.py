#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState     
     
class PublisherNode(Node): 
        def __init__(self):
            super().__init__("publisher") 
            self.subscriber = self.create_subscription(JointState,"joint_states",self.callback_publisher, 10)
            self.get_logger().info("Publisher started")
        def callback_publisher(self, msg):
            print(msg.position)
     
def main(args=None):
        rclpy.init(args=args)
        node = PublisherNode() 
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
     
if __name__ == "__main__":
        main()
