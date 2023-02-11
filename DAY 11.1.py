###COURSE,PAYMENT ARE PACKAGES WHILE COURSE_DETAILS AND PAYMENT_DETAILS ARE MODULES
###So our problem statemnt is we have to access other packages modules in some other packages modules
###Like i want to access my payment_detail file in course_detail file and vice versa

import os , sys
from os.path import dirname, join , abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))

###This above three lines are always necessay to write to inform my system that how my packages and modules are structure
#After that it will create pycache file as a symbol

#from payment import payment_details

def course():

    print("This is my course file")

#payment_details.payment()

#Finally i am able to track my payment function from module payment_details of package payemnt from course_details file

#Now to do same vice versa thing in my payment_details file i have to first comment out that one imp line because then i will 
#get circular error
