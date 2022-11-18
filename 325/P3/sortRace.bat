./generate 1000000 100000 999999
time sort numbers.txt > sorted.txt
time ./mySortA numbers.txt  sortedA.txt
time ./mySortV numbers.txt  sortedV.txt
time ./mySort  numbers.txt  sortedM.txt