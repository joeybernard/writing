import recipy
import numpy

arr = numpy.arange(10)
arr = arr + 500

numpy.save('test.npy', arr)

