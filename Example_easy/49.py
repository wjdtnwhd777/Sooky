class Myclass:
    var = 'False'
    def sayHi(self):
        print(str(self.var)+'!')

obj = Myclass()
print(obj.var+'!')
obj.var = 'True'
obj.sayHi()
