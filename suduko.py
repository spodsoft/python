import functools
import time
from copy import deepcopy
import cellgroup as CellGroup
import cell as Cell


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug


class Cell:
    # Initialiser
    def __init__(self, theRow: CellGroup, theColumn: CellGroup, theZone: CellGroup):
        self.value  = None
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.row    = theRow
        self.column = theColumn
        self.zone   = theZone
        
        self.row.add(self)
        self.column.add(self)
        self.zone.add(self)
       
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
            self.zone.removeCellCandidate(theValue)
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
    
class CellGroup:
    
       # Initialiser
    def __init__(self, number=0):
        self.cells = []
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.complete = False
        self._number = number
        
        
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
    def number(self,theValue):
        self._number = theValue
    
    def getCell(self, index):
        return self.cells[index] 
    
    def containsValue(self,aValue):
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
        
        
    def getCandidates(self):
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

             
class Suduko:
    # Initialiser
    def __init__(self):
        self.rows = []
        self.columns = []
        self.zones = []
        
        for index in range(9):
            self.rows.append(CellGroup(index))
            self.columns.append(CellGroup(index))
            self.zones.append(CellGroup(index))
                 
        for row in range(9):                
            for column in range(9):
                newValue = Cell(self.rows[row], self.columns[column], self.zones[3 * int(row / 3) + int(column / 3)])
            
                
    def __str__(self):
        return f"{self.members.count}"
        
    def print(self):
        for row in range(9):
            rowString = ""
            for column in range(9):
                rowString = rowString + str(self.rows[row].getCell(column))
                if column==2 or column==5:
                    rowString = rowString + "|"
            print(rowString)                
            if row == 2 or row == 5:
                print("---+---+---")
        print("")
        
    def show(self):
        for row in range(9):
            rowString = ""
            for column in range(9):
                rowString = rowString + str(len(self.rows[row].getCell(column).getCandidates()))
                if column==2 or column==5:
                    rowString = rowString + "|"
            print(rowString)                
            if row == 2 or row == 5:
                print("---+---+---")
        print("")
        
    def getRow(self,row):
        return self.rows[row]
    
    def getColumn(self,column):
        return self.columns[column]
    
    def getZone(self,row,column):
        return self.zones[3 * int(row / 3) + int(column / 3)]
    
    def getCell(self,row,column):
        return self.rows[row].getCell(column)
    
    def setValue(self,row,column,value):
        self.rows[row].getCell(column).setValue(value)
        
    def setValues(self,row,newValues):
        index = 0
        for aValue in newValues:
            if aValue != 0:
                self.setValue(row,index, aValue)
            index = index + 1
            
    def review(self):
        for aRow in self.rows:
            aRow.processSingles()
        for aColumn in self.columns:
            aColumn.processSingles()
        for aZone in self.zones:
            aZone.processSingles()    
        
        for aRow in self.rows:
            aRow.processMandatorySingles()
        for aColumn in self.columns:
            aColumn.processMandatorySingles()
        for aZone in self.zones:
            aZone.processMandatorySingles()    
            
        for aRow in self.rows:
            aRow.processDoubles()
        for aColumn in self.columns:
           aColumn.processDoubles()
        for aZone in self.zones:
           aZone.processDoubles()                   
        
# Main
if __name__ == "__main__":
    puzzle = Suduko()

    puzzle.setValues(0,[0,0,0,0,1,0,5,0,0]);
    puzzle.setValues(1,[0,5,0,0,0,0,0,0,4]);
    puzzle.setValues(2,[0,8,0,2,0,5,0,3,0]);
    puzzle.setValues(3,[0,0,9,0,0,0,0,0,8]);
    puzzle.setValues(4,[0,2,0,0,3,0,0,5,0]);
    puzzle.setValues(5,[3,4,0,0,0,0,0,0,0]);
    puzzle.setValues(6,[0,3,0,0,0,2,0,7,0]);
    puzzle.setValues(7,[1,0,0,0,7,0,0,2,0]);
    puzzle.setValues(8,[0,0,7,8,4,0,0,0,0]);
    
    puzzle.print()

    for loop in range(9):
        puzzle.review()
        puzzle.print()

    puzzle.show()
    
    print(repr(puzzle.getRow(0).getCell(0)))

    #puzzle.setValues(0,[1,0,0,0,0,0,7,0,6]);
    #puzzle.setValues(1,[4,9,7,1,3,0,0,0,2]);
    #puzzle.setValues(2,[0,0,0,7,0,0,1,0,0]);
    #puzzle.setValues(3,[0,1,0,6,0,7,0,4,0]);
    #puzzle.setValues(4,[0,8,0,0,5,0,2,0,0]);
    #puzzle.setValues(5,[5,2,0,8,0,3,9,6,0]);
    #puzzle.setValues(6,[0,4,0,0,8,2,0,0,1]);
    #puzzle.setValues(7,[0,0,0,0,6,9,3,5,0]);
    #puzzle.setValues(8,[8,0,3,0,0,0,0,0,9]);
    
    
    #puzzle.setValues(0,[0,1,9,0,0,6,0,0,7]);
    #puzzle.setValues(1,[0,5,0,9,0,0,0,0,3]);
    #puzzle.setValues(2,[0,7,0,1,5,2,0,4,0]);
    #puzzle.setValues(3,[0,2,0,0,0,0,4,0,5]);
    #puzzle.setValues(4,[0,6,0,4,7,8,0,3,0]);
    #puzzle.setValues(5,[1,0,4,2,0,0,0,6,0]);
    #puzzle.setValues(6,[0,0,0,3,0,9,0,7,6]);
    #puzzle.setValues(7,[7,9,0,0,0,4,0,8,0]);
    #puzzle.setValues(8,[5,0,0,7,0,0,0,2,0]);
    
