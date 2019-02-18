import c4d
from c4d import gui
from random import randint

def main():
   op = c4d.documents.GetActiveDocument()
   sel = op.GetActiveObjects(0)
   
   if len(sel) > 0:
    for ob in sel:
        
        cd_r = randint(0, 255) / 256.0
        cd_g = randint(0, 255) / 256.0
        cd_b = randint(0, 255) / 256.0
        color = c4d.Vector(cd_r,cd_g,cd_b)
        
        ob[c4d.ID_BASEOBJECT_USECOLOR] = True
        ob[c4d.ID_BASEOBJECT_COLOR] = color
        ob[c4d.NULLOBJECT_ICONCOL] = True
        
        c4d.EventAdd()
        
        
if __name__=='__main__':
    main()
    
