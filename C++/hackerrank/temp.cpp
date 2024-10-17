

#include <iostream>
#include <vector>
using namespace std;


struct test {
    int a;
    string b;
} temp;

class temp_class{
    public:
    temp_class(){
        cout<<"constructor"<<endl;
    }
    private:
    temp_class(int a){
        cout<<"constructor"<<endl;
    }
    protected:
    temp_class(int a, int b){
        cout<<"constructor"<<endl;
    }

    ~temp_class(){
    cout<<"destructor"<<endl;
};

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

test return_sum(int a, int b){
    test *obj = new test();
    obj->a = 10;
    obj->b = "20";

    float c = 0;
    c = a+b;
    string yos = "yoseph";
    return *obj;
}
