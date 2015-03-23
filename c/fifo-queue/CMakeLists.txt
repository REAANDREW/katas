cmake_minimum_required (VERSION 2.8)
project (Fifo)
include_directories("./include")
add_executable(Fifo main.c src/queue.c)
