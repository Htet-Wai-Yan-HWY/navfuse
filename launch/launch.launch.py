# Copyright 2019 Samsung Research America
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([

        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='bl_gps',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'base_link', 'gps_link']
        ),

        launch_ros.actions.Node(
            package='robot_localization',
            executable='navsat_transform_node',
            name='navsat_transform_node',
            output='screen',
            #parameters=[os.path.join(get_package_share_directory("navfuse"), 'config', 'navsat_transform.yaml')],
            remappings=[
                # ('/imu/data', '/imu/micro'),
                #('/gps/fix', '/gps/micro'),
                ('/gps/fix', '/fix'),
                # ('/odometry/filtered', '/odometry/filtered'),
        ]
           ),
        # launch_ros.actions.Node(
        #     package='robot_localization',
        #     executable='ekf_node',
        #     name="ekf_localization_node",
        #     output='screen',
        #     parameters=[os.path.join(get_package_share_directory("navfuse"), 'config', 'ekf_with_gps.yaml')],


        # ),
])