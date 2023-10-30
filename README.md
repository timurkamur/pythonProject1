# pythonProject1
timurkamur/pythonProject1

# City Grid Tower Placement

This project focuses on the optimization of tower placements within a city grid to ensure maximum coverage with the minimum number of towers. The city grid can have obstructed blocks where towers can't be placed.

## Features

- **City Grid Generation**: Create a grid representation of a city with random obstructions.
- **Tower Placement**: Efficiently place towers to maximize coverage.
- **Path Reliability**: Determine the most reliable path between two towers based on the number of hops.
- **Visualization**: Visualize the city grid, tower placements, and data paths.

## Installation

```bash
git clone https://github.com/yourusername/citygrid-tower-placement.git
cd citygrid-tower-placement
pip install -r requirements.txt
```

## Usage

```python
from citygrid import CityGrid

# Create a 20x20 city grid
city = CityGrid(20, 20)

# Optimize tower placement with a coverage radius of 5
city.optimize_tower_placement(R=5)

# Visualize the grid
city.visualize()

# Find the most reliable path between two towers
tower_start = city.towers[0]
tower_end = city.towers[-1]
path = city.dijkstra(tower_start, tower_end)
print(path)
```

## Dependencies

- numpy
- matplotlib

## License

This project is licensed under the MIT License.

## Author

[timurkamur]([https://github.com/yourusername](https://github.com/timurkamur))
