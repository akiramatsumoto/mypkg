#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

ros2 run mypkg battery_monitor &
ros2 topic echo /batterylevel
[ $? = 0 ] || exit 1
exit 0
