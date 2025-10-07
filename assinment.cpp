#include <iostream>
using namespace std;

int main(){
    float deposit, balance = 0,with_counter = 0;
    while (true){
    cout<<"Enter amount to deposit: \n";
    if (!(cin>>deposit)){
    cout<<"Invalid input \n";
    cin.clear();
    cin.ignore(1000, '\n');
    continue;
    }
    else{
        balance += deposit;
        cout<<"Deposit successful\n";
      break;
    }
}
    while (true)
    {
    string x;   
    float with_draw,charge; 
    
    cout << "Enter amount to withdraw: \n";
    if (!(cin>>with_draw)){
        cout<<"Invalvid input \n";
        cin.clear();
        cin.ignore(10000,'\n');
        continue;
  
    }  
         with_counter += with_draw;
        if (with_counter > 500){
            cout<<"You have reached your maximum withdrawal for a day\nTry again tomorrow\n";
        }
        if(with_draw > 300){
            charge = with_draw * (0.04);
            balance -= (with_draw + charge) ;
            cout << "Successful withdrawal\nYour account balance is "<< balance <<"\n";
        }
        else if(with_draw < 300){
            balance -= with_draw;
            cout << "Successful withdrawal\nYour account balance is "<< balance<<"\n";            
        }
       else if (with_draw > balance){
        cout << "Insufficient balance\n";
    }

    
  cout<<"Do you want to continue (yes/no): \n";
  cin>> x;
  if (x != "yes"){
    break;};




}
return 0;
}


