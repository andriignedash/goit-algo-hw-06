import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Завдання 1: Створення та візуалізація графу

# Створення графу
G = nx.Graph()

# Додавання вершин (перехресть)
G.add_nodes_from(range(1, 11))

# Додавання ребер (доріг)
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 5), (5, 7), (6, 8), (7, 9), (8, 10), (9, 10)]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа міста")
plt.savefig('graph.png')  # Зберегти граф як зображення
plt.close()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
avg_degree = sum(degrees.values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Середній ступінь вершини: {avg_degree:.2f}")

# Завдання 2: Реалізація та порівняння алгоритмів DFS і BFS

def dfs(graph, start, path=[]):
    path.append(start)
    for neighbor in graph[start]:
        if neighbor not in path:
            path = dfs(graph, neighbor, path)
    return path

def bfs(graph, start):
    queue = [start]
    path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path.append(vertex)
            queue.extend(set(graph[vertex]) - set(path))
    return path

# Використання алгоритмів на нашому графі
graph_dict = nx.to_dict_of_lists(G)
start_node = 1

dfs_path = dfs(graph_dict, start_node)
bfs_path = bfs(graph_dict, start_node)

print(f"Шлях DFS: {dfs_path}")
print(f"Шлях BFS: {bfs_path}")

# Завдання 3: Алгоритм Дейкстри для знаходження найкоротшого шляху

# Додавання ваг до ребер
weights = {
    (1, 2): 4, (1, 3): 2, (2, 4): 5, (2, 5): 10, (3, 6): 3,
    (4, 5): 2, (5, 7): 3, (6, 8): 6, (7, 9): 1, (8, 10): 8, (9, 10): 7
}
nx.set_edge_attributes(G, weights, 'weight')

# Реалізація алгоритму Дейкстри
shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
shortest_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

print(f"Найкоротші шляхи від вершини {start_node}: {shortest_paths[start_node]}")
print(f"Довжини найкоротших шляхів від вершини {start_node}: {shortest_lengths[start_node]}")
