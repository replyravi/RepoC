import csv
import sys

def parse_warnings(log_file, output_csv):
    with open(log_file, "r") as infile, open(output_csv, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Line", "File", "Message"])

        for line in infile:
            parts = line.strip().split(": ")
            if len(parts) < 3:
                continue

            writer.writerow(parts)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python parser.py <log_file> <output_csv>")
        sys.exit(1)

    parse_warnings(sys.argv[1], sys.argv[2])
