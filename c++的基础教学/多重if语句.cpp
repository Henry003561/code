# include<iostream>
# include<string>
using namespace std;

int main()
{
    int score=0;
    cout << "请输入一个分数:";
    cin >> score;
    cout << "你的分数是：" << score << endl;
    if(score > 600)
    {
        cout << "恭喜，你考上一本大学" << endl;
    }
    else
    {
        cout << "未考上一本" << endl;
    }
    system("pause");
    return 0;
}