import re

def read_dracula_conf(file_path):
    color_mapping = {}
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\w+)[\s]+#([\da-fA-F]{6})', line)
            if match:
                color_name = match.group(1).strip()
                hex_value = match.group(2).strip().upper()  # Convert hex to uppercase
                color_mapping[color_name] = hex_value
    return color_mapping

def read_template_xml(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def substitute_colors(template_content, color_mapping):
    for color_name, hex_value in color_mapping.items():
        placeholder = f'<{color_name}>'
        template_content = template_content.replace(placeholder, f'#{hex_value}')
    return template_content

def write_output_file(output_path, content):
    with open(output_path, 'w') as file:
        file.write(content)

def main():
    dracula_conf_path = './dracula.conf'
    template_xml_path = './template.xml'
    output_file_path = './royalts-dracula.rtcp'
    
    # Step 1: Read colors from dracula.conf
    color_mapping = read_dracula_conf(dracula_conf_path)

    # Step 2: Read template.xml content
    template_content = read_template_xml(template_xml_path)

    # Step 3: Substitute colors in the template
    output_content = substitute_colors(template_content, color_mapping)

    # Step 4: Write the output to the rtcp file
    write_output_file(output_file_path, output_content)
    
    print(f'Successfully created {output_file_path}')

if __name__ == '__main__':
    main()