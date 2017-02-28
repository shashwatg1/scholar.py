/*
Query = word1 word2 (in general field)
Url = https://scholar.google.co.in/scholar?hl=en&q=word1+word2
Query = word1 word2 (in author)
Url = https://scholar.google.co.in/scholar?as_q=&hl=en&as_sauthors=word1+word2

What the code is doing: read from a file called queryNames and output urls in a file called queryUrls

To compile: g++ qToUrl.cpp
To run: ./a.out
*/

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main() {
    string line;
    ifstream myfile("queryNames"); // input file
    ofstream myfileO("queryUrls"); // output file
    if(myfile.is_open() && !myfile.eof()) {
        getline(myfile,line);
        int c=0;
        while(line[c]!='\0')
        {
            if(line[c]==' ')
                line[c]='+';
            c++;
        }
        myfileO << "https://scholar.google.co.in/scholar?hl=en&q=" << line;
        while(!myfile.eof()) {
            getline(myfile,line);
            int c=0;
            while(line[c]!='\0')
            {
                if(line[c]==' ')
                    line[c]='+';
                c++;
            }
            myfileO << endl << "https://scholar.google.co.in/scholar?hl=en&q=" << line;
        }
        myfile.close();
        myfileO.close();
    }
}