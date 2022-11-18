#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <thread>
#include <unistd.h>
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
        if (arr[j] <= pivot) {
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

// int* split(int arr[], int start, int end)
// {
//     int temp[125000 + 1];
//     for(int i = start; i < end; i++)
//     {
//         temp[i] = arr[i];
//     }
//     return temp;
// }
// int* merge(int first[], int second[], int size)
// {
//     int temp[size *  2 + 1];
//     int i = 0, j = 0, k = 0;
//     while (i < size)
//     {
//         temp[k++] = first[i++];
//     }
//     while (j < size)
//     {
//         temp[k++] = second[j++];
//     }
//     quickSort(temp,0,size*2);
//     return temp;
// }
  

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
    const int THREAD_MAAX = 125000;
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

    
    // int arr1[THREAD_MAAX];
    // for (int i = 0; i < THREAD_MAAX; i++)
    // {
    //     arr1[i] = v[i];
    // }
    //  int arr2[THREAD_MAAX];
    // for (int i = THREAD_MAAX; i < THREAD_MAAX * 2; i++)
    // {
    //     arr2[i] = v[i];
    // }
    // int arr3[];
    // int arr4[];
    // int arr5[];
    // int arr6[];
    // int arr7[];
    // int arr8[];

    thread thread0(quickSort,v,0,THREAD_MAAX);
    thread thread1(quickSort,v,THREAD_MAAX,THREAD_MAAX*2);
    thread thread2(quickSort,v,THREAD_MAAX*2,THREAD_MAAX*3);
    thread thread3(quickSort,v,THREAD_MAAX*3,THREAD_MAAX*4);
    thread thread4(quickSort,v,THREAD_MAAX*4,THREAD_MAAX*5);
    thread thread5(quickSort,v,THREAD_MAAX*5,THREAD_MAAX*6);
    thread thread6(quickSort,v,THREAD_MAAX*6,THREAD_MAAX*7);
    thread thread7(quickSort,v,THREAD_MAAX*7,MAX);

    thread0.join();
    thread1.join();
    thread2.join();
    thread3.join();
    thread4.join();
    thread5.join();
    thread6.join();
    thread7.join();



    fout.open(argv[2], ios::out | ios::trunc);
    for (int i = 0; i < MAX; i++)
    fout << v[i] <<endl;

    fout.close();
    fin.close();
    return 0;
}