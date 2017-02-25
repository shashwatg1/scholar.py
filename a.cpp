#include "bits/stdc++.h" // includes all libraries
#include <chrono> // high res time
#include <thread>
#include <unistd.h>

using namespace std::chrono;
using namespace std;
// using namespace std::chrono_literals;

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::shared_ptr<FILE> pipe(popen(cmd, "r"), pclose);
    if (!pipe) throw std::runtime_error("popen() failed!");
    while (!feof(pipe.get())) {
        if (fgets(buffer.data(), 128, pipe.get()) != NULL)
            result += buffer.data();
    }
    return result;
}

bool chk_status(const char* cmd) {
    string  s = exec(cmd);
    auto st = s.find("Results ");
    stringstream ss;
    int x;
    if (st!= string::npos) {
        ss << s.substr (st);
        string temp;
        ss >> temp >> x;
    } else return 1;
    return (x > 0);
}
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
    int zeros = 0;
    while(1) {
        cerr << "run\n"; // prints error reports on the terminal
        if (!chk_status((s1+v[count%10]+s2).c_str())) { // prints the string in the form of c characters on the terminal
            cout << zeros++ << ' ';
            // exit(0);
        } else zeros = 0;
        if (zeros == 3) {
            cout << "Done q = " << count << "Time = " << (duration_cast<seconds>( high_resolution_clock::now() - t1 ).count())/60 << "mins\n";
            cerr << "Done q = " << count << "Time = " << (duration_cast<seconds>( high_resolution_clock::now() - t1 ).count())/60 << "mins\n";
            exit(0);
        }

        cerr << s1+v[count%10]+s2 << '\n';
        unsigned w_t = rand()%7 + 13;
        cerr << "wait" << w_t << "\n";
        sleep(w_t); // sleep is like a delay
        auto duration = duration_cast<seconds>( high_resolution_clock::now() - t1 ).count();
        cerr << duration<< ")count = " << count++ << endl;
        cout << duration<< ")count = " << count << endl;
    }
    assert(0);

}


