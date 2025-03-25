
#from .decorators import debug, deepcopy

class Cell:
    from  .cellgroup import CellGroup
    
    # Initialiser
    def __init__(self, theRow: CellGroup, theColumn: CellGroup, theBlock: CellGroup):
        self.value  = None
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.row    = theRow
        self.column = theColumn
        self.block   = theBlock
        
        self.row.add(self)
        self.column.add(self)
        self.block.add(self)
       
    def __str__(self):
        if self.value != None:
            return f"{self.value}"
        return "."
        
    def __repr__(self):
        row = self.row.number
        column = self.column.number
        
        if self.value != None:
            return f"<{self.__class__.__name__} location={row},{column} value={self.value}>"
        return f"<{self.__class__.__name__} location={row},{column} candidates={self.candidates}>"
    
 #   def __eq__(self, aValue):
 # #      if self.value == None:
 #           return False
 #       
 #       if isinstance(aValue,int):
 #           return self.value == aalue
 #       
  #      if isinstance(aValue, Value):
 #           return self.value == aValue.value
 #       
 #       return False
    
    def setValue(self,theValue):
        if ( self.value != None ):
            print(f"ERROR: SetValue {repr(self)} V={theValue}")
            return
        
        if ( theValue in self.candidates ):
            self.value = theValue
            self.candidates = []
            self.row.removeCellCandidate(theValue)
            self.column.removeCellCandidate(theValue)
            self.block.removeCellCandidate(theValue)
        else:
            print(f"ERROR: Fail set value of {theValue} on {repr(self)}")

        
    def getValue(self):
        return self.value
    
    def removeCandidate(self,theValue):
        if ( self.value != None ):
            return
        if ( theValue in self.candidates):
            self.candidates.remove(theValue)

        if ( len(self.candidates)== 0 ):  
            print(f"ERROR Fail remove value of {theValue} on {repr(self)}")
        
    def getCandidates(self):
        return self.candidates
    
    