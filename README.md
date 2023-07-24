# Testo_dd_sim_Mobile-Robot-ROS1
## Introduction
หุ่นยนต์สำหรับช่วย รปภ. ตรวจตราในอาคาร หุ่นจะรับคำสั่งเสียงแล้วเคลื่อนที่ไปยังห้องที่สั่ง โดยหุ่นยนต์มีล้อขับเคลื่อนแบบ differential drive

![This is an image](https://github.com/KarnMatas/FRA502_Mobile-Robot-ROS1/blob/main/simulation_images/Screenshot%20from%202023-07-24%2017-23-10.png?raw=true)

## OS and ROS
* Ubuntu 20.04 LTS
* ROS Noetic
## Dependencies
* actionlib
* actionlib_msgs
* gazebo_ros
* geometry_msgs
* move_base_msgs
* nav_msgs
* rospy
* sensor_msgs
* speech_recognition (python lib)
* std_msgs
* tf
## Commands
### Create Map
รันคำสั่งเรียกใช้ Gmapping เพื่อให้หุ่นสามารถเก็บแมพได้
```bash
roslaunch testo_dd_sim building_map_gmapping.launch
```
รันคำสั่งให้สามารถควบคุมหุ่นยนต์ด้วยคีบอร์ดได้ในอีก terminal
```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py 
```
เมื่อได้แมพที่ต้องการให้รันคำสั่งฃ
```bash
rosrun map_server map_saver -f <ที่อยู่ของไฟล์ map>
```
### Full Operation
รันคำสั่งเพื่อให้หุ่นสามารถใช้ move_base ให้ใช้งานระบบ navigation ได้
```bash
roslaunch testo_dd_sim nav_to_goal.launch
```
รันคำสั่งเพื่อรับคำสั่งเสียงแล้วเคลื่อนที่ไปยังห้องที่ต้องการได้ในอีก terminal
```bash
rosrun testo_dd_sim actionlib_send_goal_voice.py
```
ห้องที่ใช้เป็นคำสั่งเสียงได้มีอยู่ 4 คำสั่ง
* home : POSE เริ่มต้นที่หุ่น spawn
* 101  : ห้อง 101
* 102  : ห้อง 102
* 103  : ห้อง 103
  
![This is an image](https://github.com/KarnMatas/FRA502_Mobile-Robot-ROS1/blob/main/simulation_images/Screenshot%20from%202023-07-24%2017-18-29.png?raw=true)

## Problems
* ขณะนี้ในส่วนของการรับคำสั่งเสียงสามารถทำงานได้ปกติแต่ขณะใช้งานจะมี error ของ driverเกี่ยวกับเสียงขึ้นมารบกวนอยู่
* แมพที่ลองสร้างอาจจะมีความกว้างและสิ่งกีดขวางน้อยเกินไปจนอาจทำให้ AMCL ทำงานได้ไม่ดีพอในตอนที่ทำ navigation จึงยังมีการหลงแมพอยู่
