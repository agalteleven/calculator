#include <iostream>
#include <cstdint>
using namespace std;

extern "C"
{
	void hello()
	{
		cout << "Hello, World from C++!" << endl;
	}

	uint64_t fibonaci(int n)
	{
		uint64_t previous[2] = {1, 1};
		for (int i = 2; i < n; i++)
		{
			uint64_t temp = previous[1];
			previous[1] = previous[0] + previous[1];
			previous[0] = temp;
		}
		return previous[1];
	}
}