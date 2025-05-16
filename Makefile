LIB_RS_PATH := operations/lib.rs
LIB_NAME := operations
OUTPUT_DIR := .
OPERATIONS_FILES := $(wildcard operations/*.rs)

ifeq ($(OS),Windows_NT)
    LIB_EXTENSION := dll
    TARGET := x86_64-pc-windows-gnu # Or your preferred Windows target
else ifeq ($(shell uname -s),Darwin)
    LIB_EXTENSION := dylib
    TARGET := x86_64-apple-darwin # Or your preferred Darwin target
else
    LIB_EXTENSION := so
    TARGET := x86_64-unknown-linux-gnu # Or your preferred Linux target
endif

OUTPUT_LIB := $(OUTPUT_DIR)/lib$(LIB_NAME).$(LIB_EXTENSION)

all: $(OUTPUT_LIB)

$(OUTPUT_LIB): $(LIB_RS_PATH) $(OPERATIONS_FILES)
	rustc --crate-type cdylib -C incremental=operations/build --target $(TARGET) -o $@ $<

clean:
	rm -f $(OUTPUT_LIB)

.PHONY: all clean