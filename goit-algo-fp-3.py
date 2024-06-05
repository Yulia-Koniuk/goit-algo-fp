import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Ініціалізуємо бінарну купу (піраміду)
    heap = [(0, start)]
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

# Приклад графу у вигляді словника: вершина -> {сусід: вага}
graph = {
    'A': {'B': 5, 'D': 9, 'E': 2},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'D': 3},
    'D': {'A': 9, 'C': 3, 'E': 2, 'F': 2},
    'E': {'A': 2, 'D': 2, 'F': 3},
    'F': {'D': 2, 'E': 3, 'G': 2},
    'G': {'F': 2}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

print("Найкоротші відстані від вершини", start_vertex, "до інших вершин:")
for vertex, distance in shortest_distances.items():
    print("Вершина:", vertex, "- Відстань:", distance)
