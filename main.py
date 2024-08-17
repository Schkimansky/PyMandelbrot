import numpy as np
from PIL import Image

ITERATIONS = 80
xmin, xmax, ymin, ymax = -2.5, 1.5, -2.0, 2.0


def mandelbrot(c) -> int:
    z = complex(0.0, 0.0)

    for i in range(ITERATIONS):
        if abs(z) > 2.0:
            return i
        z = (z * z) + c

    return 0


def color(i):
    r = (i * 2) % 255
    g = (i * 1) % 255
    b = (i * 5) % 255
    return r, g, b


def main():
    width = 512
    height = 512

    image = np.zeros((width, height, 3), dtype=np.uint8)

    for x in range(width):
        for y in range(height):
            c = complex(xmin + (x / width) * (xmax - xmin),
                        ymin + (y / height) * (ymax - ymin))
            i = mandelbrot(c)
            image[x, y] = color(i)

    Image.fromarray(image).save('mandelbrot.png')


if __name__ == '__main__':
    main()
