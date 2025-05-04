

MARS_MULTIPLE = 0.378  #constant 

def main():
    
    earth_weight = input("Enter your weight on Earth: ")
    
    earht_weight_float = float(earth_weight)
    
    mars_weight = earht_weight_float * MARS_MULTIPLE
    
    print("your weight on mars is: " + str(mars_weight))
  



if __name__ == '__main__':
    main()


 