class Block:
    # Good Luck!
    def __init__(self, args):
        self.width = args[0]
        self.length = args[1]
        self.height = args[2]
        
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.width * self.length * self.height
    
    def get_surface_area(self):
        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)