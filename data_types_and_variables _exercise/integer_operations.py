import math
from math import floor

first_numb = int(input())
second_numb = int(input())
third_numb = int(input())
fourth_numb = int(input())

sum = first_numb + second_numb
separated_numb = floor(sum/third_numb)
final_numb = separated_numb * fourth_numb
print(final_numb)