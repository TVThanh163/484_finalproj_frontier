# TurtleBot 4 Autonomous Frontier Exploration

This repository contains the packages and launch files required to run autonomous frontier exploration on the TurtleBot 4 using ROS 2 and Nav2.

## 1. Prerequisites and Dependencies

Before building the packages, ensure your system has ROS 2 (Jazzy) and the necessary navigation and TurtleBot 4 packages installed.

### Install ROS 2
Ensure you have ROS 2 Jazzy installed on your Ubuntu system. If you haven't installed it yet, follow the [official ROS 2 Jazzy installation guide](https://docs.ros.org/en/jazzy/Installation.html).

### Install Nav2 and TurtleBot 4 Packages
Open a terminal and run the following commands to install the required dependencies for navigation and the TurtleBot 4 desktop environment:

```bash
sudo apt update
sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup
sudo apt install ros-jazzy-turtlebot4-navigation ros-jazzy-turtlebot4-desktop
sudo apt install ros-jazzy-rmw-fastrtps-cpp
```

## 2. Building the Workspaces

This project relies on two main workspaces that need to be built: `m-explore-ros2` (the frontier exploration logic) and `tb4_ws` (your custom robot bringup and launch files).

Navigate to the root of your project directory (`~/484_finalproj_frontier`) and build both packages using `colcon`.

**Build `m-explore-ros2`:**

```bash
cd ~/484_finalproj_frontier/m-explore-ros2
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
```

**Build `tb4_ws`:**

```bash
cd ~/484_finalproj_frontier/tb4_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
```

## 3. Running the Exploration in the Lab

To successfully communicate with the TurtleBot 4 in the lab environment, you must configure your network settings to use the correct Domain ID, Fast RTPS middleware, and the centralized Discovery Server before launching the autonomy stack.

Open a new terminal and run the following commands in order:

```bash
# 1. Source the base ROS 2 Jazzy installation
source /opt/ros/jazzy/setup.bash 

# 2. Configure network and middleware settings for the lab environment
export ROS_DOMAIN_ID=2 
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp 

# 3. Source the TurtleBot 4 Discovery Server configuration
source /etc/turtlebot4_discovery/setup.bash 

# 4. Source the built exploration and custom workspace overlays
source ~/484_finalproj_frontier/m-explore-ros2/install/setup.bash 
source ~/484_finalproj_frontier/tb4_ws/install/setup.bash 

# 5. Launch the autonomous frontier exploration stack
ros2 launch my_robot_bringup autonomy.launch.py
```

### Notes on Execution
* Ensure the TurtleBot 4 is powered on and connected to the same Discovery Server network before running the launch command.
* The `autonomy.launch.py` file handles the initialization of SLAM, Nav2, and the `explore_lite` node simultaneously. You should see RViz open automatically (if configured in your launch file) to visualize the mapping process.

### [Video Demonstration](https://drive.google.com/drive/folders/1FdxSFfPrFTKxkJf2epyAVT496P3k9zny?usp=sharing)