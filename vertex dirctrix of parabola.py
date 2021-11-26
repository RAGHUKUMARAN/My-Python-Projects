def parabola(a, b, c): 
    print ("Vertex: (" , (-b / (2 * a)) , ", "
        ,(((4 * a * c) - (b * b)) / (4 * a)) , ")" ) 
          
    print ("Focus: (" , (-b / (2 * a)) , ", "
        , (((4 * a * c) - (b * b) + 1) / (4 * a)) , ")" ) 
      
    print ("Directrix: y="
            , (int)(c - ((b * b) + 1) * 4 * a ))     
      
       
a = int(input("enter the value of a :- "))
b = int(input("enter the value of b :- "))
c = int(input("enter the value of c :- "))
  
parabola(a, b, c) 
