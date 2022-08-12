# include<iostream>
using namespace std;

int main()
{
    float f1 = 3.14f;
    double d1 = 3.144;
    cout << "f1 =" << f1 << endl;
    cout << "d1 = " << d1 << endl;
    // 统计实型内存空间
    cout << "float的内存空间有：" << sizeof(f1) << endl;
    cout << "double的内存空间有：" << sizeof(d1) << endl;
    return 0;
}