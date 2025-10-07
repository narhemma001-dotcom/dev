#include <iostream>
using namespace std;

int main() {
    // Declare variables
    double baseSalary, totalSales, bonus, additionalBonus, payCheck;
    int noOfServiceYears;

    // Get user input
    cout << "Enter base salary: $";
    cin >> baseSalary;

    cout << "Enter number of service years: ";
    cin >> noOfServiceYears;

    cout << "Enter total sales for the month: $";
    cin >> totalSales;

    // Calculate bonus based on service years
    if (noOfServiceYears <= 5) {
        bonus = 10 * noOfServiceYears;
    } else {
        bonus = 20 * noOfServiceYears;
    }

    // Calculate additional bonus based on total sales
    if (totalSales < 5000) {
        additionalBonus = 0;
    } else if (totalSales >= 5000 && totalSales < 10000) {
        additionalBonus = totalSales * 0.03;
    } else {
        additionalBonus = totalSales * 0.06;
    }

    // Calculate total paycheck
    payCheck = baseSalary + bonus + additionalBonus;

    // Output the results
    cout << "\nSummary of Earnings:\n";
    cout << "Base Salary: $" << baseSalary << endl;
    cout << "Bonus: $" << bonus << endl;
    cout << "Additional Bonus (Commission): $" << additionalBonus << endl;
    cout << "Total Paycheck: $" << payCheck << endl;

    return 0;
}