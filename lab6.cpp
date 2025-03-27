#include <iostream>

using namespace std;
double harmonicSum =0;

double harmonic(int n){
    if(n==0){
        return 0;
    }
    harmonic(n-1);

    harmonicSum +=1.0/n;

    if(n==1){
        cout<<"1";
    }
    else{
        cout<<" + 1/"<<n;
    }

    return harmonicSum;
}

int main() {
    int num;

    cout << "Enter number for the harmonic series: ";
    cin >> num;

    double y = harmonic(num);
    cout<<" = "<<y;

}
