# utility functions
def to_upper_case(text):
  return text.upper()

def to_lower_case(text):
  return text.lower()

# this is main file
if __name__ == "__main__":
  print(__name__, type(__name__))
  print(to_upper_case("Quinlan"))