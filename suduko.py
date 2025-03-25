from suduko import *
             
class Suduko:
    # Initialiser
    def __init__(self):
        self.rows = []
        self.columns = []
        self.blocks = []
        
        for index in range(9):
            self.rows.append(CellGroup(index))
            self.columns.append(CellGroup(index))
            self.blocks.append(CellGroup(index))
                 
        for row in range(9):                
            for column in range(9):
                newValue = Cell(self.rows[row], self.columns[column], self.blocks[3 * (row // 3) + (column // 3)])
            
                
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
        
    def getRow(self,row: CellGroup) -> CellGroup:
        return self.rows[row]
    
    def getColumn(self,column: CellGroup) -> CellGroup:
        return self.columns[column]
    
    def getBlock(self,row: int ,column: int) -> CellGroup:
        return self.blocks[3 * (row // 3) + (column // 3)]
    
    def getCell(self,row: int,column: int) -> Cell:
        return self.rows[row].getCell(column)
    
    def setValue(self,row: int,column: int,value: int) -> None:
        self.rows[row].getCell(column).setValue(value)
        
    def setValues(self,row,newValues) -> None:
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
        for aZone in self.blocks:
            aZone.processSingles()    
        
        for aRow in self.rows:
            aRow.processMandatorySingles()
        for aColumn in self.columns:
            aColumn.processMandatorySingles()
        for aBlock in self.blocks:
            aBlock.processMandatorySingles()    
            
        for aRow in self.rows:
            aRow.processDoubles()
        for aColumn in self.columns:
           aColumn.processDoubles()
        for aBlock in self.blocks:
           aBlock.processDoubles()                   
        
# Main
if __name__ == "__main__":
    puzzle = Suduko()

    puzzle.setValues(0,[3,0,0,0,9,0,0,7,0]);
    puzzle.setValues(1,[0,0,5,0,0,1,2,6,0]);
    puzzle.setValues(2,[0,0,0,0,0,0,0,0,5]);
    puzzle.setValues(3,[0,0,2,6,0,9,0,0,7]);
    puzzle.setValues(4,[0,0,0,0,0,0,0,0,0]);
    puzzle.setValues(5,[4,0,0,3,2,0,6,0,0]);
    puzzle.setValues(6,[5,0,9,0,0,0,0,1,0]);
    puzzle.setValues(7,[0,6,7,9,0,0,8,0,0]);
    puzzle.setValues(8,[0,0,0,0,7,0,0,0,2]);
    
    puzzle.print()

    for loop in range(9):
        puzzle.review()
        puzzle.print()

    puzzle.show()
    
    print(repr(puzzle.getRow(0).getCell(0)))

    #puzzle.setValues(0,[0,0,0,0,1,0,5,0,0]);
    #puzzle.setValues(1,[0,5,0,0,0,0,0,0,4]);
    #puzzle.setValues(2,[0,8,0,2,0,5,0,3,0]);
    #puzzle.setValues(3,[0,0,9,0,0,0,0,0,8]);
    #puzzle.setValues(4,[0,2,0,0,3,0,0,5,0]);
    #puzzle.setValues(5,[3,4,0,0,0,0,0,0,0]);
    #puzzle.setValues(6,[0,3,0,0,0,2,0,7,0]);
    #puzzle.setValues(7,[1,0,0,0,7,0,0,2,0]);
    #puzzle.setValues(8,[0,0,7,8,4,0,0,0,0]);
    
    
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
    