#include <boost/graph/use_mpi.hpp>
#include <boost/graph/distributed/delta_stepping_shortest_paths.hpp>
#include <iostream>

int main(int argc, char *argv[])
{
    std::cout << boost::graph::distributed::delta_stepping_shortest_paths << std::endl;
    return 0;
}
