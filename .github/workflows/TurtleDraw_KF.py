import turtle
import math

def main():
    screen = turtle.Screen()
    screen.setup(450, 450)
    screen.title("TurtleDraw_kf")
    
    t = turtle.Turtle()
    t.speed(0)
    
    filename = input("Enter filename: ")
    
    total_distance = 0.0
    prev_x = None
    prev_y = None
    first_point = True
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split()
                
                if parts[0] == 'stop':
                    t.penup()
                    prev_x = None
                    prev_y = None
                else:
                    color = parts[0]
                    x = int(parts[1])
                    y = int(parts[2])
                    
                    t.pencolor(color)
                    
                    if first_point:
                        t.penup()
                        t.goto(x, y)
                        t.pendown()
                        first_point = False
                    else:
                        if prev_x is not None:
                            distance = math.sqrt((x - prev_x)**2 + (y - prev_y)**2)
                            total_distance += distance
                        t.goto(x, y)
                    
                    prev_x = x
                    prev_y = y
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except ValueError as e:
        print(f"Error parsing file: {e}")
        return
    
    t.penup()
    t.goto(180, -200)
    t.write(f"Total distance: {total_distance:.2f}", align="right", font=("Arial", 12, "normal"))
    
    input("Press enter to exit")
    screen.bye()

if __name__ == "__main__":
    main()
“python3 TurtleDraw_KF.py”
