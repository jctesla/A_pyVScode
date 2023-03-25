
def main():
   print(f"First Modul's Name :{__name__}")                         # Run from import of second Modul's Name :firstModule


if __name__ == '__main__':
  print(f"Run from A Modul's Name :{__name__}")            # result = __main__
  # main()
else:
  print(f"Run from B Modul's Name :{__name__}")         # result = __main__