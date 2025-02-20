#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name;
    long number;

    cout << "What is your name? " << endl;
    getline(cin, name);
    cout << "Hello "<< name << endl;

    cout << "What is your Student ID? " << endl;
    cin >> number;
    cout << "Your ID is "<< number << endl;

    //

    int var1;
    int var2;

    cout << "Enter first number" << endl;
    cin >> var1;

    cout << "Enter second number" << endl;
    cin >> var2;

    int sum = var1 + var2;
    int diff = var1 - var2;
    int prod = var1 * var2;

    cout << "var1 = " << var1 << endl;
    cout << "var2 = " << var2 << endl;
    cout << "var1 + var2 = " << sum << endl;
    cout << "var1 - var2 = " << diff << endl;
    cout << "var1 * var2 = " << prod << endl;

    //
    string name;
    int labGrade;
    int midGrade;
    int finalGrade;

    cout << "What is your name? " << endl;
    getline(cin, name);

    cout << "Enter your Lab Grade? " << endl;
    cin >> labGrade;

    cout << "Enter your Midterm Grade? " << endl;
    cin >> midGrade;

    cout << "Enter your Final Grade? " << endl;
    cin >> finalGrade;

    double lastScore;
    lastScore=(labGrade*25/100)+(midGrade*35/100)+(finalGrade*40/100);

    cout << "Name: "<< name << endl;
    cout << "Lab Grade: "<< labGrade << endl;
    cout << "Midterm Grade: "<< midGrade << endl;
    cout << "Final Grade: "<< finalGrade << endl;
    cout << "Last Score: "<< lastScore << endl;

    //
    cout << "* \n ** \n *** \n ** \n * "<<endl;

    return 0;
}
