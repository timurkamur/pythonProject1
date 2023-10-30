import matplotlib
matplotlib.use('Agg')
import numpy as np
import random
import matplotlib.pyplot as plt


class CityGrid:
    def __init__(self, N, M, obstruction_rate=0.3):
        self.N = N
        self.M = M
        self.grid = np.zeros((N, M))
        self.towers = []

        # Расставляем препятствия
        num_obstructions = int(N * M * obstruction_rate)
        for _ in range(num_obstructions):
            x, y = random.randint(0, N - 1), random.randint(0, M - 1)
            while self.grid[x][y] == -1:  # проверяем, что не попали на уже существующее препятствие
                x, y = random.randint(0, N - 1), random.randint(0, M - 1)
            self.grid[x][y] = -1  # -1 означает препятствие

    def optimize_tower_placement(self, R):
        while np.any(self.grid == 0):  # пока есть непокрытые блоки
            max_coverage = 0
            best_position = None

            for x in range(self.N):
                for y in range(self.M):
                    if self.grid[x][y] != -1:  # если не препятствие
                        # подсчет потенциального покрытия для текущей позиции
                        coverage = sum([1 for i in range(max(0, x - R), min(self.N, x + R + 1))
                                        for j in range(max(0, y - R), min(self.M, y + R + 1))
                                        if self.grid[i][j] == 0])

                        if coverage > max_coverage:
                            max_coverage = coverage
                            best_position = (x, y)

            if best_position:
                self.place_tower(best_position[0], best_position[1], R)
            else:
                break

    def place_tower(self, x, y, R):
        if self.grid[x][y] == -1:
            print("Невозможно разместить башню на препятствии!")
            return
        self.towers.append((x, y, R))
        for i in range(max(0, x - R), min(self.N, x + R + 1)):
            for j in range(max(0, y - R), min(self.M, y + R + 1)):
                if self.grid[i][j] != -1:
                    self.grid[i][j] = 1  # 1 означает покрытие башни

    def dijkstra(self, start, end):
        distance = {tower: float('infinity') for tower in self.towers}
        previous_vertices = {tower: None for tower in self.towers}
        distance[start] = 0
        vertices = self.towers.copy()

        while vertices:
            current_vertex = min(vertices, key=lambda tower: distance[tower])
            vertices.remove(current_vertex)
            if distance[current_vertex] == float('infinity'):
                break
            for neighbour, cost in self.get_neighbours(current_vertex):
                alternative_route = distance[current_vertex] + cost
                if alternative_route < distance[neighbour]:
                    distance[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = [], end
        while previous_vertices[current_vertex] is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.append(start)
        return path[::-1]

    def get_neighbours(self, current_vertex):
        neighbours = []
        x, y, R = current_vertex
        for tower in self.towers:
            tx, ty, _ = tower
            if tower != current_vertex and abs(tx - x) <= R and abs(ty - y) <= R:
                neighbours.append((tower, 1))  # cost is 1 for each hop
        return neighbours

    def visualize(self, save_path="city_grid.png"):
        plt.imshow(self.grid, cmap='gray')
        for tower in self.towers:
            plt.plot(tower[1], tower[0], 'ro')  # башни отмечены красным
        plt.savefig(save_path)
        plt.close()


# Пример использования:
city = CityGrid(20, 20)
R = 5 # радиус
city.optimize_tower_placement(R)
city.visualize()
tower_start = city.towers[0]
tower_end = city.towers[-1]
path = city.dijkstra(tower_start, tower_end)
print(path)

