cmake_minimum_required(VERSION 3.16)
project(Operations VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)

# Define source files for the library
file(GLOB_RECURSE OPERATIONS_SOURCES
  "src/*.cpp"
)
file(GLOB_RECURSE OPERATIONS_HEADERS
  "src/*.hpp"
)

# Create the dynamic library
add_library(${PROJECT_NAME} SHARED
  ${OPERATIONS_SOURCES}
  ${OPERATIONS_HEADERS} # Headers are included for IDE awareness
)

# Set output directory for the library (optional)
set_target_properties(${PROJECT_NAME} PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR} # Output to the project's build directory
  OUTPUT_NAME "operations" # Ensure the output name is "operations" without the "lib" prefix
)