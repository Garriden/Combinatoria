#include <iostream>
#include <cmath>
using namespace std;

// APUESTAS, INITIAL_MONEY, TOTAL_MONEY, LAST_LOST 
// 32,4,320,-124
// 1,2,4,8,16,32,64,128

#define ITERATIONS false

int binaryNum[12];
bool PRINT_ALL_POSSIBILITIES = true;

int MAX_INITIAL_MONEY_IT = 512;
int MAX_COLORES_SEGUIDOS_IT = 8;

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
    int moneyApostar = INITIAL_MONEY;
    int dayMoney = 0;
    for(int ii = 0; ii <= COLORES_SEGUIDOS-1; ++ii) {
        dayMoney -= moneyApostar; 
        if(binaryNum[COLORES_SEGUIDOS-1-ii] == 0) { // black
            moneyApostar *= 2;
        } else { // red
            dayMoney += (moneyApostar*2);
            if(PRINT_ALL_POSSIBILITIES) {
                cout << " / " << dayMoney << endl;
            }
            
            return; 
        }
    }
    if(PRINT_ALL_POSSIBILITIES) {
        cout << " / " << dayMoney << endl;
    }
    TOTAL_MONEY = dayMoney;
}

int main()
{
#if ITERATIONS
    cout << "APUESTAS, INITIAL_MONEY, TOTAL_MONEY, LAST_LOST ";
    cout << endl;
    
    COLORES_SEGUIDOS = 1; 
    INITIAL_MONEY = 1;
    
    while(INITIAL_MONEY <= MAX_INITIAL_MONEY_IT) {
        while(COLORES_SEGUIDOS <= MAX_COLORES_SEGUIDOS_IT) {
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
