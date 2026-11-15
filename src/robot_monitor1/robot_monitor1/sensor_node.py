import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorNode(Node):

    def __init__(self):
        super().__init__('sensor_node')

        # Battery drain parameter
        self.declare_parameter('drain_rate', 0.5)

        self.battery = 100.0

        # Publishers
        self.battery_pub = self.create_publisher(
            Float32, '/battery_level', 10
        )

        self.temp_pub = self.create_publisher(
            Float32, '/temperature', 10
        )

        self.current_pub = self.create_publisher(
            Float32, '/motor_current', 10
        )

        # Timer: executes every second
        self.timer = self.create_timer(1.0, self.update)

        self.get_logger().info('Sensor node started')

    def update(self):

        # Read updated parameter
        rate = self.get_parameter('drain_rate').value

        # Decrease battery
        self.battery = max(0.0, self.battery - rate)

        # Calculate temperature
        temperature = 25.0 + (100.0 - self.battery) * 0.5

        # Create messages
        b = Float32()
        b.data = float(self.battery)

        t = Float32()
        t.data = float(temperature)

        c = Float32()
        c.data = float(2.0 + (100.0 - self.battery) * 0.05)  # Simulated motor current  


        # Publish sensor values
        self.battery_pub.publish(b)
        self.temp_pub.publish(t)
        self.current_pub.publish(c)

        self.get_logger().info(
            f'Battery = {self.battery:.1f}% '
            f'Temperature = {temperature:.1f}°C '
        )


def main(args=None):
    rclpy.init(args=args)

    node = SensorNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()