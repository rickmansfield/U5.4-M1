# Unit 5.4 M1 Graphs I 10/18/2021
## [CoLab Link](https://colab.research.google.com/drive/1lFl_30IdaFz_F9KqXSmi-sEArW60lZ8S?usp=sharing#scrollTo=F_L5EjH5J38N)
 ## [Video Link](https://www.youtube.com/watch?v=n2vDA6QNLW0)
You have been working with graphs all this time but you might have called them...

- Linked Lists
- Trees
- Binary Search Trees

All of those are forms of graphs. Think of graphs as the overarching category that encompasses a multitude of sub data structures such as Lists, Trees, Heaps and more...

## Directed Vs Undirected
**Directed**
- Twitter Follow
- You Follow an other Person

**Undirected / Bi Directional**
- Facebook Friendship
- You make friends with an other user, who is also then in turn your friend

## Cyclic Vs Acyclic
- cyclic graphs could model a route from home to work to school to home
- acyclic graph could model a routh where you just go either from home to work or from home to school

## Vertices and Edges
- a Vertex / Node would be an object to represent something like a User / Person / Student / Location
- a Edge / Connection could be a freindship / rivalry / follow / network connection / neighbor

## Weighted Vs Unweighted
- Weighted Edges contain some sort of value
- Unweighted does not contain any extra meta data

## Adjacency List and Adjacency Matrix
```
{
  "User1": ["User210", "User340", "User2"],
  "User2": ["User1"],
  "User210": ["User340", "User1"],
  "User340": ["User1", "User210"]
}


   0  1  2  3  4  5
[
 0[0, 1, 0, 1, 0, 1],
 1[1, 0, 0, 0, 1, 0],
 2[0, 0, 0, 1, 0, 0],
 3[1, 0, 1, 0, 0, 0],
 4[0, 1, 0, 0, 0, 0],
 5[1, 0, 0, 0, 0, 0]
 ]

 [[0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
```