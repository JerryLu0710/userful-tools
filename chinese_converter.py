import os
import opencc
import argparse
import ebooklib
from lxml import etree
from ebooklib import epub

def convert_simplified_to_traditional_epub(epub_path):
    # Read the EPUB file
    book = epub.read_epub(epub_path)

    # Initialize the converter
    converter = opencc.OpenCC('s2hk')

    # Loop through all the items in the EPUB file
    for item in book.get_items():
        if item.get_type() in [ebooklib.ITEM_DOCUMENT, ebooklib.ITEM_NAVIGATION]:
            # Convert the content from Simplified Chinese to Traditional Chinese
            content = item.get_content().decode('utf-8')
            converted = converter.convert(content)
            item.content = converted.encode('utf-8')

    # Update the table of contents
    toc_item = book.get_item_with_id('ncx')
    if toc_item:
        toc_content = toc_item.get_content()
        toc_tree = etree.fromstring(toc_content)
        update_toc_content(toc_tree, converter)
        toc_item.content = etree.tostring(toc_tree, encoding='utf-8', xml_declaration=False)

    # Write the converted content to a new EPUB file
    new_epub_path = os.path.splitext(epub_path)[0] + '_traditional.epub'
    epub.write_epub(new_epub_path, book)

    print(f"Converted EPUB is saved as {new_epub_path}")

# Helper function to update the table of contents content
def update_toc_content(toc_tree, converter):
    # Update the text content of the table of contents
    for element in toc_tree.iter():
        if element.text:
            element.text = converter.convert(element.text)
        if element.tail:
            element.tail = converter.convert(element.tail)

    # Update the href attributes in the table of contents
    for element in toc_tree.iter('content'):
        href = element.get('src')
        if href:
            element.set('src', converter.convert(href))

def convert_simplified_to_traditional_text(input_file, output_file):
    # Convert encoding from Guobiao (GBK) to UTF-8
    with open(input_file, 'r', encoding='gbk') as file:
        guobiao_text = file.read()

    utf8_text = guobiao_text.encode('utf-8').decode('utf-8')

    # Convert Simplified Chinese to Traditional Chinese
    converter = opencc.OpenCC('s2hk')
    traditional_text = converter.convert(utf8_text)

    # Save as UTF-8 encoded file with Traditional Chinese text
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(traditional_text)

def convert_directory(directory_path):
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Get the full path of the file
        file_path = os.path.join(directory_path, filename)
        # Check if the file is an EPUB file
        if filename.endswith('.epub'):
            convert_simplified_to_traditional_epub(file_path)
        # Check if the file is a text file
        elif filename.endswith('.txt'):
            convert_simplified_to_traditional_text(file_path, os.path.splitext(file_path)[0] + '_traditional.txt')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Simplified Chinese to Traditional Chinese')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', type=str, help='Convert a single text file')
    group.add_argument('-e', '--epub', type=str, help='Convert a single EPUB file')
    group.add_argument('-d', '--directory', type=str, help='Convert all EPUB and text files in a directory')
    args = parser.parse_args()

    if args.file:
        convert_simplified_to_traditional_text(args.file, os.path.splitext(args.file)[0] + '_traditional.txt')
    elif args.epub:
        convert_simplified_to_traditional_epub(args.epub)
    elif args.directory:
        convert_directory(args.directory)