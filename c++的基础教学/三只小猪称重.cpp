# include<iostream>
# include<string>
using namespace std;

int main()
{
    double A;
    double B;
    double C;
    cout << "A小猪的体重是：";
    cin >> A;
    cout << "B小猪的体重是：";
    cin >> B;
    cout << "C小猪的体重是：";
    cin >> C;
    if((A>B && A>C))
    {
        cout<< "A小猪最重"<<endl;
    }

    else if ((B>A && B>C))
    {
        cout << "B小猪是最重" << endl;
    }

    else if(C>A && C>B)
    {
        cout << "C小猪是最重的" << endl;
    }  

    else if ((A==B && C<A))
    {
        cout << "A和B重于C" <<endl;
    }

    else if ((A==C && A>B))
    {
        cout << "A和C重于B" << endl;
    }

    else if ((B==C && B>A))
    {
        cout << "B和C同样重于A" << endl;
    }

    else
    {
        cout << "A和B和C同样重" << endl;
    }
    
    system("pause");
    return 0;
}