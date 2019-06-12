#! /usr/bin/env python3

from math import cos
from math import pi
from datetime import datetime
import temp
import heat

class c:
	pass
conf = c()
conf.temp_max = 25
conf.temp_min = 15

def main():
	adjust_heat()

def adjust_heat():
	t = temp.measure()
	print("Measured temp is %d" %t)
	hour = get_current_hour()
	ideal_temp = get_ideal_temp(hour)
	print("Ideal temp is %d" % ideal_temp)
	diff = ideal_temp - t
	if diff > 0:
		heat.increase(diff)
		print("increasing temperature (diff %d)" % diff)
	else:
		heat.decrease(diff)
		print("decreasing temperature (diff %d)" % diff)

def get_ideal_temp(h):
	tmax = conf.temp_max
	tmin = conf.temp_min
	p = 24
	m = (tmax + tmin) / 2
	a = (tmax - tmin) / 2
	return -a*cos(2*pi/p*h)+m

def get_current_hour():
	now = datetime.now()
	return now.hour

if __name__ == '__main__':
	main()