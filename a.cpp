#include "bits/stdc++.h" // includes all libraries
#include <chrono> // high res time
#include <thread>
#include <unistd.h>

using namespace std::chrono;
using namespace std;
// using namespace std::chrono_literals;

int main() {
    // string s = "as";
    int i = 10;
    int count = 0;
    // string v;
    const string s1 = "timeout 8 ./scholar.py -dd --cookie-file cookie.txt --txt-globals --author \"";
    const string s2 = "\" | grep \'\\[G\\]\' | grep Results &";
    high_resolution_clock::time_point t1 = high_resolution_clock::now();

    vector<string> v;
    while(i--) {
        string ssss;
        getline(cin, ssss);
        v.push_back(ssss);
    }
    while(1) {
        cerr << "run\n"; // prints error reports on the terminal
        system((s1+v[count%10]+s2).c_str()); // prints the string in the form of c characters on the terminal
        cerr << s1+v[count%10]+s2 << '\n';
        unsigned w_t = rand()%7 + 13;
        cerr << "wait" << w_t << "\n";
        sleep(w_t); // sleep is like a delay
        auto duration = duration_cast<seconds>( high_resolution_clock::now() - t1 ).count();
        cerr << duration<< ")count = " << count++ << endl;
        cout << duration<< ")count = " << count << endl;
    }
}


