import time

a = range(1000000)
c = []
starttime = time.clock()
for b in a:
    c.append(b*b)
endtime = time.clock()
print "Total time used: " , (endtime-starttime)

