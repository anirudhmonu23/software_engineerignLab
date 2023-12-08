class WeatherModel:weatherModleing
    @staticmethod
    def quadratic_model(time, coefficients):
        a, b, c = coefficients
        temperature = a * (time ** 2) + b * time + c
        return temperature

def main():
    # Hard-coded coefficients
    coefficients = [0.1, -2, 10]

    # Example usage
    time_point = 3
    result = WeatherModel.quadratic_model(time_point, coefficients)
    print(f"Temperature at time {time_point} is {result} degrees Celsius.")

if __name__ == "__main__":
    main()
