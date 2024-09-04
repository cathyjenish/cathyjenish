import numpy as np


class Obstacle:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.calcFullCord()

    def printFullCords(self):
        print(self.topLeft, self.topRight, self.bottomLeft, self.bottomRight)

    def calcFullCord(self):
        otherP1 = [self.topLeft[0], self.bottomRight[1]]
        otherP2 = [self.bottomRight[0], self.topLeft[1]]

        points = [self.topLeft, otherP1, otherP2, self.bottomRight]

        # Finding correct coords and what part of rectangle they represent - we can't always assume we receive the top left and bottomRight
        x = [item[0] for item in points]
        y = [item[1] for item in points]

        minX = np.min(x)
        minY = np.min(y)

        maxX = np.max(x)
        maxY = np.max(y)

        self.topRight = np.array([maxX, maxY])
        self.bottomLeft = np.array([minX, minY])

        self.topLeft = np.array([minX, maxY])
        self.bottomRight = np.array([maxX, minY])

        self.allCords = [self.topLeft, self.topRight, self.bottomLeft, self.bottomRight]

        self.width = self.topRight[0] - self.topLeft[0]
        self.height = self.topRight[1] - self.bottomRight[1]


class Obstacle2:
    def __init__(self, vertices):
        self.vertices = np.array(vertices)
        self.calculate_properties()
        self.calcFullCord()

    def calculate_properties(self):
        # Calculate additional properties of the polygon
        self.centroid = np.mean(self.vertices, axis=0)
        self.area = 0.5 * np.abs(
            np.dot(self.vertices[:, 0], np.roll(self.vertices[:, 1], 1))
            - np.dot(self.vertices[:, 1], np.roll(self.vertices[:, 0], 1))
        )
        # Other properties can be added based on your requirements

    def print_properties(self):
        print("Vertices:", self.vertices)
        print("Centroid:", self.centroid)
        print("Area:", self.area)

    def calcFullCord(self):
        if hasattr(self, "vertices"):
            # Irregular obstacle with vertices
            self.allCords = self.vertices.tolist() + [self.vertices[0].tolist()]
            x = [item[0] for item in self.vertices]
            y = [item[1] for item in self.vertices]

            minX = np.min(x)
            minY = np.min(y)

            maxX = np.max(x)
            maxY = np.max(y)

            self.topRight = np.array([maxX, maxY])
            self.bottomLeft = np.array([minX, minY])

            self.topLeft = np.array([minX, maxY])
            self.bottomRight = np.array([maxX, minY])

            self.allCords = self.vertices
        else:
            print("Invalid")
