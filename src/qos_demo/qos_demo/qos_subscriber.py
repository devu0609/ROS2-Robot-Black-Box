import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from qos_demo.qos_utils import make_qos


class QosSubscriber(Node):

    def __init__(self):
        super().__init__('qos_subscriber')

        # Parameters
        self.declare_parameter('reliability', 'reliable')
        self.declare_parameter('durability', 'volatile')
        self.declare_parameter('depth', 5)

        rel = self.get_parameter('reliability').value
        dur = self.get_parameter('durability').value
        depth = self.get_parameter('depth').value

        # Subscriber
        self.sub = self.create_subscription(
            String,
            '/chatter',
            self.callback,
            make_qos(rel, dur, depth)
        )

        self.get_logger().info(
            f'Subscriber QoS: {rel}, {dur}, depth {depth}'
        )

    def callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    node = QosSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
