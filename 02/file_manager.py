class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.path = rf'D:\coding projects\miw\02\text files\{file_name}'
        print(self.path)
            
    def readFile(self):
        fileLines = self.getLines()
        
        return ''.join(fileLines)
            
    def getLines(self):
        try:
            result = list()
            
            with open(self.path, 'r', encoding='utf-8') as fileReader:
                for line in fileReader:
                    result.append(line)
                    
            return result
        except IOError as error:
            print(f'Failed to read the file: {error}')

    def updateFile(self, text_data):
        try:
            hook = open(self.path, 'w', encoding='utf-8')
                
            hook.write(text_data)
            
            hook.close()
            
            return
        except Exception as error:
            print(f'Failed to write to the file: {error}')
        
        return
    