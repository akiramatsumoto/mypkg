#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

ros2 run mypkg battery_monitor &
NODE_PID=$!
timeout 10 ros2 topic echo /batterylevel | tee - /tmp/mypkg.log
kill $NODE_PID

percent=$(cat /tmp/mypkg.log | grep data | head -n 1 | sed 's/data://')
echo "電池残量"$percent"%"
