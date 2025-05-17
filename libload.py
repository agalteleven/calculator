import os
import sys
import cffi

def load_operations_lib_simple(directory="."):
    """
    Loads the 'operations' library using cffi, making function calls
    directly as attributes of the returned library object.

    Args:
        directory (str, optional): The directory where the library is located.
                                     Defaults to the current directory.

    Returns:
        object or None: The loaded library object with functions accessible
                        as attributes if successful, None otherwise.
    """
    lib_name = "operations"
    lib_path = None
    ffi = cffi.FFI()

    if sys.platform.startswith("win"):
        lib_filename = f"lib{lib_name}.dll"
    elif sys.platform.startswith("linux"):
        lib_filename = f"lib{lib_name}.so"
    elif sys.platform.startswith("darwin"):
        lib_filename = f"lib{lib_name}.dylib"
    else:
        print(f"Unsupported operating system: {sys.platform}")
        return None

    potential_path = os.path.join(directory, lib_filename)
    if os.path.exists(potential_path):
        try:
            lib = ffi.dlopen(potential_path)
            print(f"Successfully loaded library (cffi simple): {potential_path}")
            # Declare the signature of the 'hello_rust' function
            ffi.cdef("void hello_rust();")
            return lib
        except OSError as e:
            print(f"Error loading library at {potential_path} (cffi simple): {e}")
            return None
    else:
        print(f"Library not found at: {potential_path}")
        return None

if __name__ == "__main__":
    lib = load_operations_lib_simple()
    if lib:
        try:
            # Call the 'hello_rust' function directly as an attribute
            lib.hello_rust()
            print("Rust function 'hello_rust' executed (no return value).")

        except Exception as e:
            print(f"Error interacting with the library (cffi simple): {e}")
    else:
        print("Failed to load the operations library (cffi simple).")