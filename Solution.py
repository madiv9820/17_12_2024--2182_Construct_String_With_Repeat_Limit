from collections import Counter
import heapq

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