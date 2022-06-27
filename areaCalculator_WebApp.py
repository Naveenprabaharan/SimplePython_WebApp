from pywebio.input import input, FLOAT
from pywebio.output import put_text

def area():
    radius = input("Enter Radius(mm)：", type=FLOAT)
    

    area = 3.14 * (radius**2)

    

  
    put_text('AREA OF CIRCLE: %.3f' % (area))
    

if __name__ == '__main__':
    area()