#outlier data can be extracted from boxplot
#finding the mean
import numpy
from scipy import stats
speed=[23,455,55,43,44,33,22,112,22,22,22]
x=numpy.mean(speed)
print(x)
#median
speed=[23,455,55,43,44,33,22,112,22,22,22]
x=numpy.median(speed)
print(x)
#mode
speed=[23,455,55,43,44,33,22,112,22,22,22]
x=stats.mode(speed)
print(x)
#standard deviation
speed=[23,455,55,43,44,33,22,112,22,22,22]
x=numpy.std(speed)
print(x)
speed=[23,455,55,43,44,33,22,112,22,22,22]
x=numpy.var(speed)
print(x)
#percentile
speed=[23,455,55,43,44,33,22,112,22,22,22]
x=numpy.percentile(speed,75)
print(x)
