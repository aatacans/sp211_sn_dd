from sp211_sn_dd.shortest_path import shortest_path

def test_trivial():
    graph = {'A': [('B', 1)], 'B': []}
    dist, path = shortest_path(graph, 'A', 'B')
    assert dist == 1
    assert path == ['A', 'B']
