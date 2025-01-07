#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Akira Matsumoto <akiram8427@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil
import os

class BatteryInfoProvider:
    # バッテリー情報を取得, だめならエラーメッセージを表示
    def get_battery_status(self):
        battery = psutil.sensors_battery()
        if battery is None:
            raise RuntimeError("Battery information is not available.")
        return battery.percent

class MockBatteryInfoProvider:
    # mock_valueを設定
    def __init__(self, mock_value=50):
        self.mock_value = mock_value

    # mock_valueを返す
    def get_battery_status(self):
        return self.mock_value

def main():
    rclpy.init()
    node = Node("battery_monitor")
    pub = node.create_publisher(Float32, "batterylevel", 10)

    # 環境変数でモックか実機かを切り替える
    # 環境変数USE_MOCK_BATTERYが設定されていればmock_value=75に
    use_mock = os.getenv("USE_MOCK_BATTERY", "false").lower() == "true"
    if use_mock:
        provider = MockBatteryInfoProvider(mock_value=75)
    else:
        provider = BatteryInfoProvider()

    def cb():
        try:
            battery_status = provider.get_battery_status()
            msg = Float32()
            msg.data = float(battery_status)
            pub.publish(msg)
        except RuntimeError as e:
            node.get_logger().warn(str(e))

    node.create_timer(2.0, cb)
    rclpy.spin(node)

