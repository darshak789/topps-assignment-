
#include <bits/stdc++.h>
using namespace std;

double averageRuns(int runs, int matches,
                   int notout)

{

    int out = matches - notout;

    if (out == 0)
        return -1;

    double avg = double(runs) / out;

    return avg;
}

int main()
{
    int runs = 10000;
    int matches = 250;
    int notout = 50;

    double avg = averageRuns(
        runs, matches, notout);

    if (avg == -1)
        cout << "NA";
    else
        cout << avg;

    return 0;
}
