#include <fstream>
#include <iostream>

using std::fstream;
using std::cout;
using std::endl;
using std::ios;

int main(int argc, char *argv[])
{
    if (argc < 2) {
        cout << "need file" << endl;
        return 0;
    }
    // open file
    fstream file(argv[1], ios::in | ios::binary);

    int vertices_count = 0;
    long long edges_count = 0;

    // read header
    file.read((char*)(&vertices_count), sizeof(int));
    file.read((char*)(&edges_count), sizeof(long long));

    // print graph
    cout << "Graph has " << vertices_count << " vertices" << endl;
    cout << "Graph has " << edges_count << " edges" << endl;

    // get & print graph data for WEIGHTED graph
    for(long long i = 0; i < edges_count; i++)
    {
        int src_id = 0, dst_id = 0;
        float weight = 0;

        // read i-th edge data
        file.read((char*)(&src_id), sizeof(int));
        file.read((char*)(&dst_id), sizeof(int));
        file.read((char*)(&weight), sizeof(float)); // remove it for unweighed graph

        //print edge data
        cout << src_id << " " << dst_id << " | " << weight << endl;
    }

    file.close();
}
