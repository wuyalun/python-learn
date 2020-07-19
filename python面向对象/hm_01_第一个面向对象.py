class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
# 调用方法
tom.drink()
tom.eat()

print(tom)
addr = id(tom)
print("%d" % addr)
print("%x" % addr)