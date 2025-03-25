
from .decorators import debug, deepcopy

class CellGroup:
    
       # Initialiser
    def __init__(self, number=0):
        self.cells = []
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.complete = False
        self._number = number
        
        # Delayed import
        from .cell import Cell
        
    @debug   
    def __copy__(self):
        print("GROUP COPY") 
        return None
               
    def __str__(self):
        return f"Group {self.number} {len(self.cells)}"
        
    def __repr__(self):
        return f"<{self.__class__.__name__} complete={self.complete},members={self.cells}>"
    
    def add(self,aCell):
        self.cells.append(aCell)

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self,theValue) -> None:
        self._number = theValue
    
    def getCell(self, index) -> any:
        return self.cells[index] 
    
    def containsValue(self,aValue) -> bool:
        for aCell in self.cells:
            if aCell.getValue() == aValue:
                return True
        return False
    
    def cellsWithCandidateValue(self,aValue):
        result = []
        for aCell in self.cells:
            if ( aValue in aCell.getCandidates() ):
                result.append(aCell)
        return result
        
    def removeCellCandidate(self,aValue):
        if ( aValue in self.candidates ):
            self.candidates.remove(aValue)
            if (len(self.candidates) == 0):
                self.complete = True
        for aCell in self.cells:
            aCell.removeCandidate(aValue)
        
        
    def getCandidates(self) -> list:
        return self.candidates
    
    def processMandatorySingles(self):
        for number in self.candidates:
            cellList = self.cellsWithCandidateValue(number)
            if ( len(cellList) == 1):
                cellList[0].setValue(number)
    
    def processSingles(self):
        for aCell in self.cells:
            if ( aCell.getValue() == None ):
                candidates = aCell.getCandidates()
                if ( len(candidates) == 1 ):
                    aCell.setValue(candidates[0])
                    
    def processDoubles(self):
        pairs = []
        for aCell in self.cells:
            if ( aCell.getValue() == None ):
                candidates = aCell.getCandidates()
                if ( len(candidates) == 2 ):
                    pairs.append(aCell)                            
        #pairs2 = list(pairs)
        
        for aValue1 in pairs:
            for aValue2 in pairs:
                if ( aValue1 != aValue2 ):
                    if ( aValue1.getCandidates() == aValue2.getCandidates() ):
                        
                        c1 = aValue1.getCandidates()[0]
                        c2 = aValue1.getCandidates()[1]
                        for aValue3 in self.cells:
                            if ( aValue1 != aValue3 ) and ( aValue2 != aValue3):
                                aValue3.removeCandidate(c1)
                                aValue3.removeCandidate(c2)
                                
                                