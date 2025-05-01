class Animal:
    iq_index = 0
   
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
       
    def out_parent_param(self):
        return self.kind,self.name
    
class Bird(Animal):

    def __init__(self, name, wight,kind='Bird'):
        super().__init__(name, kind)
        self.wight= wight

    def out_self_param(self):
        return self.wight
    
class Fish(Animal):

    def __init__(self, name, debth,kind='Fish'):
        super().__init__(name, kind)
        self.debth= debth

    def out_self_param(self):
        return self.debth
    
class Zver(Animal):

    def __init__(self, name, chish,kind='Zver'):
        super().__init__(name, kind)
        self.chish= chish

    def out_self_param(self):
        return self.chish
    

class AnimalFactory(Animal):
   
    def __init__(self, animal_type, *args):
        super().__init__(name=args[0], kind=animal_type)
        self.animal_type= animal_type
    def create_animal(*args):
        if args[0]=='Bird':
            return Bird(args[1],args[2])
        elif args[0]=='Fish':
            return Fish(args[1],args[2])
        elif args[0]=='Zver':
            return Zver(args[1],args[2])
        else:
            return ValueError('Недопустиный тип')
    

if __name__ =='__main__':
    s=Bird('kesha',12)
    print(*s.out_parent_param(), s.out_self_param())
    s1=Fish('Kain',120)
    print(*s1.out_parent_param(), s1.out_self_param())
    s2=Zver('murka','щишник')
    print(*s2.out_parent_param(), s2.out_self_param())
    s3=AnimalFactory.create_animal('Zver','musa','траваядное')
    print(s3)
    print(*s3.out_parent_param(), s3.out_self_param())
