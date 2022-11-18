#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <thread>
#include <unistd.h>
using namespace std;

class qs
{
    public:
        int* c_arr;
        int c_low;
        int c_high;

        qs(int* arr, int low, int high)
        {
            c_arr = arr;
            c_low = low;
            c_high = high;
        }
};
  

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

void* qs_thread(void* qsObj)
{
    quickSort(((qs*)qsObj)-> c_arr, ((qs*)qsObj)-> c_low, ((qs*)qsObj)-> c_high);
    // delete ((qs*)qsObj);
    return nullptr;
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
    const int THREAD_MAX = 50;
  	ofstream fout;
	ifstream fin;
	int n;
	
	int v[MAX];
	int count = 0;

    pthread_t thread0, thread1, thread2, thread3, thread4, thread5, thread6, thread7;
    int iret0, iret1, iret2, iret3, iret4, iret5, iret6, iret7;

    fin.open(argv[1]);
    while (fin >> n )
	{
		v[count++] = n;	// insert a number into the arary and increase the index
	}


    iret0 = pthread_create(&thread0, NULL, qs_thread, new qs(&v[THREAD_MAX],0,THREAD_MAX));
    // iret1 = pthread_create(&thread1, NULL, qs_thread, new qs(&v[THREAD_MAX * 2],0,THREAD_MAX*2));
    // iret2 = pthread_create(&thread2, NULL, qs_thread, new qs(&v[THREAD_MAX * 3],0,THREAD_MAX*3));
    // iret3 = pthread_create(&thread3, NULL, qs_thread, new qs(&v[THREAD_MAX * 4],0,THREAD_MAX*4));
    // iret4 = pthread_create(&thread4, NULL, qs_thread, new qs(&v[THREAD_MAX * 5],0,THREAD_MAX*5));
    // iret5 = pthread_create(&thread5, NULL, qs_thread, new qs(&v[THREAD_MAX * 6],0,THREAD_MAX*6));
    // iret6 = pthread_create(&thread6, NULL, qs_thread, new qs(&v[THREAD_MAX * 7],0,THREAD_MAX*7));
    // iret7 = pthread_create(&thread7, NULL, qs_thread, new qs(&v[THREAD_MAX * 8],0,THREAD_MAX*8));
    // cout << iret0 << iret1 << iret2 << iret3 << iret4 << iret5 << iret6 << iret7 << endl;
    
    fout.open(argv[2], ios::out | ios::trunc);
    for (int i = 0; i < MAX; i++)
    fout << v[i]<<endl;

    fout.close();
    fin.close();
    return 0;
}