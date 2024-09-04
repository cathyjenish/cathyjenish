import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Polygon
from classes.Obstacle import Obstacle


class Utils:
    def isWall(self, obs):
        all_points = []

        if hasattr(obs, "allCords"):
            all_points.extend(obs.allCords)

        if hasattr(obs, "vertices"):
            all_points.extend(obs.vertices)

        if not all_points:
            return False  # If there are no points, it's not a wall or a rectangle

        x = [item[0] for item in all_points]
        y = [item[1] for item in all_points]
        if len(np.unique(x)) < 2 or len(np.unique(y)) < 2:
            return True  # Wall
        else:
            return False  # Rectangle

    def drawMap(self, obs, curr, dest):
        fig = plt.figure()
        currentAxis = plt.gca()
        utils = Utils()
        for ob in obs:
            if isinstance(ob, Obstacle):
                if utils.isWall(ob):
                    x, y = zip(*ob.vertices)
                    currentAxis.add_patch(
                        Polygon(
                            ob.vertices, closed=True, edgecolor="red", facecolor="none"
                        )
                    )
                else:
                    currentAxis.add_patch(Polygon(ob.vertices, closed=True, alpha=0.4))

            else:
                if self.isWall(ob):
                    x_1 = [item[0] for item in ob.vertices]
                    y_1 = [item[1] for item in ob.vertices]
                    plt.scatter(x_1, y_1, c="blue")
                    plt.plot(x_1, y_1)

                else:
                    currentAxis.add_patch(
                        Polygon(
                            ob.vertices,
                            alpha=0.4,
                        ),
                    )
        plt.scatter(curr[0], curr[1], s=200, c="green")
        plt.scatter(dest[0], dest[1], s=200, c="green")
        fig.canvas.draw()
