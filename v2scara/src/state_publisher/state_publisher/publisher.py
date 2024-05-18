#!/usr/bin/env python3
import rclpy
import socket
import math
from rclpy.node import Node
from sensor_msgs.msg import JointState     

HOST = '192.168.222.55'
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
class PublisherNode(Node): 
        def __init__(self):
            super().__init__("publisher") 
            self.subscriber = self.create_subscription(JointState,"joint_states",self.callback_publisher, 10)
            self.get_logger().info("Publisher started")
        def callback_publisher(self, msg):
            value = msg.name[0]+str(int(10-(msg.position[0]*-1)*10/0.445))+"#"+msg.name[1]+str(int((msg.position[1]*180/math.pi)+90))+"#"+msg.name[2]+str(int((msg.position[2]*180/math.pi)+90))+"#"+msg.name[3]+str(int((msg.position[3]*180/math.pi)+90))
            print(value)
            client_socket.send(str(value).encode("utf-8"))
     
def main(args=None):
        rclpy.init(args=args)
        node = PublisherNode() 
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
     
if __name__ == "__main__":
        main()
