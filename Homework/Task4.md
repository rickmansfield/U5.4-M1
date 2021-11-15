# Unit 5.4 M1 Task 4

## Question
- Givent the following __Vertext__ and __Graph__ classes, 
- choose the python code that would correctly create the graph pictured below:
  
![image](/assets/AdjacencyList.jpg)

```python
  class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return f"[{self.value}] connections: {[x.value for x in self.connections]}"

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
```
## Solution
![image](/assets/Task4.jpg)