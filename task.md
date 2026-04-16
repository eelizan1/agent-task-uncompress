# Uncompress
## Problem Description
Write a method, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:
```
<number><char>
for example, '2c' or '3a'.
```
The method should return an uncompressed version of the string where each `char` of a group is repeated `number` times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

## Requirements
- Function name should be `uncompress`
- Input: A single string of one or more `<number><char>` groups
- Output: A single uncompressed string
- The number in each group may be more than one digit (e.g. `12e` or `127y`)
- Handle strings with a single group as well as multiple consecutive groups
- File name should be `uncompress.py`

## Test Examples
```
uncompress("2c3a1t");   // -> "ccaaat"
uncompress("4s2b");     // -> "ssssbb"
uncompress("2p1o5p");   // -> "ppoppppp"
uncompress("3n12e2z");  // -> "nnneeeeeeeeeeeezz"
uncompress("127y");     // -> "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
```

## Acceptance Criteria
- Must include type hints
- Must include a docstring with a description and at least one example
- Must correctly handle multi-digit numbers as the repeat count
- Must not use any built-in compression or encoding libraries
- Must include error handling for invalid or malformed input strings
