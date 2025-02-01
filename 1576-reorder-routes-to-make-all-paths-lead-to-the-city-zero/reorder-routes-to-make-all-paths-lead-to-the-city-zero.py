class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # road from a to b
            graph[b].append((a, 0))  # road from b to a
        
        def dfs(city, visited):
            visited.add(city)
            count = 0
            for neighbor, change in graph[city]:
                if neighbor not in visited:
                    count += change
                    count += dfs(neighbor, visited)
            return count
        
        return dfs(0, set())
