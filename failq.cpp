#include "bits/stdc++.h"

using namespace std;

int main(int argc, char *argv[]) {
	ifstream ql(argv[1]);
	ifstream qacc(argv[2]);
	map<string, bool> acc;
	int deb = 0;
	acc.clear();
	while (!qacc.eof()) {
		string s, s2("");
		qacc >> s;
		int i;
		for (i = s.length()-1; i > -1; --i)
			if (s[i] == '/')
				break;
		while(i++ != s.length()-1)
			s2 += s[i];
		acc[s2] = 1;
		// cout << s2 << '\n';
	}
	// cerr << 
	cerr << "----------------\n";
	deb = 0;
	cout << "acc: " << acc.size() << '\n';
	for (auto i: acc) {
		cout  << '#' << i.first.length()<< i.first << i.second << '#'<< ' ';
		for (auto j: i.first)
			cout << (int)j <<' ' << j << '\n';
	}
	cout << '\n';

	cerr << "----------------\n";
	while (!ql.eof()) {
		string s;
		string s2;
		getline(ql, s);
		for (int i = 0; i < s.length(); ++i) {
			if (s[i] != ' ') {
				s2 += s[i];
			}
		}
		cout << s2 << '\n';
		for (auto i: acc) {
			if (i.second == 1)
				if (s2 == i.first)
					cout << s << '\n';
				else cout << i.first.length() << i.first << ":not eq :" << s2 << s2.length() << ' ' << i.first.compare(s2) << '\n';
		}


	}

}