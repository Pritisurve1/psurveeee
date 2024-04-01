#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(0)); // the random number generator
    int secretNumber = rand() % 100 + 1; // Generate a random number between 1 and 100
    int guess;
    int attempts = 0;

    cout << "Welcome to the Number Guessing Game!" << endl;

    do {
        cout << "Enter your guess (between 1 and 100): ";
        cin >> guess;
        attempts++;

        if (guess > secretNumber) {
            cout << "IT's Too high! Try again." << endl;
        } else if (guess < secretNumber) {
            cout << "IT's Too low! Try again." << endl;
        } else {
            cout << "Congratulations! You guessed the number in " << attempts << " attempts." << endl;
        }
    } while (guess != secretNumber);

    return 0;
}
