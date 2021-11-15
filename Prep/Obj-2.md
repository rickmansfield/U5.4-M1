# Unit 5.4 M1 Objective 2

Note remember to refer to the markdown preview of this file to see the picture. 
![image](/assets/GraphA.JPG)

1. Using the graph show in this picture, write python code to represen the graph in an adjacency list. 
```python
class Graph: 
    def _inti_(self):
        self.verticies = {
            "A": {"B": 1},
            "B": {"C": 3, "D": 2, "E": 1},
            "C": {"E": 4},
            "D": {"E": 2},
            "E": {"F": 3},
            "F": {},
            "G": {"D": 1},
        }

```

2. Using the same graph, write python code to represent the graph in an adjacency matrix. 
```python
class Graph:
    def _init_(self):
        self.edges = [
        [0, 1, 0, 0, 0, 0, 0]  
        [0, 0, 3, 2, 1, 0, 0],
        [0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        ]
```
the above graph is based on this matrix
```
    A B C D E F G 
A   0 0 0 0 0 0 0 
B   1 0 0 0 0 0 0
C   0 3 0 0 0 0 0 
D   0 2 0 0 0 0 1
E   0 1 4 2 0 0 0
F   0 0 0 0 3 0 0
G   0 0 0 0 0 0 0
```
refer to this resource image

![image](/assets/ExampleMatrix.JPG) ![image](/assets/ExampleMatrixGraph.JPG)

3. Write a paragraph that compares and contrasts the efficiency of your different representations. 








