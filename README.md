# Date Processing Pipeline

A modular Python pipeline for parsing, filtering, and formatting
date-based text logs.\
This project demonstrates a clean processor-pattern architecture useful
in ETL workflows, log analysis, and time-series preprocessing.

## Features

-   Extract dates from raw text strings
-   Filter entries by specified weekdays
-   Format dates into custom string formats
-   Chain multiple processors into a pipeline
-   Handles malformed or missing dates safely
-   Requires only the Python standard library

## Architecture
```
    Raw Logs
      ↓
    DateParser
    (Extract and validate timestamps)
      ↓
    WeekdayFilter
    (Retain specific weekdays)
      ↓
    DateFormatter
    (Convert to formatted text)
      ↓
    Final Processed Output

All processors inherit from a common `DataProcessor` base class and are
fully composable.
```

## Example Usage

``` python
from date_processor import *

pipeline = ProcessingPipeline([
    DateParser(date_format="%Y-%m-%d"),
    WeekdayFilter(allowed_days=["Monday", "Wednesday", "Friday"]),
    DateFormatter(output_format="%A, %B %d")
])

logs = [
    "2024-10-14: System backup completed",
    "2024-10-15: User registration spike",
    "2024-10-16: Database maintenance"
]

results = pipeline.process(logs)
print(results)
```

Expected Output:

    [
      "Monday, October 14: System backup completed",
      "Wednesday, October 16: Database maintenance"
    ]

## Project Structure
```
    date-processing-pipeline/
    │── date_processor.py        # Core pipeline implementation
    └── README.md
```

## Requirements

-   Python 3.8 or higher
-   No external libraries required (`datetime` module only)

## Extending the Pipeline

To add additional processing steps, create a class that inherits from
`DataProcessor`:

``` python
class CustomProcessor(DataProcessor):
    def process(self, data):
        # Custom transformation
        return data
```

Examples of useful extensions:

-   Removing weekends or holidays
-   Tagging dates with categories (workday, weekend, fiscal quarter)
-   Writing processed output to files or databases
-   Converting timestamps across time zones

## Testing Considerations

Key cases to validate:

  Scenario                      Expected Behavior
  ----------------------------- ------------------------------------
  Empty input                   Returns empty list
  Malformed log entries         Skipped safely
  Incorrect date format         Skipped without error
  Multiple processors chained   Produces correct sequential result

## License

This project is provided for educational and demonstration purposes.\
You may reuse and modify it freely.
