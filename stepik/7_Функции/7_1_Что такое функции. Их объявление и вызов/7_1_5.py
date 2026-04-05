def show_numbers(width, height):
    x = 2*width + 2*height
    print(f'Периметр прямоугольника, равен {x}')


w, h = map(int, input().split())
show_numbers(w, h)