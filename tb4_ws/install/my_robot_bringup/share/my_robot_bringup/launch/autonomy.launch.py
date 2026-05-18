from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Paths to the launch files you were running manually
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([FindPackageShare('turtlebot4_navigation'), 'launch', 'slam.launch.py'])
        ])
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([FindPackageShare('turtlebot4_navigation'), 'launch', 'nav2.launch.py'])
        ])
    )

    viz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([FindPackageShare('turtlebot4_viz'), 'launch', 'view_navigation.launch.py'])
        ])
    )

    explore_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([FindPackageShare('explore_lite'), 'launch', 'explore.launch.py'])
        ]),
        launch_arguments={
            'robot_base_frame': 'base_link',
            'costmap_topic': '/global_costmap/costmap',
            'visualize': 'true'
        }.items()
    )

    return LaunchDescription([
        slam_launch,
        nav2_launch,
        viz_launch,
        explore_launch
    ])
