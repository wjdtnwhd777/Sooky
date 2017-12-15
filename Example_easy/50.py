class Myclass:
    var = 'False'
    def sayHi(self):
        print(str(self.var)+'!')
        param1 = "hi!"
        self.param2 = "hello!"
        print(param1)
        print(self.param2)
obj = Myclass()
print(obj.var+'!')
obj.var = 'True'
obj.sayHi()
