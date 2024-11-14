import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    
    def test_generate_random_list(self): 
        # Since the list is random, let's test for its length instead of exact content
        result = generate_random_list(9)
        self.assertEqual(len(result), 9)
        self.assertTrue(all(isinstance(num, int) for num in result))
    
    def test_find_max(self):
        self.assertEqual(find_max([6, 13, 17, 11, 3]), 17)
        self.assertEqual(find_max([-10, -20, -5]), -5)
    
    def test_find_min(self):
        self.assertEqual(find_min([6, 13, 17, 11, 3]), 3)
        self.assertEqual(find_min([-10, -20, -5]), -20)

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(find_average([10, 20, 30]), 20.0)

    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(find_even_numbers([7, 9, 11]), [])  # No even numbers
        self.assertEqual(find_even_numbers([10, 20, 30]), [10, 20, 30])  # All even numbers
        self.assertEqual(find_even_numbers([-4, -3, -2, -1, 0]), [-4, -2, 0])  # Handling negatives and zero

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)

    def test_return_list_stats(self):
        stats = return_list_stats([1, 2, 3, 4, 5])
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 5)
        self.assertEqual(stats["average"], 3.0)
        self.assertEqual(stats["even_numbers"], [2, 4])
        self.assertEqual(stats["odd_numbers"], [1, 3, 5])
        self.assertEqual(stats["number_of_even_numbers"], 2)
        self.assertEqual(stats["number_of_odd_numbers"], 3)

    def test_process_characters_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 3, 5])

    def test_process_characters_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 2, 3, 5])

    def test_process_characters_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c'])
        self.assertEqual(result_numbers, [1])

    def test_process_characters_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, [])
        self.assertEqual(result_numbers, [1, 2, 3])

    def test_generate_squared_dict(self):
        self.assertEqual(generate_squared_dict(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    def test_convert_word_list_sentence(self):
        sentence = "There is only one to fear and his name is Death."
        result = convert_to_word_list(sentence)
        self.assertEqual(result, ['there', 'is', 'only', 'one', 'to', 'fear', 'and', 
                                  'his', 'name', 'is', 'death'])

    def test_letters_count_sentence(self):
        text = "There is only one to fear and his name is Death."
        result = letters_count_map(text)
        self.assertEqual(result['a'], 4)
        self.assertEqual(result['t'], 6)

    def test_text_to_morse(self):
        self.assertEqual(text_to_morse("Hello World"), '.... . .-.. .-.. ---   .-- --- .-. .-.. -.. ')
        self.assertEqual(text_to_morse("SOS"), '... --- ...')

if __name__ == '__main__':
    unittest.main()