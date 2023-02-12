from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self,sensor):

        self.depth  = 3

        if sensor == 0:
        
            self.string1 = '<material name="No Sensor">'

            self.string2 = '    <color rgba="0 0 1.0 1.0"/>'

            self.string3 = '</material>'

        else:
            self.string1 = '<material name="Sensor">'

            self.string2 = '    <color rgba="0 1.0 0 1.0"/>'

            self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
