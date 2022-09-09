
class vector:
    def __init__(self, vec):
        self.vec =  vec

    def __str__(self):
        str1 = ''
        index = 0
        for i in self.vec:
            str1 += f' {i}a{index} +'
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)
    
    def __mul__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] * vec2.vec[i])
        return vector(newlist)
            
    
        


v =  vector([4,2,7])
v1 = vector([5,8,2])
print(v+v1)
mul = v*v1
print(mul)