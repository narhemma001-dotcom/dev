#include <iostream>
using namespace std;

int main(){
float  balance = 0,count = 0,charge;
float deposit, withdraw; 
string x , y;    
while (true){
cout << "Enter amount to deposit: \n";
if (!(cin>>deposit)){
    cout <<"Invalid input\n";
    cin.clear();
    cin.ignore(1000,'\n');
    continue;
}else{
    balance += deposit;
   break; };

}
while(true){
cout<<"Enter amount to withdraw: \n";
if (!(cin >> withdraw)){
    cout <<"Invalid input\n";
    cin.clear();
    cin.ignore(1000,'\n');
    continue;

}
else{
    count += withdraw;
    if ( withdraw > balance){
        cout<<"You balance is insufficient\nDo you want to withdraw for a charge service of $25.00(yes/no)\n";
        if(!(cin>>y)){
        cout <<"Invalid input\n";
        cin.clear();
        cin.ignore(1000,'\n');
        continue;
    }
    else{
        if (y != "no" ){
        cout<<"Enter amount to withdraw: \n";
        if (!(cin >> withdraw)){
        cout <<"Invalid input\n";
        cin.clear();
        cin.ignore(1000,'\n');
        continue;
        }
        else{
            charge = 25;
            balance -= (withdraw +charge);
            cout << "Withdrawal successful\nYour current balance is " << balance <<'\n';
        }

        }
    }
}
else {
    if (count > 500){
        cout << "You have reached your maximum or today.\nTry again tomorrow\n";

    }
    else if(withdraw > 300){
             charge = withdraw * 0.04;
            balance -= (withdraw +charge);
            cout << "Withdrawal successful\nYour current balance is " << balance <<'\n';       
    }
    else {
        balance -= (withdraw +charge);
        cout << "Withdrawal successful\nYour current balance is " << balance <<'\n';
    }


}

cout << "Do you want to continue (yes/no): \n";
cin>> x;
if (x != "yes"){break;}



}
}

    return 0;
}











