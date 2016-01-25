# ballot_ready

#requires python3 and numpy

#commandline input used for tests with virtualenv: env/bin/python3 mechanical_turk_processor.py "sample.csv" "AB" "AC" "AE" "BC" "test.csv"

#command line input example: python3 mechanical_turk_processor.py "sample.csv" "AB" "AC" "AE" "BC" "test.csv"

#command line input general format: python3 mechanical_turk_processor.py "name/and/path/of/csvfile_you_are_taking_data_from_in_quotes.csv" "alphacode_for_column_with_first_names" "alphacode_for_column_with_last_names" "alphacode_for_column_where_data_starts" "alphacode_for_last_column_of_data" "file/path/and/name/for/new/file/to/be/created.csv"