# 🤖 ROS 2 Robot Black Box

## 📌 Project Overview

The **ROS 2 Robot Black Box** is a robotics monitoring and debugging project developed using ROS 2 and Python. It demonstrates how to monitor important robot parameters, detect abnormal operating conditions, and record sensor data for later analysis.

The project uses ROS 2 publishers and subscribers to exchange sensor information between nodes. It also demonstrates **Quality of Service (QoS)** configuration, ROS 2 debugging tools, and rosbag recording and playback.

## 🎯 Objectives

- Monitor robot battery level and temperature.
- Detect low-battery and high-temperature conditions.
- Publish robot health status using ROS 2 topics.
- Understand and configure ROS 2 QoS policies.
- Record sensor data using rosbag.
- Replay recorded data for debugging and analysis.
- Understand QoS compatibility between publishers and subscribers.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Robotics Middleware:** ROS 2 Humble
- **Communication:** ROS 2 Topics, Publishers and Subscribers
- **Message Types:** `std_msgs/Float32`, `std_msgs/String`
- **Data Recording:** ROS 2 Bags
- **QoS:** Reliability, Durability and History policies

##  Main Features

### 1. Robot Sensor Monitoring
- Publishes battery level and temperature data.
- Simulates battery consumption using a configurable drain rate.
- Generates temperature values based on battery consumption.

### 2. Robot Health Monitoring
- Subscribes to battery and temperature topics.
- Checks sensor values against predefined thresholds.
- Publishes robot status:
  - `OK`
  - `WARNING: LOW BATTERY`
  - `WARNING: HIGH TEMPERATURE`

### 3. QoS Demonstration
Demonstrates ROS 2 Quality of Service policies:
- Reliability
- Durability
- History and queue depth

Explores publisher-subscriber QoS compatibility and how incompatible configurations affect message delivery.

### 4. Rosbag Recording and Playback
- Records sensor topics for later analysis.
- Replays recorded sensor data.
- Observes changes in robot health status during playback.
- Supports playback speed adjustment.

##  Installation and Execution

### Prerequisites

- Ubuntu Linux
- ROS 2 Humble
- Python 3
- Colcon build tools

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ROS2-Robot-Black-Box
```

### 2. Build the Workspace

```bash
colcon build
```

### 3. Source the Workspace

```bash
source install/setup.bash
```

### 4. Run the Sensor Node

```bash
ros2 run robot_monitor1 sensor_node
```

### 5. Run the Monitor Node

Open another terminal and source the workspace:

```bash
source ~/blackbox-ws/install/setup.bash
ros2 run robot_monitor1 monitor_node
```

## ROS 2 Topics

    Topic          | Message Type | Description |
| /battery_level   | Float32      | Publishes battery percentage |
| /temperature     | Float32      | Publishes temperature |
| /robot_status    | String       | Publishes robot health status |
| /chatter`        | String       | Used for QoS communication testing |
