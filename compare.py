from libload import lib
import time

width, height = 50, 50
max_iter = 20000
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

def mandelbrot_py(c_real, c_imag, max_iter):
    z_real, z_imag = 0.0, 0.0
    for i in range(max_iter):
        z_real_sq = z_real * z_real
        z_imag_sq = z_imag * z_imag
        if z_real_sq + z_imag_sq > 4.0:
            return i
        z_imag = 2 * z_real * z_imag + c_imag
        z_real = z_real_sq - z_imag_sq + c_real
    return max_iter

print("Starting full Mandelbrot grid performance test...\n")

# C++ mandelbrot timing and correctness check
start_cpp = time.perf_counter()
total_cpp = 0
for iy in range(height):
    c_imag = ymin + (ymax - ymin) * iy / (height - 1)
    for ix in range(width):
        c_real = xmin + (xmax - xmin) * ix / (width - 1)
        total_cpp += lib.mandelbrot(c_real, c_imag, max_iter)
end_cpp = time.perf_counter()

# Python mandelbrot timing and correctness check
start_py = time.perf_counter()
total_py = 0
for iy in range(height):
    c_imag = ymin + (ymax - ymin) * iy / (height - 1)
    for ix in range(width):
        c_real = xmin + (xmax - xmin) * ix / (width - 1)
        total_py += mandelbrot_py(c_real, c_imag, max_iter)
end_py = time.perf_counter()

match = "✓" if total_cpp == total_py else "✗"

print(f"Total iterations summed C++: {total_cpp}")
print(f"Total iterations summed Python: {total_py}")
print(f"Match: {match}")
print(f"C++ elapsed time: {end_cpp - start_cpp:.3f} seconds")
print(f"Python elapsed time: {end_py - start_py:.3f} seconds")
