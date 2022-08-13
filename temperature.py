class Temperature:
    def __init__(self,celsius=0,fahrenheit=0):
        self.celsius= celsius;
        self.fahrenheit = fahrenheit;

    def convertToFahrenheit(self,celsius):
        self.fahrenheit = (celsius * 9/5) + 32;
        return self.fahrenheit;

    def convertToCelsius(self,fahrenheit):
        self.celsius = (fahrenheit -32) * (5/9);
        return self.celsius;


tem1 = Temperature();

print(tem1.convertToCelsius(100));
print(tem1.convertToFahrenheit(100));