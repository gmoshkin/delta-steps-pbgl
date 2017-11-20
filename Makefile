all: bpgl_test.cpp
	clang++ -I/usr/include/mpi -std=c++11 -o bpgl_test -g $<
