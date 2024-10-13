import turtle as turta
import re

#Setting global values for pixel size and grid orientation.
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(2000)
    turta.penup()
    turta.goto(-PIXEL_SIZE * (COLUMNS+0.5) / 2, PIXEL_SIZE * ROWS / 2) # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)
    
#The below function returns the color from the given color-code string. 
def get_color(color_code):
    colors = ['black', 'white', 'red', 'yellow','orange','green','yellowgreen','sienna','tan', 'gray','darkgray']
    
    
    try:
        if color_code.upper() == 'A':     #checks if the color code is A and assigns value, otherwise value is linked to index position in list.
            return colors[-1]
        return colors[int(color_code)]
    
    except:
        return None
        
#Draws a square shaped pixel of desired pixel length
def draw_color_pixel(color_string, turta):
    
        

    turta.fillcolor(get_color(color_string))
    turta.pendown()
    turta.begin_fill()
    turta.right(90)
    turta.forward(PIXEL_SIZE)
    turta.right(90)
    turta.forward(PIXEL_SIZE)
    turta.right(90)
    turta.forward(PIXEL_SIZE)
    turta.right(90)
    turta.forward(PIXEL_SIZE)
    turta.end_fill()
    turta.penup()

#draws a line from given sequence of string.
def draw_line_from_string(color_string, turta):
    
    for i in color_string:
        if get_color(i) == None:                #if getcolor() returns None, ie. color code does not exist, prints invalid entry and returns ValueError (used later)
            print("Invalid Entry")
            return ValueError
        
        else:
            draw_color_pixel(i, turta)                  #draws square and then aligns to position for next pixel
            turta.penup()
            turta.forward(PIXEL_SIZE)
            turta.pendown()
            
    turta.penup()                                                   #Alings position for next row.
    turta.left(180)
    turta.forward((len(color_string)+1)*PIXEL_SIZE)
    turta.left(90)
    turta.forward(PIXEL_SIZE)
    turta.left(90)
    turta.forward(PIXEL_SIZE)
    return True
            
#asks user for input of color coded strings and draws the rows.
def draw_shape_from_string(turta):
    
    while True:
        
        
        
        in_string = input("Enter the string of color codes: ")
        if in_string == '':                                         #checks if empty string is entered
            print("Invalid string entered.")
            break
        
        elif re.findall(r"[b-zB-Z \W]+", in_string) != []:              #using re module to check whether string given contains any character that is non numeric and not A
            print("Invalid string entered.")
            break
            
        else:
            draw_line_from_string(in_string, turta)
                
#draws the black and red grid mentioned in part 2        
def draw_grid(turta):
    grid_line = '02020202020202020202'
    grid_line_inverse = '20202020202020202020'
    
    
    for i in range(20):
        if i % 2 == 0:
            draw_line_from_string(grid_line, turta)
            
        else:
            draw_line_from_string(grid_line_inverse, turta)
        
#reads a file for eahc line of color coded strings, strips each line and draws pixels accordingly
def draw_shape_from_file(turta):
    f = input("Enter the name of the text file you want to use for the drawing: ")
    
    try:
        with open(f) as rfile:
            for i in rfile:
                
                draw_line_from_string(i.strip(),turta)
                
    except FileNotFoundError:                           #exception to catch file not found error
        print("file not found!")
        
