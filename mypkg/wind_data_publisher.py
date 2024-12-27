

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Int16
import requests

class WindDataPublisher(Node):
    def __init__(self):
        super().__init__("wind_data_publisher")

        self.wind_speed_pub = self.create_publisher(Float32, "wind_speed", 10)
        self.wind_deg_pub = self.create_publisher(Int16, "wind_direction", 10)

        self.create_timer(5.0, self.publish_wind_data)

        self.api_key = "570dc450e51af949569d2f4a4d2201cf"
        # 場所を変えたい場合はここで変更
        self.city = "Tokyo"
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"

    def get_wind_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                wind_speed = data['wind']['speed']
                wind_deg = data['wind'].get('deg', None)  # 風向が存在しない場合に備える
                return wind_speed, wind_deg
            else:
                self.get_logger().error(f"天気データの取得に失敗しました。レスポンスコード: {response.status_code}")
                return None, None
        except Exception as e:
            self.get_logger().error(f"天気データの取得中にエラーが発生しました: {e}")
            return None, None

    def publish_wind_data(self):
        wind_speed, wind_deg = self.get_wind_data()
        if wind_speed is not None and wind_deg is not None:
            # 風速をパブリッシュ
            wind_speed_msg = Float32()
            wind_speed_msg.data = float(wind_speed)
            self.wind_speed_pub.publish(wind_speed_msg)
            self.get_logger().info(f"風速をパブリッシュしました: {wind_speed_msg.data} m/s")

            # 風向をパブリッシュ
            wind_deg_msg = Int16()
            wind_deg_msg.data = int(wind_deg)
            self.wind_deg_pub.publish(wind_deg_msg)
            self.get_logger().info(f"風向をパブリッシュしました: {wind_deg_msg.data} 度")

        else:
            self.get_logger().warn("天気データがないため、パブリッシュできませんでした。")


def main(args=None):
    rclpy.init()
    node = WindDataPublisher()
    rclpy.spin(node)

