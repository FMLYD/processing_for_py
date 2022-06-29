class Mover:
    def __init__(self,x,y):
        self.location = PVector(x, y)
        self.r = 12
        self.maxspeed = 100
        self.maxforce =0.1
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
    def applyForce(self,force) :
        self.acceleration.add(force)
    def applyBehaviors(self,lst):
        separateForce = self.separate(lst)
        separateForce.mult(2)
        self.applyForce(separateForce)
    def seek(self,target):
        desired = PVector.sub(target,self.location)
        if desired.mag()<100:
            return PVector (0,0)
        desired.normalize()
        desired.mult(self.maxspeed)
        steer = PVector.sub(desired,self.velocity)
        steer.limit(self.maxforce)
        return steer
    def separate(self,lst):
        desiredseparation = self.r*10
        sum = PVector(0,0)
        count = 0
        for other in lst :
            d = PVector.dist(self.location, other.location)
                
            if d > 0 and d < desiredseparation :
                
                diff = PVector.sub(self.location, other.location)
                diff.normalize()
                diff.div(d)
                sum.add(diff)
                count+=1
        if count > 0 :
            sum.div(count)
            sum.normalize()
            sum.mult(self.maxspeed)
            sum.sub(self.velocity)
            sum.limit(self.maxforce)
        return sum
    def update(self):
        self.velocity.add(self.acceleration)
  
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        if self.location.x<0 or self.location.x>width:
            self.velocity.x=-self.velocity.x
        if self.location.y<0 or self.location.y>height:
            self.velocity.y=-self.velocity.y
        self.acceleration.mult(0)
    def display(self) :
        fill(100,100,255,1000)
        noStroke()
        pushMatrix()
        translate(self.location.x, self.location.y)
        ellipse(0, 0, self.r, self.r)
        popMatrix()
class StarManager:
    def __init__(self):
        a=[0]
        a=a*10
        self.matrix=[a]*10
        self.stars=[]
        num=random(10)
        for x in range(int(10)):
            stars+=[Star()]
        self.update()
    def update(self,movers):
        for m in movers:
            i,j=m.location.x//10,m.location.y//10
            
class StarShip:
    def __init__(self,x,y):
        self.location = PVector(x, y)
        self.r = 50
        self.maxspeed = 10
        self.maxforce =0.1
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
    def applyForce(self,force) :
        self.acceleration.add(force)
    def applyBehaviors(self,lst):
        separateForce = self.separate(lst)
        separateForce.mult(2)
        self.applyForce(separateForce)
    def seek(self,target):
        desired = PVector.sub(target,self.location)
        if desired.mag()<100:
            return PVector (0,0)
        desired.normalize()
        desired.mult(self.maxspeed)
        steer = PVector.sub(desired,self.velocity)
        steer.limit(self.maxforce)
        return steer
    def separate(self,lst):
        desiredseparation = self.r*2
        sum = PVector(0,0)
        count = 0
        for other in lst :
            d = PVector.dist(self.location, other.location)
            if d > 0 and d < desiredseparation :
                diff = PVector.sub(self.location, other.location)
                diff.normalize()
                diff.div(d)
                sum.add(diff)
                count+=1
        if count > 0 :
            sum.div(count)
            sum.normalize()
            sum.mult(self.maxspeed)
            sum.sub(self.velocity)
            sum.limit(self.maxforce)
        return sum
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        if self.location.x<0 or self.location.x>width:
            self.velocity.x=-self.velocity.x
        if self.location.y<0 or self.location.y>height:
            self.velocity.y=-self.velocity.y
        self.acceleration.mult(0)
    def display(self) :
        fill(100,100,255,1000)
        noStroke()
        pushMatrix()
        translate(self.location.x, self.location.y)
        ellipse(0, 0, self.r, self.r)
        popMatrix()
def setup():
    global m,x
    smooth()
    size(1000,1000)
    m=[]
    for x in range(150):
        m+=[Mover(random(width),random(height))]
def draw():
    global m,x
    fill(255,20)
    rect(0,0,width,height)
    for x in m:
        x.applyBehaviors(m)
        x.update()
        x.display()
    
