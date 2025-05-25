ifeq ($(OS),Windows_NT)
    export LIB_EXTENSION := dll
    export EXE_EXTENSION := .exe # Or your preferred Windows target
else ifeq ($(shell uname -s),Darwin)
    export LIB_EXTENSION := dylib
    export EXE_EXTENSION := 
else
    export LIB_EXTENSION := so
    export EXE_EXTENSION := 
endif
export OPERATIONS_LIB_NAME = liboperations.$(LIB_EXTENSION)

all:
	tup

.PHONY: all