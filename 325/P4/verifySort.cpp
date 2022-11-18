#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <thread>
#include <unistd.h>
#include <algorithm>
using namespace std;

bool verify(int arr[], int length)
{
    if(is_sorted(arr, arr + length))
    {
        return true;
    }
    return false;
}

int main(int argc, char* argv[])
{
    if (argc < 2)
	{
		cout << "Please include input filename and output filename in param list.\n";
		cout << "Example:\n";
		cout << "     % verifySort mySort.txt\n";
		exit(EXIT_SUCCESS);
	}
    const int MAX = 1000000;
	ifstream fin;
	int n;
	
	int v[MAX];
	int count = 0;

    fin.open(argv[1]);
    while (fin >> n )
	{
		v[count++] = n;	// insert a number into the arary and increase the index
	}
        
    if (verify(v,MAX))
    {
        cout << "Sorted" << endl;
    }
    else
    {
        cout << "Not Sorted" << endl;
    }

    fin.close();
    return 0;
}