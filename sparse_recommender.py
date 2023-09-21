class SparseMatrix:

    def __init__(self):
        self.matrix = {}
        self.rows = 0
        self.cols = 0

    def set_value(self, row, col, value):
        
        
        if row < 0 or col < 0:
            raise IndexError()
            
        
        self.rows = max(self.rows, row+1)
        self.cols = max(self.cols, col+1)
        
        
        self.matrix[(row, col)] = value

    def get_value(self, row, col):
       
        
        if (row, col) not in self.matrix:
            raise KeyError()
            
        return self.matrix[(row, col)]

    def recommend(self, user_vector):
        
       
        if len(user_vector) != self.cols:
            raise ValueError()
            
        recommendation = []
        
        
        for row in range(self.rows):
            dot_product = 0
            for col, value in enumerate(user_vector):
                try:
                    dot_product += value * self.get_value(row, col)
                except KeyError:
                    pass
                    
            recommendation.append(dot_product)
            
        return recommendation
