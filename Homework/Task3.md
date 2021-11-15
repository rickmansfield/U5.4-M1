# Unit 5.4 M1 Task 1
![image](/assets/Task3.jpg)

## Question
- Choose the python code that correctly represent the graph shown in the picture using an adjacentcy list.

## Solution
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