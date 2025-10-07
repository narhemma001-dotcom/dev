#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(){
while (true){
int num,operation;
vector<int>n={};
cout<<"1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n";
if (!(cin>> operation)){
cout<<"Invalid input, try again";
cin.clear();
cin.ignore(10000, '\n');
}  
for (int i = 0; i < 2 ; i++){
    cout<<"Enter num"<< i+1<<": ";
if (!(cin>> num)){
    cout<<"Invalid input, try again";
    cin.clear();
    cin.ignore(10000, '\n');
}
    n.push_back(num);
}
if (operation == 1){
int add = n[0]+n[1];
cout<<add<<endl;
}
else if(operation == 2){
    int sub = n[0]-n[1];
    cout<< sub<<endl;
}
else if(operation== 3){
    int mult = n[0]*n[1];
    cout<< mult<<endl;
}
else if(operation == 4){
    if (n[1]== 0){
        cout<<"Invalid input, second number cannot be zero"<<endl;
    }
    else{    
        double div = static_cast<double>(n[0])/n[1];  
    cout<< div<<endl;}
}
else{
    cout<<"Invalid operation"<<endl;
}
char x;
cout<<"Do you want to continue?(y/n): ";
cin>>x;
if(x=='n'){break;}
}



}