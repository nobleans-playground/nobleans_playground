################################################################################
# Set minimum required version of cmake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 3.5)
project(nobleans_playground)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

################################################################################
# Find ament packages and libraries for ament and system dependencies
################################################################################
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

################################################################################
# Generate interfaces
################################################################################
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/SpawnProto.srv"
)

################################################################################
# Install
################################################################################
install(
  DIRECTORY
    launch
    worlds
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS
    controllers/spawner/spawner.py
  DESTINATION lib/${PROJECT_NAME}
)

################################################################################
# Macro for ament package
################################################################################

ament_export_dependencies(rosidl_default_runtime)
ament_package()
