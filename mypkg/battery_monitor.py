import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

rclpy.init()
node = Node("battery_monitor")
pub = node.create_publisher(Float32, "batterylevel", 10)
battery = psutil.sensors_battery()

def cb():
    msg = Float32()
    msg.data = battery.percent
    pub.publish(msg)


def main():
    node.create_timer(2.0, cb)
    rclpy.spin(node)
