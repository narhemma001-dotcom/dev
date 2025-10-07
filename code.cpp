#include <iostream>
using namespace std;

int main(){
    double accBalance = 60;
    double withdrawalAmount; int Count=0;
    const double maxAmount = 500;
    double serviceCharge = 0, newBalance;
    char userResponse;



    // Check for 0 or negative account balance
    if (accBalance <= 0) {
        cout << "Account balance is zero or negative. Withdrawal not allowed." << endl;
    }else  {
        cout << "Enter amount to be withdrawn: " << endl;
        cin >> withdrawalAmount;
        Count++;
    }

    //Maximum Withdrawal
    if (withdrawalAmount > maxAmount || Count > 500) {
        cout << "Maximum withdrawal amount is $500. You've reached your limit for the day." << endl;
    }

    // Calculate service charge with withdrawals over 300
    if (withdrawalAmount > 300) {
        serviceCharge = 0.04 * (withdrawalAmount)  ;
        newBalance =accBalance - (withdrawalAmount + serviceCharge);
        cout << "Your new balance is: " <<newBalance << endl;
    }


    // Checking if account has sufficient balance
    if (accBalance >= withdrawalAmount ) {
        newBalance = accBalance - withdrawalAmount;
        cout << "Withdrawal successful. Your new balance is: $" << newBalance << endl;
    } else {
        cout << "Insufficient funds. Would you like to withdraw with a service charge of $25? (Y/N): ";
        cin >> userResponse;
    }
        if (userResponse == 'Y') {
            newBalance = accBalance - (withdrawalAmount + 25);
            cout << "Withdrawal successful. Your new balance is: $" << newBalance << endl;
        }
        return 0;
}

