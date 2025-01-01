#!/bin/bash
# SPDX-FileCopyrightText: 2024 Akira Matsumoto <akiram8427@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

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
if (( $(echo "$percent >= 0" | bc -l) )) && (( $(echo "$percent <= 100" | bc -l) )); then
    exit 0
else
    echo 1
fi
