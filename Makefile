# the compiler: gcc for C program, define as g++ for C++
CC = g++
 
# compiler flags:
#  -g     - this flag adds debugging information to the executable file
#  -Wall  - this flag is used to turn on most compiler warnings
CFLAGS  = -g -Wall -std=c++17
 
# The build target 
TARGET = Main.cpp
NAME = Matura
 
main: 
	$(CC) $(CFLAGS) Main.cpp class/File.cpp -o $(NAME)

clean:
	$(RM) $(NAME)