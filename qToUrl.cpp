/*
Query = word1 word2 (in general field)
Url = https://scholar.google.co.in/scholar?hl=en&q=word1+word2
Query = word1 word2 (in author)
Url = https://scholar.google.co.in/scholar?as_q=&hl=en&as_sauthors=word1+word2

What the code is doing: accept a file called queryNames in cin and output urls in a file called queryUrls

To compile: g++ qToUrl.cpp
To run: ./a.out < queryNames > queryUrls
*/

#include <iostream>
#include <string>
using namespace std;
int main()
{
    string line;
    if(!cin.eof())
    {
        getline(cin,line);
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
        while(line.find("++") && line.find("++")<line.length())
        {
            c=line.find("++");
            line.erase(c,1);
        }
        cout << "https://scholar.google.co.in/scholar?hl=en&q=" << line;
        while(!cin.eof())
        {
            getline(cin,line);
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
            while(line.find("++") && line.find("++")<line.length())
            {
                c=line.find("++");
                line.erase(c,1);
            }
            cout << endl << "https://scholar.google.co.in/scholar?hl=en&q=" << line;
        }
    }
}