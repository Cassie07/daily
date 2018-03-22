# this is the code of my internship programming online
# input: abb,aaa
# output: 2
# input: ababaa,aba
# output: 3+2=5
# we try to find the largest difference in this code

class solution(object):
    def __init__(self):
        self.sum = 0
        self.count = 1
        self.S = raw_input('s=')
        self.T = raw_input('t=')

    def difference(self):
        s = list(self.S)
        t = list(self.T)
        if len(t) <= len(s) and len(t) >= 1 and len(s) < (10 ** 5):
            while (len(s) >= len(t)):
                for i in range(len(t)):
                    if s[i] != t[i]:
                        self.sum = self.sum + 1
                s = s[self.count:len(s)]
                self.count = self.count + 1
            return self.sum
        else:
            return 0
        print(sum)

if __name__ == '__main__':
    b=solution()
    print(b.difference())
