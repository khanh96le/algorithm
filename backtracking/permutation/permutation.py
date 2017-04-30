
n = 8
b = [True] * (n + 1)
x = [0] * (n + 1)

def permutation(i):
  for j in range(0, n + 1):
    if b[j]:
      x[i] = j
      b[j] = False
      if (i < n):
        permutation(i+1)
      else:
        log(x)
      b[j] = True

def log(x):
  print x


permutation(0)
