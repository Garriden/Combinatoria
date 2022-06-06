#include <iostream>
#include <algorithm>
#include <chrono>
#include <random>
#include <vector>
using namespace std;

// 0.4865 (18/37)

int const INITIAL_SIMULATIONS = 1000;
int const INITIAL_MONEY = 100;
int const MINIMUM_BET = 4;
int const IT_ = 50;

int main() {

    int simulationsMoney = 0;
    int simulations = INITIAL_SIMULATIONS;
    while(simulations --> 0) {
        int ii = IT_;
        int totalMoney = INITIAL_MONEY;
        int moneyBet = MINIMUM_BET;
        while(ii --> 0) {
            totalMoney -= moneyBet;
        
            mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
            int ruletNumber = rng()%37;
            
            if(ruletNumber <= 18) {
                //cout << "RED, WIN!" << "   . ";
                totalMoney += moneyBet * 2;
                moneyBet = 4;
            } else { // BLACK
                //cout << "BLACK, LOST" << " . ";
                moneyBet *= 2;
                if(moneyBet >= 128) {
                    moneyBet = 4;
                }
            }
            //cout << "number: " << ruletNumber << " / nextBet: ";
            //cout << moneyBet << endl;
        }
        cout << "Money won: " << totalMoney - INITIAL_MONEY << endl;
        simulationsMoney += (totalMoney - INITIAL_MONEY);
    }
    cout << "Simulations AVG Money won: " << simulationsMoney/INITIAL_SIMULATIONS << endl;
}
