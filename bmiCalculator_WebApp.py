from pywebio.input import input, FLOAT
from pywebio.output import put_text

def discountFinder():
    original_price = input("Enter Original Price(Rs)：", type=FLOAT)
    discount = input("Enter Discount(%)：", type=FLOAT)

    dis_price = original_price - (original_price * (discount / 100))

       
    put_text('Your Discounted price is: %.1f Rupees' % (dis_price))
            

if __name__ == '__main__':
    discountFinder()