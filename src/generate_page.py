from markdown_blocks import (
    markdown_to_html_node
)
from extract_markdown import (
    extract_title
)
import htmlnode

import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown_content = file.read()

    with open(template_path, "r") as file:
        template_content = file.read()

    title = extract_title(markdown_content) 
    html_nodes = markdown_to_html_node(markdown_content)
    html_content = html_nodes.to_html()


    updated_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Create any necessary directories if they don't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the updated content to the destination file
    with open(dest_path, "w") as file:
        file.write(updated_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """Recursively generate HTML pages for all markdown files in the content directory."""
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):  # Process markdown files only
                markdown_file_path = os.path.join(root, file)
                
                # Generate the path for the destination HTML file, preserving directory structure
                relative_path = os.path.relpath(markdown_file_path, dir_path_content)
                dest_file_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
                
                # Generate the page from the markdown and template
                generate_page(markdown_file_path, template_path, dest_file_path)
                print(f"Generated {dest_file_path}")