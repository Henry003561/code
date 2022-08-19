#include <iostream>
using namespace std;

int main()
{
    //1.创建字符型变量
    char ch = 'a';
    cout << ch << endl;
    //2.字符型变量的内存大小
    cout << "chr的内存大小:" << sizeof(ch) << endl;
    //3.查看字符型变量的对应的ascll码
    cout << (int)ch << endl;
    system("pause");
    return 0;
}