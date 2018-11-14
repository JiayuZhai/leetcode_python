class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        :ref:https://leetcode.com/problems/bus-routes/discuss/122771/C%2B%2BJavaPython-BFS-Solution
        """
        to_routes = collections.defaultdict(set)
        for i,route in enumerate(routes):
            for j in route: to_routes[j].add(i)
        bfs = [(S,0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T: return bus
            for route_i in to_routes[stop]:
                for next_stop in routes[route_i]:
                    if next_stop not in seen:
                        bfs.append((next_stop, bus+1))
                        seen.add(next_stop)
                routes[route_i] = []
        return -1
