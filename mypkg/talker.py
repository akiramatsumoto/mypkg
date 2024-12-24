import rclpy
from rclpy.node import Node
from person_msgs.srv import Query
import random

rclpy.init()
node = Node("talker")


def cb(request, response):
    # 送られた数字を繰り返し回数に
    loop = request.name + 1
    # 数字の回数の桁数を生成するアルゴリズム
    mylist = list(range(loop))
    for i in range(1, loop, 1):
        mylist[i] = random.randrange(10)
    mojiretu = ""
    for h in range(1, loop, 1):
        mojiretu += str(mylist[h])
    response.age = int(mojiretu)
    # レスポンスを返す
    return response


def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)
