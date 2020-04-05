import re as regex

content_file = """      =            
              X         
   :            
      x         
  n  
    r 
        y   
      Y            
              y        
     p    
         a       
 `          
            n            
          |    
  a          
o    
       h        
          `            
          g               
           o 
   z      """


lines = content_file.split("\n")
tab = []
for l in list(lines):
    match = regex.search(r'([^ ])', l)
    key = match.group(1) if match else ''
    values = regex.split(r'[^ ]', l)

    print(chr(int(str(ord(key))) + int(len(values[1]) - int(len(values[0])))), end="")
