import json

# Load JSON data from a file
def load_data(file_path):
    """Loads JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)

# Generate HTML content for each animal
def serialize_animal(animal):
    """Converts animal data into an inline-styled HTML list item."""
    return f"""
    <li style="background: white; padding: 20px; border-radius: 10px; 
               box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2); width: 80%; 
               max-width: 600px; text-align: left; margin-bottom: 20px;">
        <div style="font-size: 22px; font-weight: 400; margin-bottom: 10px; 
                    text-transform: uppercase; color: #444;">
            {animal['name'].upper()}
        </div>
        <div>
            <ul style="padding: 0; margin: 0; list-style-type: none;">
                <li><strong>Diet:</strong> {animal['characteristics'].get('diet', 'Unknown')}</li>
                <li><strong>Skin Type:</strong> {animal['characteristics'].get('skin_type', 'Unknown')}</li>
                <li><strong>Type:</strong> {animal['characteristics'].get('type', 'Unknown')}</li>
                <li><strong>Lifespan:</strong> {animal['characteristics'].get('lifespan', 'Unknown')}</li>
                <li><strong>Color:</strong> {animal['characteristics'].get('color', 'Unknown')}</li>
                <li><strong>Location:</strong> {', '.join(animal.get('locations', ['Unknown']))}</li>
                <li><strong>Scientific Name:</strong> {animal['taxonomy'].get('scientific_name', 'Unknown')}</li>
            </ul>
        </div>
    </li>
    """

# Generate the final HTML file
def generate_html(data):
    """Generates the animals.html file from a template."""
    template_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Animal Repository</title>
    </head>
    <body style="background-color: #ffe6e6; text-align: center; font-family: Arial, sans-serif; padding: 20px;">
        <h1 style="font-size: 36px; font-weight: bold; color: black;">My Animal Repository</h1>
        <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; align-items: center; gap: 20px;">
            {"".join(serialize_animal(animal) for animal in data)}
        </ul>
    </body>
    </html>
    """

    # Write the final HTML output
    with open("animals.html", "w") as output_file:
        output_file.write(template_content)

# Main execution
if __name__ == "__main__":
    animals_data = load_data("animals_data.json")  # Load the JSON data
    generate_html(animals_data)  # Generate the final HTML
    print("✅ animals.html has been generated successfully!")