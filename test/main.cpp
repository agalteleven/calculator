#include <iostream>
#include "libload.h"
#include <cstdint>
#include "bindings.hpp"
using namespace std;

int main()
{
	const char *lib_path = "liboperations.dll";

	lib_handle_t lib = getlib(lib_path);
	if (!lib)
	{
		return 1;
	}

	hello();

	cout << "10th in fibonacci sequence is: " << fibonaci(75) << endl;

	freelib(lib);
	return 0;
}