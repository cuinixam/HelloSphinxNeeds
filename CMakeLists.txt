# cmake project definition
cmake_minimum_required(VERSION 3.22.0)

set(VARIANT ${FLAVOR}/${SUBSYSTEM} CACHE STRING "Variant to build.")
set(BUILD_KIT prod CACHE STRING "Target Group to build.")

include(${CMAKE_SOURCE_DIR}/variants/${VARIANT}/config.cmake)

project(${VARIANT} CXX C ASM)

# Fetch all extensions into modules directory
set(FETCHCONTENT_BASE_DIR ${CMAKE_SOURCE_DIR}/build/modules CACHE INTERNAL "")
include(FetchContent)

# Include spl-core
if(DEFINED ENV{SPLCORE_PATH})
    message(WARNING "SPLCORE_PATH defined! Use fixed SPL-CORE version from: $ENV{SPLCORE_PATH}")
    include($ENV{SPLCORE_PATH}/cmake/spl.cmake)
else()
    FetchContent_Declare(
        spl-core
        GIT_REPOSITORY https://github.com/avengineers/spl-core.git
        GIT_TAG develop
    )
    FetchContent_MakeAvailable(spl-core)

    include(${spl-core_SOURCE_DIR}/cmake/spl.cmake)
endif()

include(${CMAKE_SOURCE_DIR}/variants/${VARIANT}/parts.cmake)

# TODO: refactor/remove; we want to explicitly add includes where required
foreach(component_name ${COMPONENT_NAMES})
    target_include_directories(${component_name} PUBLIC ${target_include_directories__INCLUDES})
endforeach()
