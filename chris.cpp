#include <iostream>
using namespace std;

int main(){

while (true){    
int len1 , len2,no_of_tile; 
float area; 
string n,x;
cout<<"Enter unit of measurement(meter/centimeter)\n";
cin >> n;

cout<<"Enter length 1: \n";
if (! (cin >> len1)){
cout << "Invalid input";
cin.clear();
cin.ignore(1000,'\n');
continue;

}
cout<<"Enter length 2: \n";
if(! (cin >> len2)){
cout << "Invalid input";
cin.clear();
cin.ignore(1000,'\n');
continue;

}

if (n == "meter"){
    area = len1 * len2 ;
}
else if (n == "centimeter"){
area = (len1/100.0) * (len2/100.0);
}
else {
    cout<<"Invalid input,\nEnsure input is meter or centimeter";
    continue;
}
    cout <<"Area is "<< area << "\n";
    no_of_tile = area / 0.25;
    cout<<"Number of tiles required is "<< no_of_tile<<"\n";

cout << "Do you want to continue(yes/no): \n";
cin>> x;
if (x != "yes"){break;}
}
return 0;
}

