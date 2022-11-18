// filename: matrix2.cpp
// compile line: %c++ matrix2.cpp -o matrix2 -pthread
#include <string>
#include <thread> // include the thread library
#include <iostream>
using namespace std;
// Internal
// this is the function that is called by each thread
void print_message(string quote)
{
cout << quote<<endl;
}


string quote[4] = {"I","know","kung","fu"};

int main()
{
 // create 2 threads. threads launch a process upon creation
 // pass the function name and all parameters.
 // In this case, a function name and string
 thread thread0(print_message,quote[0]);
 thread thread1(print_message,quote[1]);
 thread thread2(print_message,quote[2]);
 thread thread3(print_message,quote[3]);

 // force the threads to join back to the main program
 thread0.join();
 thread1.join();
 thread2.join();
 thread3.join();

 return 0;
}