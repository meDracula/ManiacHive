import unittest
from semantic import SemanticHandler

class TestSemantic(unittest.TestCase):
    def setUp(self):
        self.sprites_info = {1: ["<sprite>", ['East', 'West', 'North', 'South']]}

    def test_syntax_success(self):
        stdin = "1 East"
        expected = {1, 'East'}
        self.assertIsInstance(SemanticHandler.syntax(stdin, self.sprites_info), dict)
        self.assertTrue(SemanticHandler.syntax(stdin, self.sprites_info), expected) 

    def test_syntax_SyntaxError(self):
        expected = {1, 'East'}
        with self.assertRaises(SyntaxError):
                stdin = "1"
                SemanticHandler.syntax(stdin, self.sprites_info) 

    def test_grammer_success(self):
        sprites_info = {2: ["<sprite>", ['East', 'West', 'North', 'South']]}
        stdin = "2 North"
        expected = {2, 'North'}
        self.assertTrue(SemanticHandler.grammer(stdin, sprites_info), expected) 

    def test_grammer_TypeError(self):
        expected = {1, 'East'}
        with self.assertRaises(TypeError):
                stdin = "Q Down"
                SemanticHandler.grammer(stdin, self.sprites_info) 

        with self.assertRaises(TypeError):
                stdin = "1 Down"
                SemanticHandler.grammer(stdin, self.sprites_info) 

        with self.assertRaises(TypeError):
                stdin = "Q North"
                SemanticHandler.grammer(stdin, self.sprites_info) 

    def test_grammer_KeyError(self):
        #Sprites_info key = 1 => [...]
        expected = {1, 'East'}
        with self.assertRaises(KeyError):
                stdin = "2 East"
                SemanticHandler.grammer(stdin, self.sprites_info) 

    def test_grammer_IndexError(self):
        sprites_info = {1: ["<sprite>", ['North']]}
        expected = {1, 'North'}
        with self.assertRaises(IndexError):
                stdin = "1 East"
                SemanticHandler.grammer(stdin, sprites_info) 


if __name__ == '__main__':
    unittest.main()

