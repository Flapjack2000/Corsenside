#include <iostream>
#include <string>

bool checkPalindrome(std::string word);

int main()
{
	std::string word;

	while (true) {
		std::cout << "Enter a word, and I'll tell you if it's a palindrome: \n";
		std::getline(std::cin, word);
		std::cout << "\n" << checkPalindrome(word) << "\n";
	}
	return 0;
}

static bool checkPalindrome(std::string word)
{
	if (word.length() == 0)
	{
		return true;
	}
	else
	{
		if (word.at(0) == word.at(word.length() - 1))
		{
			return checkPalindrome(word.substr(1, word.length() - 2));
		}
		else 
		{
			return false;
		}
	}
}
