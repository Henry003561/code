# include<iostream>
using namespace std;

int main()
{
    int a;
    int b;
    a= 13;
    b = 9;
    // a+b加减乘除运算
    int c;
    c = a+b;
    cout << "a+b=" << c << endl;
    int d;
    d = a-b;
    cout << "a-b=" << d << endl;
    int e;
    e = a*b;
    cout << "a*b=" << e << endl;
    int f;
    f = a/b;
    cout << "a/b=" << f << endl; //两个整数相除，结果依然是整数
    double a1;
    double b1;
    cout <<"输入a1";
    cin >> a1;
    cout << "输入b1";
    cin >> b1;
    cout << a1/b1 << endl;
    system("pause"); 
    return 0;
}