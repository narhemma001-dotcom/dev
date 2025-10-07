#include <iostream>
using namespace std;

int main() {
float side1 , side2, side3;

cout<<"Enter length 1: ";
cin>>side1;
cout<<"Enter length 2: ";
cin>>side2;
cout<<"Enter length 3: ";
cin>>side3;

if(side1 == 0 || side2 ==0 || side3 == 0){
        cout<<"Invalid input..";}
    
else if(side1 == side2 && side2== side3){
    cout<<"It is an equilatoral triangle";
}
else if(side1 != side2 && side2 != side3 && side1 != side3 && side1 != 0 && side2!=0 && side3 != 0 ){
    cout<<"It is a scalene triangle";
}
else{
    cout<<"It is an isosceles triangle";

    };


  return 0;  
}


