# include <iostream>
# include<string>
using namespace std;

int main()
{
    int score = 0;
    cout << "请输入你的分数:";
    cin >> score;
    cout << "你的分数是:" << score <<endl;
    if(score >= 600)
    {
        cout << "恭喜你考上一本"<< endl;
    }
    else if((score<600&&score>=500))
    {
        cout << "恭喜你考上二本"<<endl;
    }
    else if((score< 500 && score >= 400))
    {
        cout << "恭喜你考上三本"<<endl;
    }
    else
    {
        cout << "你没有考上大学" << endl;
    }
    system("pause");
    return 0;
}