# the compiler: gcc for C program, define as g++ for C++
CC = g++
 
# compiler flags:
#  -g         - this flag adds debugging information to the executable file
#  -Wall      - this flag is used to turn on most compiler warnings
# -std=c++17  - tells the compiler to use C++17
CFLAGS  = -g -Wall -std=c++17
 
# The build target
NAME = Matura
TARGET = Main.cpp
FCLASS = class/File.cpp
 
main: 
	$(CC) $(CFLAGS) $(TARGET) $(FCLASS) -o $(NAME)

clean:
	$(RM) $(NAME)