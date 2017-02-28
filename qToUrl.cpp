/*
Query = word1 word2 (in general field)
Url = https://scholar.google.co.in/scholar?hl=en&q=word1+word2
Query = word1 word2 (in author)
Url = https://scholar.google.co.in/scholar?as_q=&hl=en&as_sauthors=word1+word2

I accept a file called queryNames in cin and output urls in a file called queryUrls

To compile: g++ qToUrl.cpp
To run: ./a.out < queryNames > queryUrls
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    int i = 10; // number of query terms
    string s;
    while(i--) {
        s="";
        getline(cin, s);
        int c = 0;
        while(s[c]!='\0')
        {
            if(s[c]==' ')
                s[c]='+';
            c++;
        }
        cout << "https://scholar.google.co.in/scholar?hl=en&q=" << s << endl; 
    }
}