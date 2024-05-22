#!/bin/bash

ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro ~/fyp/v2scara/src/description/robot.urdf.xacro)" &
sleep 2
ros2 run joint_state_publisher_gui joint_state_publisher_gui &

rviz2 --f base_link
