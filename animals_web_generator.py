import json


def load_data(file_path):
    """Loads animal data from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


def generate_animal_html(animal):
    """Generates structured HTML for each animal."""
    html = '<li class="cards__item">\n'
    html += f'  <div class="card__title">{animal["name"].upper()}</div>\n'
    html += '  <div class="card__text">\n'
    html += '    <ul>\n'

    # Adding animal characteristics
    if "diet" in animal["characteristics"]:
        html += f'      <li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>\n'
    if "skin_type" in animal["characteristics"]:
        html += f'      <li><strong>Skin Type:</strong> {animal["characteristics"]["skin_type"]}</li>\n'
    if "type" in animal["characteristics"]:
        html += f'      <li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>\n'
    if "lifespan" in animal["characteristics"]:
        html += f'      <li><strong>Lifespan:</strong> {animal["characteristics"]["lifespan"]}</li>\n'
    if "color" in animal["characteristics"]:
        html += f'      <li><strong>Color:</strong> {animal["characteristics"]["color"]}</li>\n'

    # Adding location(s)
    if "locations" in animal and animal["locations"]:
        html += f'      <li><strong>Location:</strong> {", ".join(animal["locations"])}</li>\n'

    # Adding scientific name
    if "scientific_name" in animal["taxonomy"]:
        html += f'      <li><strong>Scientific Name:</strong> {animal["taxonomy"]["scientific_name"]}</li>\n'

    html += '    </ul>\n'
    html += '  </div>\n'
    html += '</li>\n'

    return html


def main():
    """Main function to generate the animals.html file."""
    # Load animal data from JSON
    animals = load_data("animals_data.json")

    # Read the HTML template
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # Generate HTML for all animals
    animals_html = "\n".join(generate_animal_html(animal) for animal in animals)

    # Replace placeholder in template
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write final output to animals.html
    with open("animals.html", "w") as output_file:
        output_file.write(final_html)

    print("✅ animals.html has been successfully generated!")


if __name__ == "__main__":
    main()

# bonus feuture