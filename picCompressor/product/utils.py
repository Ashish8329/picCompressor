from rest_framework import serializers
import csv
import io

def validate_csv_file(csv_file):
    """Validates the uploaded CSV file"""
    try:
        if not csv_file.name.endswith(".csv"):
            raise ValueError("Uploaded file must be a CSV.")
        
        # Read and decode file (Django's InMemoryUploadedFile or TemporaryUploadedFile)
        decoded_file = csv_file.read().decode('utf-8')
        file_io = io.StringIO(decoded_file)  # Convert string to file-like object

        reader = csv.reader(file_io)
        header = next(reader, None)  # Read the first row (header)
        
        if header is None or len(header) != 2:
            raise ValueError("Error: handling CSV data, make sure the CSV data is in the provided format.")

    except (ValueError, UnicodeDecodeError) as e:
        raise serializers.ValidationError({"csv_file": str(e)})
