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
int main()
{
    string line;
    ifstream myfile("queryNames"); // input file
    ofstream myfileO("queryUrls"); // output file
    if(myfile.is_open() && !myfile.eof())
    {
        getline(myfile,line);
        int c=0;
        int l=line.length();
        while(c<l)
        {
            while(!(((line[c]>='A')&&(line[c]<='Z'))||((line[c]>='a')&&(line[c]<='z'))))
            {
                if(line[c]==' ' || line[c]=='\0')
                    break;
                line.erase(c,1);
                l--;
            }
            if(line[c]==' ')
                line[c]='+';
            if(line[c]=='\0')
                    break;
            c++;
        }
        myfileO << "https://scholar.google.co.in/scholar?hl=en&q=" << line;
        while(!myfile.eof())
        {
            getline(myfile,line);
            int c=0;
            int l=line.length();
            while(c<l)
            {
                while(!(((line[c]>='A')&&(line[c]<='Z'))||((line[c]>='a')&&(line[c]<='z'))))
                {
                    if(line[c]==' ' || line[c]=='\0')
                        break;
                    line.erase(c,1);
                    l--;
                }
                if(line[c]==' ')
                    line[c]='+';
                if(line[c]=='\0')
                    break;
                c++;
            }
            myfileO << endl << "https://scholar.google.co.in/scholar?hl=en&q=" << line;
        }
        myfile.close();
        myfileO.close();
    }
}