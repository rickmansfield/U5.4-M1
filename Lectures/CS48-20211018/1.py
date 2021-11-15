# Vertex Class
class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return f"[{self.value}] connections: {[connection.value for connection in self.connections]}"

    def __repr__(self):
        return f"{[connection.value for connection in self.connections]}"

    def add_connection(self, vert, weight=0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]


# Graph Class
class Graph:

    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        self.count += 1
        return new_vert

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
        return self.vertices.keys()


g = Graph()
g.add_vertex(10)
g.add_vertex(20)
g.add_vertex(30)
g.add_edge(10, 40)
g.add_edge(40, 10)
g.add_edge(340, 560)
g.add_edge(340, 20)
print(g.vertices)
