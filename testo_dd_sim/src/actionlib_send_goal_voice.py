#!/usr/bin/env python3

import rospy
import actionlib
import speech_recognition as sr 
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Rooms dictionary

building ={
            #[x ,  y , yaw]
    "home": [0.001, 0.001, 0.001],
    "101" : [-4.59, 6.31, 1.57],
    "102" : [5.16, 9.05, -1.08],
    "103" : [-0.57, -5.25, 0.0]

}
goal_now =""


def movebase_client():
    global goal_now
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()

    # Get goal from user voice
    # robot_pose = input("Enter you room number: ")
    # robot_goal = building[robot_pose]
    # goal_now = robot_pose

    def feedback_cb(self):
        rospy.loginfo("Going to "+ goal_now)
    
    while(not (client.get_result())):
        try:
            r = sr.Recognizer() 
            with sr.Microphone(device_index=0,chunk_size=8192) as source:                                                                       
                print("Where do you want to go ?")                                                                                   
                audio = r.listen(source)
                room = r.recognize_google(audio)
                print("You said " + room)
                try:
                    robot_goal = building[room]
                    goal_now =room

                    goal.target_pose.header.frame_id = "map"
                    goal.target_pose.header.stamp = rospy.Time.now()
                    goal.target_pose.pose.position.x = robot_goal[0]
                    goal.target_pose.pose.position.y = robot_goal[1]
                    goal.target_pose.pose.orientation.w = robot_goal[2]

                    client.send_goal(goal,feedback_cb=feedback_cb)
                    wait = client.wait_for_result()
                    if not wait:
                        rospy.logerr("Action server not available!")
                        rospy.signal_shutdown("Action server not available!")
                    else:
                        return client.get_result()
                except:
                    print("There is no "+room+" in the building")
                    continue

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


if __name__ == '__main__':
    while(1):
        rospy.init_node('movebase_client_py')
        try:
            # rospy.init_node('movebase_client_py')
            result = movebase_client()
            if result:
                rospy.loginfo("Goal execution done!")
            if result == 0:
                break
        except rospy.ROSInterruptException:
            rospy.loginfo("Navigation test finished.")
