class Graph():
    def __init__(self, num_edge, vertices):
        self.vertex = [None]
        self.num_edge = num_edge
        for num in range(num_edge):
            self.vertex.append([])
        self.createGraph(vertices)

    def createGraph(self, vertices):
        for vertex in vertices:
            self.vertex[vertex[0]].append(vertex[1])
            self.vertex[vertex[1]].append(vertex[0])

    def shortestNodes(self):
        dist = [float('inf')] * (self.num_edge + 1)
        q = [(1, 0)]
        while len(q) > 0:
            (cur, depth) = q.pop(0)
            if depth < dist[cur]:
                dist[cur] = depth
                for edge in self.vertex[cur]:
                    q.append((edge, depth + 1))
        dist = [x for x in dist if x < float('inf')]
        print(dist)
        max_dist = max(dist)
        dist = list(filter(lambda x: x == max_dist, dist))
        return len(dist)


def solution(n, edge):
    g = Graph(n, edge)
    return g.shortestNodes()
