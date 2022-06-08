# Finding matches in schedules of the workers

## Instructions

Once you download the repo run the following line in your terminal to test the script with the dummy data:

```bash
python main.py
```

If you want to test the script with test data:

1. Go to "main.py" file
2. Change the line "file_name = 'data.txt'" for "file_name = 'data.txt'"
3. Run the following line:

```bash
python generate_txt.py && python main.py
```

## Overwiew of the solution

The repo first generate a txt file in the same format as the examples. The days and hours for each employee were selected from the examples, for days worked the range was 3~5 days and for the hours the interval was 8 hours worked.

Then the dataset is imported it's treated to generate a list of dictionaries for each employee then to get the results asked in the exercise, it do combinations to get the matches between the employees.

## Explanation of the approach

First generate the results as i wanted to see which was the best way to analyze the txt file and that was a list of dictionaries because we can access it's elements way more easy using comprehension lists than an entire dictionary. Then with a generated dummy dataset in the desired way I started to work to get the combinations for each employee name, and once obtained compare the day-hours-pairs for each one to see if there's a match.
Once the desired result is obtained, the solution shift to start generating the scripts to import, read the file and treat it to get the names and pairs of d-h to build the list of dictionaries and then implement the solution with the generated dataset.
