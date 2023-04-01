import math

#defining the function

def paint_calc(height,width,cover) :
    area = height * width
    no_of_cans = area / cover
    total_no_of_cans = math.ceil(no_of_cans)
    print(f"Total number of cans required are {total_no_of_cans}")



#Giving the output

test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5

#Calling the function

paint_calc(height=test_h, width=test_w, cover=coverage)