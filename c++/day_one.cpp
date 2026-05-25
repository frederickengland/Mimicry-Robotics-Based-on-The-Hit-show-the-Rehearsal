#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
// .\day_one.exe
//  g++ -o day_one.exe day_one.cpp
class MIMICRY
{
public:
    struct DICT
    {
        std::vector<std::string> good_words;
        std::vector<std::string> bad_words;

        std::vector<std::string> questions =
        {
            "Tell me about yourself.",
            "What's one of your weaknesses?",
            "What's one of your strengths?",
            "What's your greatest achievement?",
            "Where do you see yourself in 5 years?"
        };
    };
};

MIMICRY::DICT array;

void loadwords(const std::string& filename,
               std::vector<std::string>& container)
{
    std::ifstream file(filename);

    if (!file)
    {
        std::cout << "Could not open " << filename << "\n";
        return;
    }

    std::string word;

    while (file >> word)
    {
        container.push_back(word);
    }
}

bool contains(const std::vector<std::string>& vec,
              const std::string& word)
{
    return std::find(vec.begin(), vec.end(), word) != vec.end();
}

int scoreanswer(const std::string& answer,
                const std::vector<std::string>& good_words,
                const std::vector<std::string>& bad_words)
{
    int score = 0;

    std::stringstream ss(answer);
    std::string word;

    while (ss >> word)
    {
        // lowercase conversion
        std::transform(word.begin(), word.end(),
                       word.begin(), ::tolower);

        if (contains(good_words, word))
        {
            score++;
        }

        if (contains(bad_words, word))
        {
            score--;
        }
    }

    return score;
}

int main()
{
    loadwords("good_words.txt", array.good_words);
    loadwords("bad_words.txt", array.bad_words);

    int totalscore = 0;

    for (const auto& question : array.questions)
    {
        std::cout << question << "\n";

        std::string answer;
        std::getline(std::cin, answer);

        int score = scoreanswer(
            answer,
            array.good_words,
            array.bad_words
        );

        totalscore += score;

        std::cout << "Answer score: "
                  << score << "\n\n";
    }

    std::cout << "Final interview score: "
              << totalscore << "\n";

    if (totalscore > 5)
    {
        std::cout << "Excellent interview\n";
    }
    else if (totalscore > 0)
    {
        std::cout << "Decent interview\n";
    }
    else
    {
        std::cout << "Poor interview\n";
    }

    return 0;
}