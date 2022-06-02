/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

// 1,2,4,8,16,32,64,128

int binaryNum[12];
int COLORES_SEGUIDOS = 6;
int TOTAL_MONEY = 0;

void decToBinary(int n)
{
    for(int kk = 0; kk < 12; ++kk) {
        binaryNum[kk]=0;
    }
 
    int ii = 0;
    while (n > 0) {
        binaryNum[ii] = n % 2;
        n = n / 2;
        ii++;
    }
 
    for (int j = COLORES_SEGUIDOS; j >= 0; j--) {
        cout << binaryNum[j];
    }
    //cout << endl;
}

void martingala()
{
    int diaMoney = 0;
    int moneyApostar = 1;
    for(int ii = 0; ii <= COLORES_SEGUIDOS; ++ii) {
        if(binaryNum[COLORES_SEGUIDOS-ii] == 0) { // red
            diaMoney -= moneyApostar;
            moneyApostar *= 2;
        } else { // black
           cout << " / " << moneyApostar*2 << endl;
           TOTAL_MONEY += moneyApostar*2;
           return; 
        }
    }
    
    cout << " / " << diaMoney << endl;
    
}

int main()
{
    for(int ii= 0; ii < 128; ++ii) {
         decToBinary(ii);
         martingala();
    }
    
    cout << "TOTAL_MONEY: " << TOTAL_MONEY << endl;

    return 0;
}
