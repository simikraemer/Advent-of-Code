from itertools import combinations

def aufgabe1(lines):
    connections = [line.split('-') for line in lines]
    graph = {}
    for a, b in connections:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    triangles = []
    for node in graph:
        neighbors = graph[node]
        for a, b in combinations(neighbors, 2):
            if a in graph[b]:
                triangles.append(set([node, a, b]))

    unique_triangles = {frozenset(triangle) for triangle in triangles}

    triangles_with_t = [triangle for triangle in unique_triangles if any(node.startswith('t') for node in triangle)]

    return len(triangles_with_t)

def aufgabe2(lines):
    connections = [line.split('-') for line in lines]
    graph = {}
    for a, b in connections:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    def bron_kerbosch(r, p, x):
        if not p and not x:
            cliques.append(r)
            return
        for v in list(p):
            bron_kerbosch(r.union({v}), p.intersection(graph[v]), x.intersection(graph[v]))
            p.remove(v)
            x.add(v)

    cliques = []
    nodes = set(graph.keys())
    bron_kerbosch(set(), nodes, set())
    largest_clique = max(cliques, key=len)
    password = ",".join(sorted(largest_clique))

    return password

with open("2024/input/23.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

print("Aufgabe 1:", aufgabe1(lines))
print("Aufgabe 2:", aufgabe2(lines))
