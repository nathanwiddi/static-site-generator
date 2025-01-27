from static_to_public import copy_directory_recursive
from generate_page import generate_pages_recursive

def main():
    # Call methods or perform actions
    source_directory = "static"
    destination_directory = "public"
    copy_directory_recursive(source_directory, destination_directory)
    
    # Generate a page from index.md using template.html and write to public/index.html
    # from_path = "content/index.md"
    # template_path = "template.html"
    # dest_path = "public/index.html"
    # generate_page(from_path, template_path, dest_path)

    dir_path_content = "content"
    template_path = "template.html"
    dest_dir_path = "public"
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
    

if __name__ == "__main__":
    main()
