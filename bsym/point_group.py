from bsym import SymmetryGroup

class PointGroup( SymmetryGroup ):

    def __repr__( self ):
        to_return = 'PointGroup\n'
        for so in self.symmetry_operations:
            to_return += f"{so.label}\t{so.as_vector()}\n"
        return to_return