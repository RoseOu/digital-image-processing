#coding:utf-8

import math
import numpy
from PIL import Image


def scale(input_img, size):
    output_width = size[0]
    output_height = size[1]
    output_array = [[ 0 for i in range(output_width)] for j in range(output_height)]
    input_width = input_img.size[0]
    input_height = input_img.size[1]
    input_array = numpy.asarray(input_img)
    for i in range(output_height):
        for j in range(output_width):
            x0 = (i+0.5) / output_height * input_height - 0.5
            y0 = (j+0.5) / output_width * input_width - 0.5

            x1 = int(x0)
            y1 = int(y0)

            u = x0 - x1
            v = y0 - y1

            #prevent to cross the border
            if (x1+1) >= input_height:
                x1 = input_height - 1 - 1
            if (y1+1) >= input_width:
                y1 = input_width - 1 - 1


            output_array[i][j] = (1-u)*(1-v)*int(input_array[x1][y1]) + (1-u)*v*int(input_array[x1][y1+1]) + u*(1-v)*int(input_array[x1+1][y1]) + u*v*int(input_array[x1+1][y1+1])
    output_img = Image.fromarray(numpy.uint8(output_array))
    return output_img


def main():
    input_img = Image.open('11.png')
    print("Input width:")
    width = int(input());
    print("Input height:")
    height = int(input());
    size = (width,height)
    output_img = scale(input_img,size)
    output_img.save("11o.png",'png')

if __name__ == "__main__":
	main()