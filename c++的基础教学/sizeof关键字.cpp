# include <iostream>
using namespace std;

int main()
{
    short num1 = 10;
    int num2 = 10;
    long num3 = 10;
    long long num4 = 10;
    cout << "short所占的内存空间：" << sizeof(num1) << endl;
    cout << "int所占的内存空间：" << sizeof(num2) << endl;
    cout << "long所占的内存空间：" << sizeof(num3) << endl;
    cout << "long long所占的内存空间："<< sizeof(num4) << endl;
    return 0;
}