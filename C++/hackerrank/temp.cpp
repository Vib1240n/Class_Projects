#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

void fizzBuzz(int n) {
    for(int i =1; i <= n; i++){
        if(i%3 == 0 || i %5 ==0 ){
            cout << "Fizz" <<endl;
        }else if (i%3 == 0 && i % 5 ==0) {
            cout << "FizzBuzz" <<endl;
        }else{
            cout <<i<<endl;
        }
    }
}


int main(){
    vector<int> arr;
    arr.push_back(2);
    cout<< "print"<<endl;
      arr.push_back(3);
    arr.push_back(4);
    arr.push_back(5);
    cout<<arr.size()<<endl;
}