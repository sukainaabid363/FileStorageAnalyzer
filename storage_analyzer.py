
from pathlib import Path
import csv


def analyze_storage(folder_path):
    """Analyze files, calculate storage usage, and export a CSV report."""

    folder = Path(folder_path)

    # Check whether the folder exists
    if not folder.exists() or not folder.is_dir():
        print("Error: Please enter a valid folder path.")
        return

    total_size = 0
    file_count = 0
    file_types = {}
    file_sizes = []
    file_records = []

    print("\n--- FILE STORAGE ANALYZER ---\n")

    # Scan all files in the folder and its subfolders
    for file in folder.rglob("*"):
        if file.is_file():
            try:
                size = file.stat().st_size
            except OSError:
                print("Could not access:", file.name)
                continue

            total_size += size
            file_count += 1

            # Store file size information
            file_sizes.append((file.name, size))

            # Group storage by file extension
            extension = file.suffix.lower() or "No extension"
            file_types[extension] = (
                file_types.get(extension, 0) + size
            )

            # Store details for the CSV report
            file_records.append({
                "File Name": file.name,
                "File Path": str(file.resolve()),
                "File Type": extension,
                "Size (Bytes)": size
            })

            print(f"{file.name} - {size} bytes")

    # Display total storage summary
    print("\n--- STORAGE SUMMARY ---")
    print("Total files:", file_count)
    print("Total storage:", round(total_size / 1024, 2), "KB")

    # Display storage by file type
    print("\n--- STORAGE BY FILE TYPE ---")

    for extension, size in sorted(file_types.items()):
        print(extension, ":", round(size / 1024, 2), "KB")

    # Display the five largest files
    print("\n--- LARGEST FILES ---")

    largest_files = sorted(
        file_sizes,
        key=lambda item: item[1],
        reverse=True
    )

    if largest_files:
        for name, size in largest_files[:5]:
            print(name, "-", round(size / 1024, 2), "KB")
    else:
        print("No files found.")

    # Ask whether the user wants to export a CSV report
    choice = input(
        "\nDo you want to save a CSV report? (yes/no): "
    ).strip().lower()

    if choice in ("yes", "y"):
        report_path = input(
            "Enter the CSV report path "
            "(example: storage_report.csv): "
        ).strip()

        if not report_path:
            report_path = "storage_report.csv"

        try:
            with open(
                report_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as csv_file:
                fieldnames = [
                    "File Name",
                    "File Path",
                    "File Type",
                    "Size (Bytes)"
                ]

                writer = csv.DictWriter(
                    csv_file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(file_records)

            print("\nCSV report saved successfully!")
            print("Report location:", Path(report_path).resolve())

        except OSError as error:
            print("Could not save the report:", error)

    else:
        print("\nCSV report was not created.")

    print("\nAnalysis completed!")


# Start the program
folder_path = input(
    "Enter the folder path to analyze: "
)

analyze_storage(folder_path)

