#!/usr/bin/env python
import subprocess
import os
import tempfile
import shutil

home = os.getenv("HOME")
print home

code = subprocess.check_output("lsb_release -c", shell=True)
code = code.partition('\t')[2].strip()
if code != "oneiric" and code != "precise" and code != "quantal" :
    print "Code not recognized (supported versions are oneiric, precise, and quantal)"
    print "Your version is " + code
    print "We will continue assuming that installing quantal packages will work, but your mileage may vary"
    code = "quantal"
print "Installing packages assuming version " + code

print "We will now ask for your password so we can install things as root"

subprocess.call("sudo sh -c 'echo \"deb http://packages.ros.org/ros/ubuntu "+code+" main\" > /etc/apt/sources.list.d/ros-latest.list'", shell=True)
subprocess.call("wget http://packages.ros.org/ros.key -O - | sudo apt-key add -", shell=True)
subprocess.call("sudo apt-get update", shell=True)
subprocess.call("sudo apt-get install ros-groovy-desktop-full", shell=True)
subprocess.call("sudo rosdep init", shell=True)
subprocess.call("rosdep update", shell=True)

subprocess.call("echo \"source /opt/ros/groovy/setup.bash\" >> ~/.bashrc", shell=True)
subprocess.call("echo \"export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:"+home+"/catkin_ws/src >> ~/.bashrc", shell=True)
subprocess.call("source ~/.bashrc", shell=True)

subprocess.call("sudo apt-get install python-rosinstall ros-groovy-joystick-drivers libgsl0-dev libtesseract-dev ros-groovy-camera1394", shell=True)

subprocess.call("mkdir -p ~/catkin_ws/src", shell=True)
os.chdir(home+"/catkin_ws/src")
subprocess.call("git clone https://github.com/uscauv/uscauv-ros-pkg.git", shell=True)
subprocess.call("git clone https://github.com/uscauv/uscauv-ros-config.git -b groovy_unstable", shell=True)


subprocess.call("git clone https://code.google.com/p/usc-interaction-software.ros/", shell=True)

subprocess.call("sudo apt-get install libleptonica-dev", shell=True)

print "Setting up camera udev rules"
subprocess.call("uscauv-ros-config/uscauv_device/udev/install_seabee_udev.sh", shell=True)
