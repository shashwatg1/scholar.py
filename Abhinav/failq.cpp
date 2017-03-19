#include "bits/stdc++.h"

using namespace std;

int main(int argc, char *argv[]) {
	ifstream ql(argv[1]);
	ifstream qacc(argv[2]);
	set<string> acc;
	int deb = 0;
	while (!qacc.eof()) {
		string s, s2("");
		qacc >> s;
		int i;
		for (i = s.length()-1; i > -1; --i)
			if (s[i] == '/')
				break;
		while(i++ != s.length()-1)
			s2 += s[i];
		acc.insert(s2);
		// cout << s2 << '\n';
	}
	// cerr << 
	cerr << "----------------\n";
	deb = 0;
	while (!ql.eof()) {
		string s;
		string s2;
		getline(ql, s);
		for (int i = 0; i < s.length(); ++i)
			if (s[i] != ' ')
				s2 += s[i];
		if (acc.find(s2) == acc.end()) { // not accepted
			// cerr << s2 << " :not found\n";
			cout << s << '\n';
		// if (deb++ == 10)
		// 	break;
		}

	}

}