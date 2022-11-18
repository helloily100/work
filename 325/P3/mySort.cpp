#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
  
void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
  
int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; 
    int i = (low-1); 
  
    for (int j = low; j <= high-1; j++) {
        if (arr[j] < pivot) {
            i++; 
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[high]);
    return (i+1);
}
  

void quickSort(int arr[], int low, int high)
{
    if (low < high) {
        int p = partition(arr, low, high);
        quickSort(arr, low, p-1);
        quickSort(arr, p+1, high);
    }
}
  
  
int main(int argc, char* argv[])
{
    if (argc < 3)
	{
		cout << "Please include input filename and output filename in param list.\n";
		cout << "Example:\n";
		cout << "     % mySort numbers.txt mySorted.txt\n";
		exit(EXIT_SUCCESS);
	}

    const int MAX = 1000000;
  	ofstream fout;
	ifstream fin;
	int n;
	
	int v[MAX];
	int count = 0;

    fin.open(argv[1]);
    while (fin >> n )
	{
		v[count++] = n;	// insert a number into the arary and increase the index
	}
    quickSort(v,0,MAX);	// call the quickSort function

        fout.open(argv[2], ios::out | ios::trunc);
        for (int i = 0; i < count; i++)
		fout << v[i]<<endl;


        fout.close();
	    fin.close();
        return 0;
}