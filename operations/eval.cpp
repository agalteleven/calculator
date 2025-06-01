#include <gmpxx.h>
#include <string>
#include <cstdint>
#include <cctype>
#include <iostream> // for std::cerr

using namespace std;

mpz_class parse_expr(const string &input, uint64_t &pos);
mpz_class parse_term(const string &input, uint64_t &pos);
mpz_class parse_factor(const string &input, uint64_t &pos);

extern "C"
{
	const char *eval(const char *input)
	{
		uint64_t pos = 0;
		string input_str(input);

		try
		{
			mpz_class output = parse_expr(input_str, pos);

			// Store output string in static buffer to keep pointer valid
			static thread_local string output_str;
			output_str = output.get_str();

			return output_str.c_str();
		}
		catch (const std::exception &e)
		{
			cerr << "eval error: " << e.what() << endl;
			static thread_local string error_str;
			error_str = string("Error: ") + e.what();
			return error_str.c_str();
		}
		catch (...)
		{
			cerr << "eval unknown error" << endl;
			static thread_local string error_str;
			error_str = "Unknown error";
			return error_str.c_str();
		}
	}
}

mpz_class parse_expr(const string &input, uint64_t &pos)
{
	mpz_class left = parse_term(input, pos);

	while (pos < input.size())
	{
		char op = input[pos];
		if (op != '+' && op != '-')
			break;

		pos++; // consume operator
		mpz_class right = parse_term(input, pos);

		if (op == '+')
			left += right;
		else
			left -= right;
	}

	return left;
}

mpz_class parse_term(const string &input, uint64_t &pos)
{
	mpz_class left = parse_factor(input, pos);

	while (pos < input.size())
	{
		char op = input[pos];
		if (op != '*' && op != '/')
			break;

		pos++; // consume operator
		mpz_class right = parse_factor(input, pos);

		if (op == '*')
			left *= right;
		else
			left /= right;
	}

	return left;
}

mpz_class parse_factor(const string &input, uint64_t &pos)
{
	if (pos >= input.size())
	{
		cerr << "parse_factor error: unexpected end of input" << endl;
		return mpz_class(0);
	}

	char thing = input[pos];
	mpz_class output;

	if (thing == '(')
	{
		pos++; // consume '('
		output = parse_expr(input, pos);

		if (pos >= input.size() || input[pos] != ')')
		{
			cerr << "parse_factor error: no closing parenthesis" << endl;
			return mpz_class(0);
		}
		pos++; // consume ')'
	}
	else if (isdigit(thing) || thing == '-')
	{
		string buffer1;
		buffer1 += thing;
		pos++;
		while (pos < input.size() && isdigit(input[pos]))
		{
			buffer1 += input[pos];
			pos++;
		}
		output = buffer1;
	}
	else
	{
		cerr << "parse_factor error: invalid character: " << thing << endl;
		return mpz_class(0);
	}

	return output;
}
