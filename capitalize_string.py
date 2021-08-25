# Complete the solve function below.
def solve(s):
    r = ''
    for i in range(len(s)):
        if i == 0 or s[i-1] == ' ':
            r += s[i].capitalize()
        else:
            r += s[i]
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
