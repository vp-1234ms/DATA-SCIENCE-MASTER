import os , sys
from os.path import dirname, join , abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))


from course import course_detail

def payment():
    print("This is my payment file")


course_detail.course()

#Finally i am able to track my course function from module course_detail of course payemnt from payemnt_details file
