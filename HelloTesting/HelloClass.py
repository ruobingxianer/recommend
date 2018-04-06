class testParagram:
    classPara = 0

    def __init__(self, var1):
        self.testPara = var1

    def addClassPara(self):
        testParagram.classPara += 1

    def addOnly(self):
        self.classPara += 1


test = testParagram("testing")
print test.testPara

test2 = testParagram("testing2")

test.addClassPara()
print test2.classPara

test2.addOnly()
print test2.classPara
print test.classPara

test2.addClassPara()
print test2.classPara
print test.classPara

print testParagram.__dict__
