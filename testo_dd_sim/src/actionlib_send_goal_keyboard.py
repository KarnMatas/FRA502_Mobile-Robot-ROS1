#!/usr/bin/env python3

import rospy
import actionlib
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
# def feedback_cb(self, feedback):
#     rospy.loginfo("Feedback for goal pose "+str()+" received")

def movebase_client():
    global goal_now
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()

    # Get goal from user
    robot_pose = input("Enter you room number: ")
    robot_goal = building[robot_pose]
    goal_now = robot_pose

    def feedback_cb(self):
        rospy.loginfo("Going to "+ goal_now)

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

if __name__ == '__main__':
    while(1):
        rospy.init_node('movebase_client_py')
        try:
            # rospy.init_node('movebase_client_py')
            result = movebase_client()
            if result:
                rospy.loginfo("Goal execution done!")
        except rospy.ROSInterruptException:
            rospy.loginfo("Navigation test finished.")
