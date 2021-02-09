try:
    f= open('simple.txt','w')
    f.write("Test write to simple text!")

except:
    print("ERROR: Could not read data")
#else:
 #   print("Success")
  #  f.close()
finally:

    print("I work always no matter what")