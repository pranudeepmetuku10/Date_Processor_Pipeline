from datetime import datetime

class DataProcessor:
    """Base class for all data processing operations."""
    
    def process(self, data):
        """Process the data and return the result."""
        raise NotImplementedError


class DateParser(DataProcessor):
    """Extract and parse dates from text entries."""
    
    def __init__(self, date_format="%Y-%m-%d"):
        self.date_format = date_format
    
    def process(self, entries):
        results = []
        for entry in entries:
            if not isinstance(entry, str):
                continue

            try:
                # Split into date and text parts
                date_str, text = entry.split(": ", 1)

                # Parse date
                date_obj = datetime.strptime(date_str, self.date_format)

                results.append({
                    'date': date_obj,
                    'text': text
                })

            except Exception:
                continue

        return results


class WeekdayFilter(DataProcessor):
    """Filter entries to keep only specific days of the week."""
    
    def __init__(self, allowed_days):
        self.allowed_days = allowed_days
    
    def process(self, entries):
        # entries contain dicts {date: datetime, text: str}
        filtered = []
        for entry in entries:
            day_name = entry['date'].strftime("%A")
            if day_name in self.allowed_days:
                filtered.append(entry)
        return filtered


class DateFormatter(DataProcessor):
    """Format dates into readable strings."""
    
    def __init__(self, output_format="%B %d, %Y"):
        self.output_format = output_format
    
    def process(self, entries):
        formatted_entries = []
        for entry in entries:
            formatted_date = entry['date'].strftime(self.output_format)
            formatted_entries.append(f"{formatted_date}: {entry['text']}")
        return formatted_entries


class ProcessingPipeline:
    """Chain multiple processors together."""
    
    def __init__(self, processors):
        self.processors = processors
    
    def process(self, data):
        result = data
        for processor in self.processors:
            result = processor.process(result)
        return result


'''
if __name__ == "__main__":
        # Test 1: DateParser basic functionality
    parser = DateParser(date_format="%Y-%m-%d")
    entries = ["2024-10-15: Event 1", "2024-10-16: Event 2"]
    result = parser.process(entries)
    print(f"Parsed {len(result)} entries")  # Should be 2

    # Test 2: DateParser with invalid entries
    parser = DateParser(date_format="%Y-%m-%d")
    entries = ["2024-10-15: Valid", "Not a date", "2024-10-16: Also valid"]
    result = parser.process(entries)
    print(f"Parsed {len(result)} entries")  # Should be 2 (skips invalid)

    # Test 3: WeekdayFilter
    filter = WeekdayFilter(allowed_days=['Monday'])
    entries = [
        {'date': datetime(2024, 10, 14), 'text': 'Monday'},
        {'date': datetime(2024, 10, 15), 'text': 'Tuesday'}
    ]
    result = filter.process(entries)
    print(f"Filtered to {len(result)} entries")  # Should be 1

    # Test 4: DateFormatter
    formatter = DateFormatter(output_format="%B %d")
    entries = [{'date': datetime(2024, 10, 15), 'text': 'Test'}]
    result = formatter.process(entries)
    print(result[0])  # Should be "October 15: Test"

    # Test 5: Full pipeline
    pipeline = ProcessingPipeline([
        DateParser(date_format="%Y-%m-%d"),
        WeekdayFilter(allowed_days=['Monday', 'Wednesday']),
        DateFormatter(output_format="%A, %B %d")
    ])
    logs = [
        "2024-10-14: Monday event",
        "2024-10-15: Tuesday event",
        "2024-10-16: Wednesday event"
    ]
    result = pipeline.process(logs)
    print(result)  # Should have 2 formatted entries (Monday and Wednesday)
    '''