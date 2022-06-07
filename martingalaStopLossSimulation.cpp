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
int const IT_ = 80;

int main() {
    int minSimulationMoney = 100;
    int maxSimulationMoney = -100;
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
                if(moneyBet >= (MINIMUM_BET*2*2*2*2*2)) {
                    moneyBet = 4;
                }
            }
            //cout << "number: " << ruletNumber << " / nextBet: ";
            //cout << moneyBet << endl;
        }
        int actualSimulationMoney = totalMoney - INITIAL_MONEY;
        cout << "Money won: " << actualSimulationMoney << endl;
        simulationsMoney += actualSimulationMoney;
        if(actualSimulationMoney < minSimulationMoney) {
            minSimulationMoney = actualSimulationMoney;
        } else if(actualSimulationMoney > maxSimulationMoney) {
            maxSimulationMoney = actualSimulationMoney;
        }
    }
    //cout << "Simulations TOTAL Money won: " << simulationsMoney << endl;
    cout << "maxSimulationMoney: " << maxSimulationMoney << "  / minSimulationMoney: " << minSimulationMoney << endl;
    cout << "Simulations AVG Money won: " << simulationsMoney/INITIAL_SIMULATIONS << endl;
}
