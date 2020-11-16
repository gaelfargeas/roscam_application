cmake_minimum_required(VERSION 3.0.2)
project(roscam_application)


if( CATKIN_DEVEL_PREFIX OR catkin_FOUND OR CATKIN_BUILD_BINARY_PACKAGE)
    set(COMPILING_WITH_CATKIN 1)

    message(STATUS "---------------------------------------------------------------------")
    message(STATUS "Roscam_application is being built using CATKIN. ROS plugins will be compiled")
    message(STATUS "---------------------------------------------------------------------")

    set(ROS_DEPENDENCIES
        rospy
        std_msgs        
        )

    find_package(catkin REQUIRED COMPONENTS 
        message_generation
        ${ROS_DEPENDENCIES} 
        )
    
    add_message_files(
        FILES
        DHT22.msg
        )

    catkin_python_setup()
        
    generate_messages(
        DEPENDENCIES
        std_msgs
        )

    catkin_package(
        CATKIN_DEPENDS 
            message_runtime
            ${ROS_DEPENDENCIES}  
        )

endif()


set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
SET(CMAKE_AUTOUIC ON)

if(NOT CMAKE_VERSION VERSION_LESS 3.1)
    set(CMAKE_CXX_STANDARD 14)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
endif()

if (NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -fno-omit-frame-pointer")
endif()

###########
## Build ##
###########

find_package(Qt5 REQUIRED COMPONENTS
    Core
    Widgets
    Multimedia
    MultimediaWidgets
    PrintSupport
    Concurrent
    Qml
    Xml
    Svg)

find_package(Qt5 QUIET COMPONENTS WebSockets)

set( QT_LINK_LIBRARIES
    Qt5::Core
    Qt5::Widgets
    Qt5::PrintSupport
    Qt5::Xml
    Qt5::Concurrent
    Qt5::Multimedia
    Qt5::MultimediaWidgets
    Qt5::Qml
    Qt5::Svg
    )

add_definitions( -DQWT_NO_SVG )

if( NOT Qt5WebSockets_FOUND)
    message(STATUS "Can't find Qt5WebSockets in your system. Have you tried [sudo apt-get install libqt5websockets5-dev] ?")
    add_definitions( -DQWT_NO_SVG )
else()
    set( QT_LINK_LIBRARIES ${QT_LINK_LIBRARIES} Qt5::WebSockets)
endif()


include_directories(
    ${Qt5Core_INCLUDE_DIRS}
    ${Qt5Gui_INCLUDE_DIRS}
    ${Qt5Widgets_INCLUDE_DIRS}
    ${Qt5Concurrent_INCLUDE_DIRS}
    ${Qt5PrintSupport_INCLUDE_DIRS}
    ${Qt5Xml_INCLUDE_DIRS}
    ${Qt5WebSockets_INCLUDE_DIRS}
    ${Qt5Multimedia_INCLUDE_DIRS}
    ${Qt5MultimediaWidgets_INCLUDE_DIRS}
    ${Qt5Svg_INCLUDE_DIRS}
    ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

catkin_install_python(PROGRAMS
  scripts/roscam_application
  # scripts/threaded_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


#############
## Testing ##
#############
