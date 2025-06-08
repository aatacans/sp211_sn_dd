# sp211_sn_dd

A minimal Python package for computing shortest paths (Dijkstra).

## Install

```bash
pip install sp211-sn-dd


from sp211_sn_dd.shortest_path import shortest_path

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": []
}
dist, path = shortest_path(graph, "A", "D")
print(dist)  # 4
print(path)  # ['A', 'B', 'C', 'D']


git clone https://github.com/aatacans/sp211_sn_dd.git
cd sp211_sn_dd
pip install -e .[dev]
pytest
g