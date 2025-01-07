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
timeout 60 ros2 topic echo batterylevel > - /tmp/mypkg.log
kill -9 $NODE_PID

cat /tmp/mypkg.log
percent=$(cat /tmp/mypkg.log | head -n 1)
if (( $(echo "$percent >= 0" | bc -l) )) && (( $(echo "$percent <= 100" | bc -l) )); then
    exit 0
else
    exit 1
fi

