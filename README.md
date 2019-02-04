# Checkpoint 1

# CODECOOL MUSIC LIBRARY ver. 0.7

Codecoolers want to play some music during breaks. They need your help to manage their music library.

## Running program

To run all tests with tests' names instead of '.', 'F' or 'E' at the beginning use:

`python3 tests.py -v`

To run tests and stop at first failing use:

`python3 tests.py -f`

To run the program itself use:

`python3 main_program.py`



## Structure

CODECOOL MUSIC LIBRARY structure consists of these modules:

#### To modify

_file_handling.py_ - importing and exporting data from/to file

_music_reports.py_ - generating reports from given data

_main_program.py_ - handling user interactions

#### To not modify

_tests.py_ - unit tests - ***DO NOT MODIFY***

_test_helpers.py_ - helper functions used in tests - ***DO NOT MODIFY***

_display.py_ - printing data on screen - ***you may only change the body of print_program_menu function if you use another data structure***


## Data

Program has to import .txt file with values separated by commas. Each line of file represents album data in given order:

`artist name,album name,release year,genre,length`

Data exported to file should have the same format.

For your implementation operate only on _albums_data.txt_ Rest of .txt files are for testing purposes only - **DO NOT MODIFY THEM!**


## General info about requirements

Passing tests is something you need to get 10 points. However, if during manual testing we find errors not found by tests from _tests.py_, you will not get max points for requirements.

## Requirements

1. Implement all functions from file_handling, music_reports and main_program modules
2. Code must pass all tests
3. Every empty function should be implemented as it was described in docstrings - **PLEASE READ THEM CAREFULLY**
4. Don't use built-in function `print()` in _file_handling_ and _music_reports_ modules
5. Menu in _main_program_ module offers at least 4 options for user (you can choose which one from _music_reports_ or _main_program_ module, for instance: 1. Delete album, 2. Get albums by genre,  3. Display oldest album, 4. Show genre stats)
6. At least one function should be foolproof
7. At least one function should be able to handle potential exceptions (you can choose which one)
8. Use functions from _display_ module to display data and menu, but only in _main_program_
9. If you read this last requirement, smile and keep your head up! You can do it! :)

NOTE:
You can add your own functions to any module if you feel they are needed to make your code cleaner.
You may add test cases for the extra functions you write.

