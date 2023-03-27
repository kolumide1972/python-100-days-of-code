class Car:
    def __init__(self,model):
        self.__model=model

    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model=model

car1=Car("TACOMA")
print(car1.model)