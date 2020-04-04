# file: loader.py  local importer  Thu Mar 31
#     test import from script dir 
#def test():
#	print ("test success")
print( "Benign warning for pyganja:")
import time  #  for timing function calls
import datetime
import pyganja #; pyganja.__version__  AE 28-Mar
from   pyganja import GanjaScene, draw
from   numpy   import e, pi
from   scipy   import cos, sin
from   matplotlib import pyplot as plt
plt.ioff()  # plotting on request
from   mpl_toolkits.clifford import plot
import mpl_toolkits.clifford; mpl_toolkits.clifford.__version__

###  support functions
def startLapse():
    print ("start time : (wait=~12sec.)")
    now = datetime.datetime.now()
    # "%Y-%m-%d %H:%M:%S"
    print (now.strftime("%M:%S"))

    print("Start timer..(wait)", end='')
    start = time.time()
    return start

## create a wrapper for input and test
def inp():
    inp = input("Enter a number: ")
    return inp
    #end    
## create printing function primitives
def prn_2(s, n):
    #requires that s contain {}
    print( s.format(n) )
    #end
def prn_place_fmt_01(n):
    print("Total time: %.2f" % n, "seconds")
    #end
def prn_place_fmt_02(s,n):
    print("{} {:2.2f} seconds".format(s,n))

#  facade to Scene and .add_object
colors = {4:[255,0,0],     0:[0,0,0], 
          5:[0,255,0],     1:[128,0,0], 
          6:[0,0,255],     2:[0,128,0],
          7:[0,255,255],   3:[0,128,128] }    
def G(): # return class instance of Scene
    print("\nG()..", end='')
    g = GanjaScene();print("..done ");return g
def A(gs,o,c,label): # param Scene for add_object
    print("A()..", end='')
    gs.add_object(o,c,label)
    print("..done ", end='');return(gs)   

def draw_reflections(sc,sc_refl,circle,point,line,sphere):
    #  Authors' note:
    #  note that due to floating point rounding, 
    #  truncate back to a single grade here, with ``(grade)``
    #  REMOVED next because no ref to function
    # point_refl = homo((circle * point.gradeInvol() * ~circle)(1))
    line_refl = (circle * line.gradeInvol() * ~circle)(3)
    sphere_refl = (circle * sphere.gradeInvol() * ~circle)(4)
    #get normal of reflected line and sphere
    line_refN = line_refl.normal()
    sphere_refN = sphere_refl.normal()

    sc_refl = G() # no reflection of a circle?
    A(sc_refl, point_refl,  colors[1], label='point_refl')
    A(sc_refl, line_refN,   colors[2], label='line_refl')
    A(sc_refl, sphere_refN, colors[3], label='sphere_refl')

    draw(sc + sc_refl, scale=0.5) # end draw_reflections()

# call this explicitly
def load():
	print ("load()") #unused
	print("set import path..", end='')
	import os
	from sys import path
	b_PATHER = True
	# AE standard import dir
	strBASE = 'C:/AE/PY/MOD'
	def app_Path(p_path):
	    pather = path.append
	    pather      (p_path)
	    os.chdir    (p_path)
	if (b_PATHER):
	    app_Path    (strBASE)
	print("path: {}".format(strBASE))
	###  consts, timer module
print("..done. End of loader.")
# end of file.