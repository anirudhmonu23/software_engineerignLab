class WeatherModel:
  @staticmethod
  def quadratic_model(time, coefficients):
      # Quadratic equation: y = ax^2 + bx + c
      a, b, c = coefficients
      temperature = a * (time ** 2) + b * time + c
      return temperature

def read_coefficients_from_file(file_path):
  # Read coefficients from file for multiple sets
  with open(file_path, "r") as file:
      coefficients_list = [list(map(float, line.split())) for line in file.readlines()]
  return coefficients_list

def main():
  coefficients_list = read_coefficients_from_file("coefficients_multi.txt")
  time_point = float(input("Enter time point: "))
  for i, coefficients in enumerate(coefficients_list, 1):
      result = WeatherModel.quadratic_model(time_point, coefficients)
      print(f"Set {i}: Temperature at time {time_point} is {result} degrees Celsius.")

if __name__ == "__main__":
  main()
