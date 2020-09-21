def repeatedString(s, n):
    for i in range(n):
        s = (s * n)[0:n]
    print(s.count('a'))

if __name__ == '__main__': 
    s = 'a'
    n = 10000
    repeatedString(s, n) 