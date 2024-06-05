import turtle
import math

ANGLE = 45
LENGTH = 100

# Функція рекурсивного малювання дерева
def draw_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)

    turtle.right(ANGLE)
    draw_tree(branch_length * math.cos(math.radians(ANGLE)), level - 1)

    turtle.left(2 * ANGLE)
    draw_tree(branch_length * math.cos(math.radians(ANGLE)), level - 1)

    turtle.right(ANGLE)
    turtle.backward(branch_length)

# Ініціалізація
def main():
    level = int(input("Введіть рівень рекурсії: "))

    turtle.speed(0)  
    turtle.left(90)  
    turtle.up()
    turtle.backward(LENGTH * 1.5)
    turtle.down()
    
    draw_tree(LENGTH, level)
    
    turtle.done()

if __name__ == '__main__':
    main()
