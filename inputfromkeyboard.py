class WeatherModel:
  @staticmethod
  def quadratic_model(time, coefficients):
      # Quadratic equation: y = ax^2 + bx + c
      a, b, c = coefficients
      temperature = a * (time ** 2) + b * time + c
      return temperature

def get_user_input():
  # Get user input for coefficients
  a = float(input("Enter coefficient a: "))
  b = float(input("Enter coefficient b: "))
  c = float(input("Enter coefficient c: "))
  return [a, b, c]

def main():
  coefficients = get_user_input()
  time_point = float(input("Enter time point: "))
  result = WeatherModel.quadratic_model(time_point, coefficients)
  print(f"Temperature at time {time_point} is {result} degrees Celsius.")

if __name__ == "__main__":
  main()
