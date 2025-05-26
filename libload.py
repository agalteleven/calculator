import os
import sys
import ctypes

class LibWrapper:
    def __init__(self, library_path):
        self._lib = ctypes.CDLL(library_path)
        self._define_functions()

    def _define_functions(self):
        # hello: void hello()
        if hasattr(self._lib, "hello"):
            self.hello = self._lib.hello
            self.hello.restype = None
            self.hello.argtypes = []

        # fibonaci: const char *fibonaci(int n)
        if hasattr(self._lib, "fibonaci"):
            self.fibonaci = self._lib.fibonaci
            self.fibonaci.restype = ctypes.c_char_p
            self.fibonaci.argtypes = [ctypes.c_int]
            
        # is_prime: bool is_prime(uint64_t n)
        if hasattr(self._lib, "is_prime"):
            self.is_prime = self._lib.is_prime
            self.is_prime.restype = ctypes.c_bool
            self.is_prime.argtypes = [ctypes.c_uint64]
            
		# mandelbrot: int mandelbrot(double real, double imag, int max_iterations)
        if hasattr(self._lib, "mandelbrot"):
            self.mandelbrot = self._lib.mandelbrot
            self.mandelbrot.restype = ctypes.c_int
            self.mandelbrot.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]


class LibLoadModule:
    def __init__(self, directory="."):
        self.lib = self._load_library(directory)

    def _load_library(self, directory):
        lib_name = "operations"
        lib_filename = None

        if sys.platform.startswith("win"):
            lib_filename = f"lib{lib_name}.dll"
        elif sys.platform.startswith("linux"):
            lib_filename = f"lib{lib_name}.so"
        elif sys.platform.startswith("darwin"):
            lib_filename = f"lib{lib_name}.dylib"
        elif sys.platform.startswith("cygwin"):
            lib_filename = f"lib{lib_name}.dll"
        else:
            print(f"Unsupported operating system: {sys.platform}")
            return None

        potential_path = os.path.join(directory, lib_filename)
        if os.path.exists(potential_path):
            try:
                lib_wrapper = LibWrapper(potential_path)
                print(f"Successfully loaded library: {potential_path}")
                return lib_wrapper
            except OSError as e:
                print(f"Error loading library at {potential_path}: {e}")
                return None
        else:
            print(f"Library not found at: {potential_path}")
            return None

libload = LibLoadModule()
lib = libload.lib

if __name__ == "__main__":
    if lib:
        print("Operations library loaded successfully.")
        lib.hello()
        n = 10
        print(f"{n}th in fibonacci sequence is: {lib.fibonaci(n)}")
    else:
        print("Failed to load the operations library.")
