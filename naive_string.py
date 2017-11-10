text = "CCDDNGNNNGEANGEREERAN"

pat = "ANGER"

def search(text,pat):
    m = len(pat)
    n = len(text)

    for i in range(0,n-m+1):
        k = 0
        for j in range(0,m):
            k = k+1
            if text[i+j] != pat[j]:
                break;

        if k == m:
            print('Pattern found at ',i)

print('string = ',text)
print('pattern = ',pat)
search(text,pat)