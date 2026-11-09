cmake_minimum_required(VERSION 3.16)
project(op_dromos_engine LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(PkgConfig QUIET)
if(PkgConfig_FOUND)
  pkg_check_modules(VALHALLA QUIET valhalla)
endif()

add_executable(route_engine
  src/main.cpp
  src/valhalla_client.cpp
)

target_include_directories(route_engine PRIVATE src)

if(VALHALLA_FOUND)
  target_compile_definitions(route_engine PRIVATE OP_DROMOS_VALHALLA_AVAILABLE=1)
  target_include_directories(route_engine PRIVATE ${VALHALLA_INCLUDE_DIRS})
  target_link_libraries(route_engine PRIVATE ${VALHALLA_LIBRARIES})
endif()
