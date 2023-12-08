class WeatherModel:
  @staticmethod
  def quadratic_model(time, coefficients):
      # Quadratic equation: y = ax^2 + bx + c
      a, b, c = coefficients
      temperature = a * (time ** 2) + b * time + c
      return temperature

def read_coefficients_from_file(file_path):
  # Read coefficients from file
  with open(file_path, "r") as file:
      coefficients = [float(coef) for coef in file.readline().split()]
  return coefficients

def main():
  coefficients = read_coefficients_from_file("coefficients.txt")
  time_point = float(input("Enter time point: "))
  result = WeatherModel.quadratic_model(time_point, coefficients)
  print(f"Temperature at time {time_point} is {result} degrees Celsius.")

if __name__ == "__main__":
  main()
