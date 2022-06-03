#include <iostream>
#include <cmath>
using namespace std;

// 1,2,4,8,16,32,64,128

#define ITERATIONS false

int binaryNum[12];
bool PRINT_ALL_POSSIBILITIES = true;

int MAX_INITIAL_MONEY = 512;
int MAX_COLORES_SEGUIDOS = 8;

int COLORES_SEGUIDOS = 5;
int INITIAL_MONEY = 4;
int TOTAL_MONEY = 0;
int lastLost = 0;

void DecToBinary(int n)
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
    
    if(PRINT_ALL_POSSIBILITIES) {
        for (int j = COLORES_SEGUIDOS-1; j >= 0; j--) {
            cout << binaryNum[j];
        }
    }
}

void Martingala()
{
    int dayMoneyLost = 0;
    int moneyApostar = INITIAL_MONEY;
    for(int ii = 0; ii <= COLORES_SEGUIDOS-1; ++ii) {
        if(binaryNum[COLORES_SEGUIDOS-1-ii] == 0) { // red
            dayMoneyLost -= moneyApostar;
            moneyApostar *= 2;
        } else { // black
            if(PRINT_ALL_POSSIBILITIES) {
                cout << " / " << (moneyApostar*2) + dayMoneyLost << endl;
            }
            TOTAL_MONEY += (moneyApostar*2) + dayMoneyLost;
            return; 
        }
    }
    if(PRINT_ALL_POSSIBILITIES) {
        cout << " / " << dayMoneyLost << endl;
    }
    TOTAL_MONEY += dayMoneyLost;
    lastLost = dayMoneyLost;
    
}

int main()
{
#if ITERATIONS
    cout << "APUESTAS, INITIAL_MONEY, TOTAL_MONEY, LAST_LOST ";
    cout << endl;
    
    COLORES_SEGUIDOS = 1; 
    INITIAL_MONEY = 1;
    
    while(INITIAL_MONEY <= MAX_INITIAL_MONEY) {
        while(COLORES_SEGUIDOS <= MAX_COLORES_SEGUIDOS) {
#endif //ITERATIONS
        
            for(int ii= 0; ii < exp2(COLORES_SEGUIDOS); ++ii) {
                 DecToBinary(ii);
                 Martingala();
            }
     
            cout << exp2(COLORES_SEGUIDOS) << "," << INITIAL_MONEY << "," << TOTAL_MONEY << "," << lastLost;
            cout << endl;
#if ITERATIONS               
            TOTAL_MONEY = 0;
            
            COLORES_SEGUIDOS++;
        }
        COLORES_SEGUIDOS = 1;
        INITIAL_MONEY *= 2;
    }
#endif //ITERATIONS
    return 0;
}
