# just a random function
import sys
def printIfTrue(m, prefix = ''):
  if m:
    print(prefix + m)
    sys.stdout.flush()
  return m

if __name__ == '__main__':
  printIfTrue(False, 'tool test:')
  printIfTrue('True', 'tool test:')
