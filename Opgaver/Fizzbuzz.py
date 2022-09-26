


for fizzbuzz in range(100):
    

    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
        
    elif fizzbuzz % 5 == 0:
        print("Buzz")
       
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    else:
        print(fizzbuzz)
  