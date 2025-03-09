from rest_framework import serializers

def validate_csv_file(csv_file):
        """Validates the uploaded CSV file"""
        try:
            if not csv_file.name.endswith(".csv"):
                raise ValueError("Uploaded file must be a CSV.")

        except ValueError as e:
            raise serializers.ValidationError({"csv_file": str(e)})