class Car:
    DEFAULT_ID=None
    DEFAULT_NAME="unknown"
    DEFAULT_RUNNING=False
    DEFAULT_FUEL=0.0

    MAX_RANGE = 1000.0 # Same for all cars
    def __init__(self,memo={}): # constructor
        self._id = Car.DEFAULT_ID
        self._name = Car.DEFAULT_NAME
        self._running = Car.DEFAULT_RUNNING
        self._fuel = Car.DEFAULT_FUEL
        self.update(memo)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        if value == None:
            self._id = None
        else:
            self._id = int(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name=str(value)

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self,value):
        self._running = bool(int(value))

    @property
    def memo(self):
        return {'id': self._id,
                'name': self._name,
                'running': self._running,
                'fuel': self._fuel}

    def update(self,value):
        if 'id' in value:
            self.id = value['id']
        if 'name' in value:
            self.name = value['name']
        if 'running' in value:
            self.running = value['running']
        if 'fuel' in value:
            self.fuel = value['fuel']

    @property
    def fuel(self):
        return self._fuel
    
    @fuel.setter
    def fuel(self,value):
        if not (value != None and value==float(value)):
            raise ValueError(self._name + "fuel must be a float")
        if not (value >= 0 and value <= 1):
            raise ValueError(self._name + "fuel must be between 0 and 1")
        self._fuel = value

    def addFuel(self,amount):
        if amount < 0 or self._fuel + amount > 1.0:
            raise ValueError(self._name + ": invalid amount of fuel")
        self._fuel += amount

    def start(self):
        self._running = True

    def stop(self):
        self._running = False

    def drive(self,distance):
        if not self._running:
            raise ValueError(self._name + ": car is not running")
        if self._fuel * Car.MAX_RANGE < distance: 
            raise ValueError(self._name + ": insufficient fuel")
        self._fuel -= distance/Car.MAX_RANGE

    def __str__(self):
        return "car(id=" + str(self._id) + \
            ",name=" + self._name + \
            ",fuel=" + \
            str(self._fuel) + \
            ",running=" + str(self._running) + ")"
