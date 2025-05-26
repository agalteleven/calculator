#include <iostream>
#include <cstdint>
#include <cmath>
#include <gmpxx.h>
using namespace std;

extern "C"
{
	void hello()
	{
		cout << "Hello, World from C++!" << endl;
	}

	const char *fibonaci(int n)
	{
		static std::string result; // persists between calls
		mpz_class a = 1, b = 1;
		for (int i = 2; i < n; i++)
		{
			mpz_class temp = b;
			b = a + b;
			a = temp;
		}
		result = b.get_str();
		return result.c_str();
	}

	bool is_prime(uint64_t n)
	{
		if (n < 2)
		{
			return false;
		}
		for (uint64_t i = 2; i < (static_cast<uint64_t>(sqrt(n)) + 1); i++)
		{
			if ((n % i) == 0)
			{
				return false;
			}
		}
		return true;
	}

	int mandelbrot(double real, double imag, int max_iterations)
	{
		double z_real = 0.0, z_imag = 0.0;
		for (int i = 0; i < max_iterations; i++)
		{
			// z = z*z + c
			double z_real_sq = z_real * z_real, z_imag_sq = z_imag * z_imag;
			if (z_real_sq + z_imag_sq > 4.0)
			{
				return i;
			}
			z_imag = 2 * z_real * z_imag + imag;
			z_real = z_real_sq - z_imag_sq + real;
		}
		return max_iterations;
	}
}