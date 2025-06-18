from collections import defaultdict

class GraphAdjacencyList:
    @staticmethod
    def build_adj_list(pairs):
        adj_list = defaultdict(list)

        for u, v in pairs:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        return adj_list

    @staticmethod
    def main():
        pairs = [
            [0, 1],
            [0, 2],
            [1, 2],
            [2, 3]
        ]

        adj_list = GraphAdjacencyList.build_adj_list(pairs)

        for node in sorted(adj_list.keys()):  # Sorting for consistent output order
            print(f"{node} -> {adj_list[node]}", end="")
            if node < max(adj_list.keys()):
                print("") # New line character 

if __name__ == "__main__":
    GraphAdjacencyList.main()
