# 383. [Ransom Note](https://leetcode.com/problems/ransom-note/)

Given two strings `ransomNote` and `magazine`, return `true` *if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1**:

> **Input**: `ransomNote = "a"`, `magazine = "b"`
>
> **Output**: `false`

**Example 2**:

> **Input**: `ransomNote = "aa"`, `magazine = "ab"`
>
> **utput**: `false`

**Example 3**:

> **Input**: `ransomNote = "aa"`, `magazine = "aab"`
>
> **Output**: `true`

**Constraints**:

- $1 \le \texttt{ransomNote.length}, \texttt{magazine.length} \le 10^5$
- `ransomNote` and `magazine` consist of lowercase English letters.
