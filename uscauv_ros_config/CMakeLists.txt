# Catkin User Guide: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/user_guide.html
# Catkin CMake Standard: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/standards.html
cmake_minimum_required(VERSION 2.8.3)
project(uscauv_ros_config)
# Load catkin and all dependencies required for this package
# TODO: remove all from COMPONENTS that are not catkin packages.
find_package(catkin REQUIRED)
catkin_metapackage()