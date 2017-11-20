namespace boost { namespace graph { namespace distributed {

template
<typename Graph, typename PredecessorMap, typename DistanceMap, typename WeightMap>
void delta_stepping_shortest_paths(const Graph& g,
                                   typename graph_traits<Graph>::vertex_descriptor s,
                                   PredecessorMap predecessor,
                                   DistanceMap distance,
                                   WeightMap weight,
                                   typename property_traits<WeightMap>::value_type delta)


template
<typename Graph, typename PredecessorMap, typename DistanceMap, typename WeightMap>
void delta_stepping_shortest_paths(const Graph& g,
                                   typename graph_traits<Graph>::vertex_descriptor s,
                                   PredecessorMap predecessor,
                                   DistanceMap distance,
                                   WeightMap weight)

} } }
