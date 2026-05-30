import csv

# Input file: original product data
input_file = "data/sample_products.csv"

# Output file: generated product titles
output_file = "outputs/generated_titles.csv"

# Open the input CSV file and read product data
with open(input_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    products = list(reader)

# Create generated titles
generated_rows = []

for product in products:
    product_name = product["product_name"]
    material = product["material"]
    structure = product["structure"]
    application = product["application"]
    keyword = product["keyword"]

    # Simple Made-in-China style title draft
    title = f"{material} {structure} {product_name} for {application} - {keyword}"

    generated_rows.append({
        "product_name": product_name,
        "generated_title": title
    })

# Write generated titles to output CSV file
with open(output_file, mode="w", encoding="utf-8", newline="") as file:
    fieldnames = ["product_name", "generated_title"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(generated_rows)

print("Title generation completed.")
print(f"Output file created: {output_file}")