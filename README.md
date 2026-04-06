# Turtlesim_project
# 🐢 ROS2 Turtlesim Automation

A ROS2-based automation project where turtles are continuously spawned and intelligently removed based on proximity.

---

## 🚀 Features
- Spawn a new turtle every second
- Detect the nearest turtle dynamically
- Remove the nearest turtle using control logic

---

## 🧠 Concepts Used
- ROS2 Nodes
- Topics & Services
- Real-time decision making

---

## ▶️ How to Run

```bash
ros2 run turtlesim turtlesim_node
ros2 run turtle_catch spawner_node
ros2 run turtle_catch controller_node
