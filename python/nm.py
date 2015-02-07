'''
This file is part of NormMem.

NormMem is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

NormMem is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with NormMem.  If not, see <http://www.gnu.org/licenses/>.
'''

import math, timeit

pw = ""

class NormNum():
    def __init__(self, poly):
        # poly is the polynomial P
        self.poly = poly
        self.t = {}
    def polyf(self, x):
        # returns P(x)
        result = 0
        l = len(self.poly)
        for i in xrange(l):
            result += int(math.pow(x,l-i)) * (self.poly[i])
        return result
    def get(self,n):
        # returns the nth digit
        if n not in self.t:
            result = ""
            i = 0
            while len(result) <= n:
                while i >= len(plist): 
                    print n
                    addprimes(42)
                result+=(str(int(self.polyf(plist[i]))))
                i += 1
            self.t[n] = result[n]
        return self.t[n]
    def getdat(self,i,l):
        return ''.join(map(self.get,xrange(i,i+l)))
    def find(self,data,lim=10000):
        data = str(data)
        i = 0
        j = 0
        while i <  xrange(lim - len(data)):
            #print "...", i
            if j == len(data): return i-j
            if self.get(i)==data[j]:
                j += 1
            else:
                i -= j
                j = 0
            i += 1

def isprime(n):
    if n < 2: return False
    global plist
    if n <= plist[-1] and n in plist:
        return True
    r = int(math.ceil(math.sqrt(n)))+2
    for i in plist:
        if i > r: break
        if n%i==0:
            return False
    plist.append(n)
    return True
        
        
def addprimes(n):
    print "\tPrimes +=", n
    for i in xrange(n):
        cur = int(plist[-1])+1
        while not isprime(cur):
            cur += 1

def pw2poly(pw):
    pw = str(pw)
    if len(pw) > 256: return False
    else:
        poly = [0]*256
        for i in xrange(len(pw)):
            poly[i] = ord(pw[i])
        return poly
    

#################
#               #
# MAIN FUNCTION #
#               #
#################

def main():
    data = 42
    pswd = pw2poly(pw)
    N = NormNum(pswd)
    x = N.find(data)
    y = N.getdat(x,len(str(data)))

    print x,y
plist = [2]

if __name__=="__main__": main()
 
 
