# python_pub_sub
#This is the example of pub sub by ROS with python
--------------------------------------------------
--------------------------------------------------
#Link source code: 
# clone source code into folder src in folder catkin_ws
git clone https://github.com/fpt-corp/ROS_Package_example?fbclid=IwAR1UZ0kZFpZcbZZOhbGWSupyf4_qb0EsNiDBdEbGE39htBL_WQcaZ7RecKE
# in some cases file Unity can not open because this size is too big, fix here https://github.com/git-lfs/git-lfs/wiki/Installation and then go to catkin_ws "git lfs pull"
# go to catkin_ws/src and "git clone" this link 
git clone https://github.com/minhvuquang080598/python_pub_sub.git
---------------------------------------------------
---------------------------------------------------
#HOW TO CREATE A PYTHON NODE
# Run all topic respectively (look in lane_detect.launch)
cd catkin_ws/ && catkin_make && source devel/setup.bash && roslaunch lane_detect lane_detect.launch
#Ctrl-Shift-T to open new terminal windows
# Run python 
source devel/setup.bash && rosrun python_lane_detect python_lane_detect.py
#Ctrl-Shift-T to open new terminal windows
#open stimulation
cd src/unity && ./test.x86_64

# Simulation information
Team1
ws://127.0.0.1:9090
------------------------------------------------------
------------------------------------------------------
