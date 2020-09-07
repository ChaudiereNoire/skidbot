Nodes to be used on 4WD vehicle produced by StenSAT http://www.stensat.org/ 

The 4WD kit has two left wheels controlled by one controller and two right wheels controlled by a second controller.  Students will start with the simple ROS 2
nodes created here and modify them to accomplish more complex tasks.

To work with these files, you have to have first gotten ROS 2, preferably Foxy Fitzroy, up and running and completed the tutorial on creating a ROS 2 package.

Once you know how to devleop a ROS 2 package, you can look through the steps described in Writing a Simple Service and Client, which served as the base for
this example.

https://index.ros.org/doc/ros2/Tutorials/Writing-A-Simple-Py-Service-And-Client/

I ran 

ros2 pkg create skidbotcli --dependencies rclpy example_interfaces --build-type ament_python

to create the structure and then added in the drive code from the StenSAT tutorials.

You are going to have to create a custom service and custom interfaces to handle the variables used by the node.

https://index.ros.org/doc/ros2/Tutorials/Custom-ROS2-Interfaces/

ros2 pkg create --build-type ament_cmake tutorial_interfaces 

You run the service node by entering the command ros2 run skidbotcli service 
You drive the vehicle by entering the command    ros2 run skidbotcli client "forward" 622 30

The commands that are currently accepted are forward, reverse, left, right, and stop

