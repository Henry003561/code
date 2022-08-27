#include <iostream>
using namespace std;

int main()
{
    //1.前置递增
    int a=10;
    ++a;//让变量加1
    cout << "a=" << a << endl;
    //2.后置递减
    int b=10;
    b++;
    cout << "b=" << b << endl;
    //3.前置和后置的区别
    // 前置递增 先让变量加1后进行表达式的计算
    // 后置递增 先进行表达式的计算再进行变量加1
    int a2=10;
    int b2= ++a2*10;
    cout << "a2=" << a2 << endl;
    cout << "b2=" << b2 << endl;
    int a3 = 10;
    int b3 =a3++ * 10;
    cout << "a3=" << a3 <<endl;
    cout << "b3=" << b3 << endl;
    system("pause");
    return 0;
}