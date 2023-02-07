from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self):

        self.depth  = 3

        self.string1 = '<material name="King Crab">'

        self.string2 = '    <color rgba="0.8 0.496 0.516 1.0"/>'

        self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
