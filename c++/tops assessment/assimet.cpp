#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class game
{
public:
    int round, user_point = 0, computer_point = 0, draw = 0;
    char user_choice, computer_choice;
    char array[3] = {'s', 'p', 'r'};
    void getdata()
    {
        cout << "Enter Number Of round You want to play: ";
        cin >> round;
    }
    void getanswer()
    {
        cout << "Enter your Choice: " << endl;
        cout << "r-Rock\ns-scissor\np-paper " << endl;
        cin >> user_choice;
        int ch = rand() % 2;
        computer_choice = array[ch];
        cout << "Computer choice= " << computer_choice << endl;
    }
    void play()
    {
        for (int i = 1; i <= round; i++)
        {
            cout << "--------ROund" << i << "-----------------" << endl;
            getanswer();
            if (user_choice == 'r' && computer_choice == 'p')
            {
                computer_point++;
                cout << "Computer Wins" << endl;
            }
            else if (user_choice == 'p' && computer_choice == 's')
            {
                computer_point++;
                cout << "Computer Wins" << endl;
            }
            else if (user_choice == 's' && computer_choice == 'r')
            {
                computer_point++;
                cout << "Computer Wins" << endl;
            }
            else if (user_choice == 'p' && computer_choice == 'r')
            {
                user_point++;
                cout << "User Wins" << endl;
            }
            else if (user_choice == 's' && computer_choice == 'p')
            {
                user_point++;
                cout << "User Wins" << endl;
            }
            else if (user_choice == 'r' && computer_choice == 's')
            {
                user_point++;
                cout << "User Wins" << endl;
            }
            else
            {
                draw++;
                cout << "Draw" << endl;
            }
        }
    }
    void winner()
    {
        if (user_point > computer_point)
        {
            cout << "******USer IS winner********" << endl;
        }
        else if (computer_point > user_point)
        {
            cout << "******Computer IS winner********" << endl;
        }
        else
        {
            cout << "********DRAW*******" << endl;
        }
    }
    void showdata()
    {
        cout << "User Point = " << user_point << endl;
        cout << "computer Point = " << computer_point << endl;
        cout << "Draw = " << draw << endl;
    }
};
int main()
{
    game g1;
    g1.getdata();
    g1.play();
    g1.showdata();
    g1.winner();
    return 0;
}