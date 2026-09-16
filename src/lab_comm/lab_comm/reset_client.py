import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class ResetClientNode(Node):
    def __init__(self):
        super().__init__('reset_client_node')
        self.client = self.create_client(Trigger, 'reset_system')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Menunggu service /reset_system...')

    def send_request(self):
        req = Trigger.Request()
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main():
    rclpy.init()
    node = ResetClientNode()
    response = node.send_request()
    node.get_logger().info(f'Respon dari server: {response.message}')
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()

if __name__ == '__main__':
    main()
