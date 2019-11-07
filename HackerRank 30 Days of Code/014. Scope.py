class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        abs_list=[]
        for i in self.__elements:
            for j in self.__elements:
                abs_list.append(abs(i-j))
            
        self.maximumDifference=max(abs_list)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
