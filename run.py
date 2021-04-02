import matplotlib.pyplot as p
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    p.style.use('classic')
    # Numbers for color map
    point_numbers = range(rw.num_points)
    # Plot random walk data
    fig, ax = p.subplots(figsize=(15,9), dpi=96)

    im = ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=p.cm.Blues,
        edgecolors='none', s = 10)

    # Plot beginning and end points
    ax.scatter(0, 0, c='green', edgecolors='none', s = 50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    p.colorbar(im, ax=ax)
    p.show()

    keep_going = input("Generate another walk? (y/n): ").lower()
    if (keep_going == 'n'):
        break