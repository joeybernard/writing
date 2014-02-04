import numpy
import time
a = numpy.arange(10000000)
starttime = time.clock()
c = a * a
endtime = time.clock()
print "Total time used: ", (endtime - starttime)

