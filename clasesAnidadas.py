class Dept:
    def __init__(self, dname):
        self.dname = dname
    class Prof:
        
        def __init__(self,pname):
            self.pname = pname

class Dept2(Dept):
    class Meta:
        dname="Moises"
        def __init__(self,nom):
            self.name = nom
            
dep = Dept("Sistemas")
prof = Dept.Prof("Daniel")
print(dep.dname,prof.pname)
dep2 = Dept2("Ana")
dep2Meta = Dept2.Meta("Yady")

print(dep2.dname,dep2Meta.dname)
