#include <iostream>
#include <string>
using namespace std;

class Solution {
  public:
    string reverseWords(string s) {
      string result = "";
      int r = s.length();
      int lenWord = 0;

      while(r > 0) {
        while(r > 0 && s[--r] == ' ');

        while(r >= 0 && s[r] != ' ') {
          r--;
          lenWord++;
        };

        result += s.substr(r+1, lenWord) + ' ';
        lenWord = 0;
      }

      result.pop_back();
      if(*result.end() == ' ') result.pop_back();
      return result;
    }
};

int main() {
  Solution s;
  int a = 4;
  cout << 'x' << s.reverseWords(" the   sky is   blue   ") << 'x' << endl;
}
