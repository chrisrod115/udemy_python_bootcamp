import math

def coverage_calc(height,width,coverage):

    
    avg_num_of_cans = (int(height)*int(width)) / coverage
    total_num = math.ceil(avg_num_of_cans)
    print(f"You will need {total_num} paint cans to cover a width of {width} x height {height}\n")
    
coverage_num = 5
test_h = int(input("What is the height? "))
test_w = int(input("What is the width? "))
coverage_calc(height= test_h,width= test_w,coverage=coverage_num)




