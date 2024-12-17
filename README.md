# [2182. Construct String With Repeat Limit](https://leetcode.com/problems/construct-string-with-repeat-limit?envType=daily-question&envId=2024-12-17)

- ### Intuition
    The goal of the problem is to construct a string such that:
    - We prioritize lexicographically larger characters.
    - No character appears more than `repeatLimit` times consecutively.

    We can use a **max-heap** (priority queue) to achieve this, which allows us to always pick the largest available character. By maintaining a frequency count of each character, we can ensure that no character exceeds the `repeatLimit` in consecutive appearances. If a character would exceed the limit, we pick the next largest character to avoid violating the constraint.

- ### Approach
    1. **Count Character Frequencies:**
        - First, we count the frequency of each character in the string. This is done using a hash map (like `unordered_map` in C++ or `collections.Counter` in Python).

    2. **Initialize the Max-Heap:**
        - We create a max-heap (priority queue) where the characters are sorted by their lexicographical order. In Python, this is achieved by using negative ASCII values with `heapq` (since it’s a min-heap by default). In C++, the priority queue is used directly.
    
    3. **Build the Result String:**
        - We repeatedly pop the largest character from the heap and append it to the result string, ensuring that no character is added more than `repeatLimit` times consecutively.
        - If there are remaining occurrences of the character, but we have reached the repeat limit, we pop the next largest character and add it to the result string. The original character is then pushed back into the heap to be used later.

    4. **Repeat Until All Characters are Processed:**
        - This process continues until all characters are exhausted or no more characters can be added without violating the `repeatLimit`.

- ### Code Implementation
    - **Python Solution**
        ```python3 []
        class Solution:
            def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
                # Step 1: Count the frequency of each character in the string
                char_Frequency, limit = Counter(s), repeatLimit
                
                # Step 2: Create a list of tuples where each tuple contains (-ASCII value, character)
                # The negative sign is used because heapq is a min-heap and we need to prioritize larger characters first
                characters = [(-ord(ch), ch) for ch in char_Frequency]
                
                # Step 3: Convert the list into a heap (min-heap based on the negative ASCII values)
                heapq.heapify(characters)

                repeat_String = ''  # This will store the final result string

                # Step 4: Process the heap until it's empty
                while len(characters):
                    x, ch = heapq.heappop(characters)  # Pop the character with the largest ASCII value (due to negative sign)

                    # Step 5: Add characters to the result string while respecting the repeatLimit
                    # The character can be added to repeat_String as long as its frequency is greater than 0 and repeatLimit allows
                    while char_Frequency[ch] and limit:
                        repeat_String += ch
                        char_Frequency[ch] -= 1  # Decrease the frequency of the character
                        limit -= 1  # Decrease the remaining repeat limit

                    # Step 6: If there are still characters left of the same type, process the next available character
                    if char_Frequency[ch]:
                        # If the heap is empty, break out of the loop
                        if not len(characters):
                            break
                        # Pop the next character with the largest ASCII value
                        y, temp_ch = heapq.heappop(characters)

                        # Add this second character to the result string
                        repeat_String += temp_ch
                        char_Frequency[temp_ch] -= 1  # Decrease its frequency

                        # Push the current character back into the heap (because we may still have more of it)
                        heapq.heappush(characters, (x, ch))
                        
                        # If there are more of the second character, push it back into the heap as well
                        if char_Frequency[temp_ch]:
                            heapq.heappush(characters, (y, temp_ch))

                    # Step 7: Reset the repeat limit after every cycle
                    limit = repeatLimit
                
                # Step 8: Return the result string after all characters are processed
                return repeat_String
        ```
    - **C++ Solution**
        ```cpp []
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
        ```

- ### Time Complexity
    - **Counting character frequencies:** This takes **$O(n)$** where **$n$** is the length of the string, as we need to traverse the string once to count the occurrences of each character.
    - **Heap operations:** 
        - The heap operations (insertion and removal) take **$O(log(k))$** time, where **$k$** is the number of unique characters in the string.
        - For each character, we perform heap operations. In the worst case, there are **$n$** characters, and each character can be involved in **$O(log(k))$** heap operations.
        - Thus, the overall heap-related complexity is **$O(n*log(k))$**, where **$k$** is the number of unique characters.

    Therefore, the **total time complexity** is: **$O(n+n*log(k))$** = **$O(nlog(k))$**, where:
        - **$n$** is the length of the string.
        - **$k$** is the number of unique characters.

- ### Space Complexity
    - **Character frequency map:** We use a hash map (or dictionary) to store the frequency of each character, which requires **$O(k)$ **space, where **$k$** is the number of unique characters.
    - **Heap storage:** The heap stores the unique characters, so it also requires **$O(k)$** space.

    Thus, the **total space complexity** is: **$O(k)$**, where:
        - **$k$** is the number of unique characters in the string.