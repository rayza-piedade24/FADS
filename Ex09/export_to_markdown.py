from nbconvert import MarkdownExporter
import nbformat
import sys
import os

# Get the input file from the command line
if len(sys.argv) != 2:
    print("Usage: python export_to_markdown.py <notebook_file.ipynb>")
    sys.exit(1)

notebook_path = sys.argv[1]
output_path = os.path.splitext(notebook_path)[0] + ".md"

# Load the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Export to Markdown
markdown_exporter = MarkdownExporter()
(body, resources) = markdown_exporter.from_notebook_node(notebook)

# Save the Markdown file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(body)

print(f"Exported {notebook_path} to {output_path}")
