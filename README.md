# Blower control

# install
```
$ cd ~/catkin_ws/src/
$ git clone git@github.com:110kazuki/blower_control.git
$ cd ~/catkin_ws
$ catkin_make
```

# run
## Step1   


## Step2   
@Terminal 1   
```
roscore
```

@Terminal 2
```
rosrun joy joy_node
```

@Terminal 3
```
rosrun blower_control scripts/joycon_ope.py
```

@Terminal 4
```
rosrun rosserial_python serial_node.py tcp
```
