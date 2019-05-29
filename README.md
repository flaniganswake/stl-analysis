# STL File Analysis

## Code Structure

The code structure consists of class objects for a Surface (Mesh) and its
Facets. There is a helper namedtuple object for Point for the vertices. The STL
filename is loaded as a command line argument. **./stl_analyzer.py Moon.stl**
The file is opened and parsed loading each facet into the surface. The parsing
has a simple validation check assuming the file is somewhat well-formed. Once
the file has been completely parsed - we are ready to get some metrics. I also
built a file using stl-numpy which is much faster, more efficient and extendable.
**./stl_mesh.py Moon.stl**

## Metrics

* The number of triangles in the model is determined by counting the facets once
the surface is completely loaded.
* The surface area of the model is found by summing the individual areas of all
the facets (triangles). The facet areas are determined by using Heron's formula.
The lengths of the edges can be found by calculating the distances between the
vertices. These side lengths are then used to determine the triangle area.
* The bounding box of the model is found by determining the min/max differences
for each of the x, y, z directions. These  vertices are the corners of the
minimum rectangular box containing the model/surface.


## Optimizations

Since the density of the facets varies according to the needs of the modeling
STL files can become quite large when considering machining tolerance. The
efficiency and speed for large STL files can be increased by using numpy-stl
implementions using better data structures for loading the mesh. Also the use of 
binary STL files would help. This can be improved even more by running in native
code instead with some multi-processing. Splitting the files and using different 
quality settings for distinct regions of the model can also improve performance.