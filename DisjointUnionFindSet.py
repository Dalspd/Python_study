class DisjointSetUnion:
    def __init__(self, n):
        self.rank = [1] * n  # 秩，在并查集树上的深度
        self.f = list(range(n))  # 根节点，初始化都指向自身

    def find(self, x: int) -> int:
        if self.f[x] == x:  # 如果本身是根节点就直接返回自身
            return x
        self.f[x] = self.find(self.f[x])  # 父节点设为根节点
        return self.f[x]  # 返回父节点（也就是根节点）

    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)  # 先找到两个根节点
        if fx == fy:  # 根节点相同则不需合并，已在同一个树内
            return False

        if self.rank[fx] < self.rank[fy]:  # 比较秩，保证深度大的作为合并的父节点
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]  # 合并秩
        self.f[fy] = fx  # 秩小的将秩大的作为父节点
        return True


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret


if __name__ == '__main__':
    sol = Solution()
    sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
