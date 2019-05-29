#!/usr/bin/env python3
#
# Basic STL parser/analyzer using numpy-stl:
#
# print output:
# - The number of triangles in the model
# - The surface area of the model
# - The bounding box of the model
# email: flaniganswake@protonmail.com
#
from matplotlib import pyplot
from mpl_toolkits import mplot3d
import numpy
from stl import mesh
import sys


def find_dims(m: mesh) -> tuple:
    ''' find the max-min dimensions '''
    min_ = tuple(m.min_)
    max_ = tuple(m.max_)
    return (max_[0] - min_[0],
            max_[1] - min_[1],
            max_[2] - min_[2])


def find_bounds(m: mesh) -> tuple:
    ''' find vertices of bounding box '''
    X, Y, Z = find_dims(m)
    return ((0, 0, 0), (0, 0, Z), (0, Y, 0), (0, Y, Z),
            (X, 0, 0), (X, 0, Z), (X, Y, 0), (X, Y, Z))


def render(m: mesh) -> None:
    ''' render in 3D '''

    # create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m.vectors))

    # auto scale to the mesh size
    scale = numpy.concatenate([m.points]).flatten('F')
    axes.auto_scale_xyz(scale, scale, scale)

    # show the plot to the screen
    pyplot.show()


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1][-4:] == ".stl":
        file_ = sys.argv[1]
    else:
        print("format: stl_data <filename.stl>")
        sys.exit()

    mesh = mesh.Mesh.from_file(file_)
    print(f"Number of Triangles: {len(mesh.units)}")
    surface_area = "%.6f" % sum(a[0] for a in mesh.areas)
    print(f"Surface Area: {surface_area}")
    print(f"Bounding Box:")
    for vertex in find_bounds(mesh):
        print(f"{vertex}")
    render(mesh)

