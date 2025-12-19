print ("x y z w")

"""for x in 0,1:
        for y in 0,1:
                for z in 0,1:
                        for w in 0,1:
                                if w and not((x<=y)<= (y==z))==1:
                                       print (x,y,z,w)"""
#w and not((x<=y)<= (y==z))==1
#w ∧ ¬((x → y) → (y ≡ z))                                
print ("x y z w")
for x in 0,1:
        for y in 0,1:
                for z in 0,1:
                        for w in 0,1:
                                if ((x == (w <= y)) and z)==1:
                                        print (x,y,z,w)
#(x ≡ (w → y)) ∧ z
