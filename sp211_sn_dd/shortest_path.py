import heapq

def shortest_path(graph, start, end):
    """
    graph: dict[node, list[(neighbor, weight)]]
    start: başlangıç düğümü
    end: bitiş düğümü
    return: (en kısa mesafe, yol listesi) veya (None, None) eğer yol yoksa
    """
    # Önce tüm dist değerlerini sonsuz yap, start için 0
    dist = {node: float('inf') for node in graph}
    prev = {}  # önceki düğüm kaydı
    dist[start] = 0

    # (mesafe, düğüm) biçiminde öncelik kuyruğu
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == end:
            break
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))

    # Hedefe ulaşılıp ulaşılmadığını kontrol et
    if dist.get(end, float('inf')) == float('inf'):
        return None, None

    # Yol bilgisini reconstruct et
    path = []
    node = end
    while node != start:
        path.append(node)
        node = prev[node]
    path.append(start)
    path.reverse()

    return dist[end], path
