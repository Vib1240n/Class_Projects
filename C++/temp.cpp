#include <iostream>

using namespace std;

string repeat;
char size;
char coupon;
double price;
double total;

int main()
{
  while (repeat != "-1")
  {
    cout << "What size pizza did you order? (m/l) ";
    cin >> size;
    
    if (size == 'm')
    {
        price = 9.99;
        cout << "The medium size pizza costs $" << price << ".\n";
        
        //Coupon Input
        cout << "Save $2 with an online coupon! Do you have a coupon?";
        cin >> coupon;
        if (coupon == 'y')
        {
            total = price - 2;
            cout << "You used a coupon. Your price is $" << total <<".\n";
            cout << "To exit the program, enter -1. To try again, enter any other key.";
            cin >> repeat;
            if(isdigit((repeat[1]))){
                continue;
            }
            else{
                break;
            }
        }
        else if (coupon == 'n')
        {
            total = price;
            cout << "You did not use a coupon. Your price is $" << total <<".\n";
            cout << "To exit the program, enter -1. To try again, enter any other key.";
            cin >> repeat;
            if(isdigit((repeat[1]))){
                continue;
            }
            else{
                break;
            }
        }
        else
        {
            cout << "Error. To exit the program, enter -1. To try again, enter any other key.";
            cin >> repeat;
            if(isdigit((repeat[1]))){
                continue;
            }
            else{
                break;
            }
        }
    } //End of if statement
    else if (size == 'l')
    {
        price = 12.99;
        cout << "The large pizza costs $" << price << ".\n";
        
        //Coupon Input
        cout << "Save $2 with an online coupon! Do you have a coupon?";
        cin >> coupon;
        if (coupon == 'y')
        {
            total = price - 2;
            cout << "You used a coupon. Your price is $" << total <<".\n";
            cout << "To exit the program, enter -1. To try again, enter any other key.";
            cin >> repeat;
            if(isdigit((repeat[1]))){
                continue;
            }
            else{
                break;
            }
        }
        else if (coupon == 'n')
        {
            total = price;
            cout << "You did not use a coupon. Your price is $" << total <<".\n";
            cout << "To exit the program, enter -1. To try again, enter any other key.";
            cin >> repeat;
            if(isdigit((repeat[1]))){
                continue;
            }
            else{
                break;
            }
        }
        else
        {
            cout << "Error. To exit the program, enter -1. To try again, enter any other key.";
            cin >> repeat;
            if(isdigit((repeat[1]))){
                continue;
            }
            else{
                break;
            }
        }
   
    } //End of elseif statement
    else
    {
        cout << "Error. To exit program, enter -1. To try again, enter any other key.";
        cin >> repeat;
        if(isdigit((repeat[1]))){
                continue;
            }
            else{
                break;
            }
    } //END OF SIZE INPUT
    
    
  }
    return 0;
}