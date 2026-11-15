import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from qos_demo.qos_utils import make_qos


class QosPublisher(Node):

    def __init__(self):
        super().__init__('qos_publisher')

        # Parameters
        self.declare_parameter('reliability', 'reliable')
        self.declare_parameter('durability', 'volatile')
        self.declare_parameter('depth', 5)

        rel = self.get_parameter('reliability').value
        dur = self.get_parameter('durability').value
        depth = self.get_parameter('depth').value

        # Publisher
        self.pub = self.create_publisher(
            String,
            '/chatter',
            make_qos(rel, dur, depth)
        )

        self.count = 0

        self.create_timer(1.0, self.timer_callback)

        self.get_logger().info(
            f'Publisher QoS: {rel}, {dur}, depth {depth}'
        )

    def timer_callback(self):

        self.count += 1

        msg = String()
        msg.data = f'message {self.count}'

        self.pub.publish(msg)

        self.get_logger().info(f'Sent: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    node = QosPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
