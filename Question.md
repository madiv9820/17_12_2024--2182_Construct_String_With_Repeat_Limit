# [2182. Construct String With Repeat Limit](https://leetcode.com/problems/construct-string-with-repeat-limit?envType=daily-question&envId=2024-12-17)

**Type:** Medium <br>
**Topics:** Hash Table, String, Greedy, Heap (Priority Queue), Counting <br>
**Companies:** Arista Networks, Microsoft 
<hr>

You are given a string `s` and an integer `repeatLimit`. Construct a new string `repeatLimitedString` using the characters of `s` such that no letter appears **more than** `repeatLimit` times **in a row**. You do **not** have to use all characters from `s`.

Return *the ***lexicographically largest**** `repeatLimitedString` *possible*.

A string `a` is **lexicographically larger** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters do not differ, then the longer string is the lexicographically larger one.
<hr>

### Examples

- **Example 1:** <br>
**Input:** s = "cczazcc", repeatLimit = 3 <br>
**Output:** "zzcccac" <br>
**Explanation:** We use all of the characters from s to construct the repeatLimitedString "zzcccac". <br>
The letter 'a' appears at most 1 time in a row. <br>
The letter 'c' appears at most 3 times in a row. <br>
The letter 'z' appears at most 2 times in a row. <br>
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString. <br>
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac". <br>
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

- **Example 2:** <br>
**Input:** s = "aababab", repeatLimit = 2 <br>
**Output:** "bbabaa" <br>
**Explanation:** We use only some of the characters from s to construct the repeatLimitedString "bbabaa". <br>
The letter 'a' appears at most 2 times in a row. <br>
The letter 'b' appears at most 2 times in a row. <br>
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString. <br> 
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa". <br>
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
<hr>

### Constraints:
- <code>1 <= repeatLimit <= s.length <= 10<sup>5</sup></code>
- `s` consists of lowercase English letters.
<hr>

### Hints:
- Start constructing the string in descending order of characters.
- When repeatLimit is reached, pick the next largest character.