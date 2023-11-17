import pytest
from sparse_recommender import SparseMatrix  

def test_set_get_value():
    sparse_matrix = SparseMatrix()
    sparse_matrix.set_value(0, 0, 5)
    assert sparse_matrix.get_value(0, 0) == 5

def test_set_invalid_index():
    sparse_matrix = SparseMatrix()
    with pytest.raises(IndexError):
        sparse_matrix.set_value(-1, 0, 5)

def test_get_missing_value():  
    sparse_matrix = SparseMatrix()
    with pytest.raises(KeyError):
        sparse_matrix.get_value(1, 1)

def test_recommend_valid():
    sparse_matrix = SparseMatrix()
    sparse_matrix.set_value(0, 0, 1) 
    sparse_matrix.set_value(1, 1, 2)
    sparse_matrix.set_value(2, 2, 3)
    
    user_vector = [0.5, 1.5, 2.5]
    result = sparse_matrix.recommend(user_vector)
    
    assert len(result) == 3
    assert result[0] == 0.5
    assert result[1] == 3.0
    assert result[2] == 7.5
    

def test_get_empty():
    sparse_matrix = SparseMatrix()
    with pytest.raises(KeyError):
        sparse_matrix.get_value(0, 0)
        
def test_recommend_large():
    sparse_matrix = SparseMatrix()
    sparse_matrix.set_value(0, 0, 1)
    sparse_matrix.set_value(1, 1, 1)
    sparse_matrix.set_value(2, 2, 1)
    
    user_vector = [2, 2, 2]
    recommendation = sparse_matrix.recommend(user_vector)
    
    
    assert len(recommendation) == 3
    assert recommendation[0] == 2
    assert recommendation[1] == 2
    assert recommendation[2] == 2

