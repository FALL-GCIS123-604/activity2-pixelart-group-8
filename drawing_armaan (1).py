import turtle
import re
import pixart_armaan


#runs the function to draw shape from entered text file.

def main():
    pixart_armaan.initialization(turtle)
    pixart_armaan.draw_shape_from_file(turtle)
    input()
    

if __name__ == "__main__":
    main()


    
