#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int reverse(int x) {
    if(x == 0 || x < -2147483647 || x > 2147483647){
        return 0;
    }
    bool negative = false;
    if(x < 0){
        negative = true;
        x = x * -1;
    }
    string ans = "";
    while(x != 0){
        ans += std::to_string(x%10);
        x /= 10;
    }
    try{
        int res = std::stoi(ans);
    }
    catch(std::out_of_range& e){
        return 0;
    }
    if(negative)
        return std::stoi(ans) * -1;
    return std::stoi(ans);
}
int main(){
    reverse(-2147483648);
}

