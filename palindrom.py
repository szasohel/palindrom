def longestPalindrome(input_string):
    # Transform input_string to trans_string.
    # For example, input_string = "abba", trans_string = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    trans_string = '#'.join('^{}$'.format(input_string))
    ts_length = len(trans_string)
    P = [0] * ts_length # new array to store length of palindromes
    C = R = 0
    
    for i in range (1, ts_length-1):
        mirror = 2*C - i #shifting mirror

        if (i < R): # checking if i is with in the right boundary
            P[i] = min(R - i, P[mirror])

        # Attempt to expand palindrome centered at i
        while trans_string[i + 1 + P[i]] == trans_string[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center and right boundary based on expanded palindrome.
        if i + P[i] > R:
            C = i
            R =i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((ts_length, i) for i, ts_length in enumerate(P))
    return input_string[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]


def main():
    s = "jkaababababaa"

    print (longestPalindrome(s))


if __name__ == '__main__':
    main()

