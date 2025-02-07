"""
This script creates "blank" versions of Jupyter notebooks by removing solution content.
It processes notebooks ending in _master.ipynb and creates corresponding _blank.ipynb files
with solution sections removed.

Based on work by Zach del Rosario (https://github.com/zdelrosario/jupyter-authoring)

Author: Ry Nduma
Date: 2024/10/31
"""

# Import required libraries
import os
import sys
import nbformat
import re
from copy import deepcopy
from datetime import datetime


def process_notebook(filename_orig):
    """
    Process a master notebook to create a blank version with solutions removed.

    Args:
        filename_orig (str): Path to the master notebook file
    """
    # Create blank notebook filename by replacing 'master' with 'blank'
    filename_blank = filename_orig.replace("master", "blank")

    # Load and create copies of the notebook
    nb_orig = nbformat.read(filename_orig, as_version=4)
    nb_blank = deepcopy(nb_orig)

    # Process each cell in the notebook
    for cell_id, cell_orig in enumerate(nb_orig["cells"]):
        text_blank = cell_orig["source"]

        # Handle markdown and code cells
        if cell_orig["cell_type"] in ["markdown", "code"]:
            # Remove HTML-style solution blocks
            text_blank = re.sub(
                "<!-- solution-begin -->(\n|.)*?<!-- solution-end -->\n?",
                "",
                text_blank,
            )
            # Remove Python comment-style solution blocks
            text_blank = re.sub(
                "# solution-begin(\n|.)*?# solution-end", "", text_blank
            )
        else:
            raise ValueError(f"Unrecognized cell type {cell_orig['cell_type']}.")

        # Update the blank notebook with processed content
        nb_blank["cells"][cell_id]["source"] = text_blank

    # Save the blank notebook
    nbformat.write(nb_blank, filename_blank)
    print(
        f"{os.path.basename(filename_orig)} successfully scrubbed! Blank notebook created."
    )


def main():
    """Main function to handle command line interface and process notebooks."""
    # Validate command line arguments
    if len(sys.argv) != 2:
        print("Usage: python make_blank_nb.py [dirname]")
        sys.exit(1)

    print(f"Starting cleaning at {datetime.now()}")
    dirname = sys.argv[1]

    # Process all master notebooks in directory
    for filename in os.listdir(dirname):
        if filename.endswith("_master.ipynb"):
            process_notebook(os.path.join(dirname, filename))


if __name__ == "__main__":
    main()
