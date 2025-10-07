
#include <iostream>
#include <cmath>
using namespace std;

int main(){
float height, weight,BMI ;
cout << "Enter your height: ";
cin>> height;
cout << "Enter your weight: ";
cin>> weight;

BMI = weight/(pow(height, 2));


if (BMI <= 18.5){
    cout<<"Your are underweight";
}
else if ( BMI > 18.5 && BMI < 24.9){
    cout<<"You have a normal weight";
}
else if (BMI <=34.9){
    cout<< "You are obesse";
}
else if(BMI <= 39.9){
    cout<<"You are severly obese";
}
else if (BMI >= 40){
    cout<< "You are beyond repairs";
}


    return 0;
}

