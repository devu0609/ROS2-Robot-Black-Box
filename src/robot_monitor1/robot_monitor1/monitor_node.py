import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class MonitorNode(Node):

    def __init__(self):
        super().__init__('monitor_node')

        self.battery_sub = self.create_subscription(
            Float32, '/battery_level', self.battery_callback, 10
        )

        self.temp_sub = self.create_subscription(
            Float32, '/temperature', self.temp_callback, 10
        )

        self.motor_current_sub = self.create_subscription(
            Float32, '/motor_current', self.motor_current_callback, 10
        )   

        self.status_pub = self.create_publisher(
            String, '/robot_status', 10
        )

        self.last_battery = 100.0
        self.last_temp = 25.0
        self.motor_current = 0.0

        self.get_logger().info('Monitor node started')

    def battery_callback(self, msg):
        self.last_battery = msg.data
        self.evaluate_status()

    def temp_callback(self, msg):
        self.last_temp = msg.data
        self.evaluate_status()

    def motor_current_callback(self, msg):
        self.motor_current = msg.data
        self.evaluate_status()    

    def evaluate_status(self):
        status = String()

        # Thresholds: Battery drops below 20% or temperature exceeds 60°C
        if self.last_battery < 20.0 or self.last_temp > 60.0:

            reasons = []

            if self.last_battery < 20.0:
                reasons.append('LOW BATTERY')

                self.get_logger().warn(
                    f'LOW BATTERY warning: {self.last_battery:.1f}%'
                )

            if self.last_temp > 60.0:
                reasons.append('HIGH TEMPERATURE')

                self.get_logger().warn(
                    f'HIGH TEMPERATURE warning: {self.last_temp:.1f}°C'
                )

            if self.motor_current > 5.0:
                reasons.append('HIGH MOTOR CURRENT')

                self.get_logger().warn(
                    f'HIGH MOTOR CURRENT warning: {self.motor_current:.1f}A'
                )       

            status.data = 'WARNING: ' + ' & '.join(reasons)

        else:
            status.data = 'OK'

        self.status_pub.publish(status)


def main(args=None):
    rclpy.init(args=args)

    node = MonitorNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()