import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_sort_large_input():
    # This test checks if the function returns 1 when >= 10 numbers are entered
    input_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # Call bubble_sort with SORT_ASCENDING (or SORT_DESCENDING, it doesn't matter here)
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    
    # Assert that the result is 1 as expected
    assert result == 1, f"Expected 1 for input size >= 10, but got {result}"
    
