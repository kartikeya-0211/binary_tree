from collections import deque, defaultdict

class BFS:
    @staticmethod
    def adj(edges, n):
        ans = defaultdict(list)
        for u, v in edges:
            ans[u].append(v)
            ans[v].append(u)
        return ans

    @staticmethod
    def bfs(adj, start, n):
        visited = [False] * n
        queue = deque()

        visited[start] = True
        queue.append(start)

        print(f"BFS Traversal starting from node {start}: ", end="")
        while queue:
            node = queue.popleft()
            print(f"{node} ", end="")

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

    @staticmethod
    def main():
        edges = [
            [0, 1],
            [0, 2],
            [1, 2],
            [1, 3]
        ]

        n = 4

        adjacency_list = BFS.adj(edges, n)

        print("Adjacency List:")
        for i in range(n):
            print(f"{i}: ", end="")
            # Sort the neighbors for consistent output, similar to Java's default List iteration
            for v in sorted(adjacency_list[i]):
                print(f"{v} ", end="")
            print()

        BFS.bfs(adjacency_list, 0, n)

if __name__ == "__main__":
    BFS.main()
