from collections import defaultdict

from helpers.input import int_array_from_list


class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.G = defaultdict(list)

    def addEdge(self, u, v):
        self.G[u].append(v)

    def count_all_paths(self, s, d, visited, count):
        visited[s] = True
        if s == d:
            count[0] += 1
            print(count)
        else:
            for i in self.G[s]:
                if visited[i] == False:
                    self.count_all_paths(i, d, visited, count)
        visited[s] = False

    def get_degrees(self):
        return [len(self.G[v]) for v in self.G]


def part1(data):
    """Finds a chain that uses all adapters to connect the charging outlet
    to your device's built-in adapter and count the joltage differences between
    the charging outlet, the adapters, and your device. Returns the number of
    1-jolt differences multiplied by the number of 3-jolt differences.

    Args:
        data ([int]): List of integer ratings of joltage adaptors.
    """
    data.sort()
    one = 0
    three = 1
    for i in range(0, len(data)):
        if i == 0:
            diff = data[i] - 0
        else:
            diff = data[i] - data[i - 1]
        if diff == 1:
            one += 1
        if diff == 3:
            three += 1
        i += 1
    return one * three


def part2(data):
    """Return the count of all valid combinations of adaptor
    from 0 (s) to 3 jolts higher than the highest rated adaptor (t).
    Constructs a DAG from s to t and counts the valid paths
    through the graph.

    Args:
        data ([int]): List of integer ratings of joltage adaptors.
    """
    data.sort()
    data.insert(0, 0)
    device_rating = data[-1] + 3
    data.append(device_rating)
    graph = Graph(len(data))
    for i in range(0, len(data) - 1):
        j = i + 1
        while j < len(data) and (data[j] - data[i]) <= 3:
            graph.addEdge(data[i], data[j])
            j += 1

    # visited = defaultdict(bool)
    # for i in data:
    #     visited[i] = False
    # count = [0]
    # graph.count_all_paths(0, device_rating, visited, count)
    # return count[0]

    degs = graph.get_degrees()
    i = len(degs) - 2
    while i >= 0:
        paths = 0
        j = 1
        while j <= degs[i]:
            paths += degs[i + j]
            j += 1
        degs[i] = paths
        i -= 1
    return degs[0]


if __name__ == "__main__":
    data = int_array_from_list("10.txt")
    print(part1(data))
    print(part2(data))
