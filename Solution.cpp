#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        // Step 1: Create a frequency map to store the frequency of each character in the string
        unordered_map<char, int> char_Frequency;
        for(const char& ch: s) ++char_Frequency[ch];  // Iterate over the string to count character occurrences

        // Step 2: Use a max-heap (priority queue) to store characters based on their frequency.
        // Since we want to access the largest character first, we use a max-heap by default in C++.
        priority_queue<char> pq;
        for(auto ptr: char_Frequency) pq.push(ptr.first);  // Push all characters into the priority queue

        // Step 3: Initialize the result string to store the final output and set the repeat limit.
        string repeat_String = "";
        int limit = repeatLimit;

        // Step 4: Process the characters in the heap until it's empty
        while(pq.size()) {  
            // Step 4.1: Pop the character with the highest lexicographical value (max-heap behavior)
            char ch = pq.top(); 
            pq.pop();

            // Step 4.2: Add the current character to the result string while respecting the repeat limit
            while(char_Frequency[ch] && limit) {
                repeat_String += ch;  // Append the character to the result string
                --char_Frequency[ch];  // Decrease its frequency
                --limit;  // Decrease the remaining repeat limit
            }

            // Step 4.3: If there are still more of the same character left, push a different character to break the limit
            if(char_Frequency[ch]) {
                // If the heap is empty and we can't add more characters, break the loop
                if(!pq.size()) break;
                
                // Add the next largest character to the result string to avoid repeating the same character too many times
                repeat_String += pq.top(); 
                --char_Frequency[pq.top()];  // Decrease the frequency of the new character
                
                // If the next character has no occurrences left, remove it from the heap
                if(!char_Frequency[pq.top()]) pq.pop();
                
                // Push the current character back into the heap as there are still remaining occurrences of it
                pq.push(ch);
            }

            // Step 4.4: Reset the repeat limit after each full cycle
            limit = repeatLimit;
        }

        // Step 5: Return the result string after processing all characters
        return repeat_String;
    }
};

int main() {
    vector<pair<string,int>> inputs = {{"cczazcc",3},{"aababab",2}};
    vector<string> outputs = {"zzcccac","bbabaa"};
    Solution sol;

    for(int i = 0; i < inputs.size(); ++i)
        cout << ((sol.repeatLimitedString(inputs[i].first, inputs[i].second) == outputs[i]) ? "true" : "false") << endl;
}