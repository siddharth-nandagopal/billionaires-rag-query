# Billionaires RAG Query

## Overview

`Billionaires RAG Query` is a Retrieval-Augmented Generation (RAG) framework designed to ingest and analyze the world's billionaires list, including details such as names, net worth, age, nationality, and primary sources of wealth. This project demonstrates how to use LLMs to interpret structured tabular data within textual documents, providing precise answers to queries about the wealthiest individuals.

## Key Features

- **Ingest Billionaires Data**: Extract data from the world's billionaires list, including key attributes like name, net worth, age, nationality, and primary sources of wealth.
- **Enhanced Query Resolution**: Use structured data as context for LLMs to answer complex questions about billionaires, such as "Who is the richest person in 2023?" or "What is the net worth of the sixth richest billionaire?".
- **Multi-Format Support**: Convert tabular data into multiple formats like JSON, CSV, XML, and Markdown for flexible LLM processing.
- **Accurate Information Retrieval**: Validate LLM responses against structured data to minimize errors and avoid misinformation.
- **Integration with RAG Systems**: Seamlessly integrate this tabular data ingestion approach with RAG frameworks to provide richer and more accurate insights.

## Prerequisites

- [asdf](https://asdf-vm.com/) for managing Python versions.
- [Poetry](https://python-poetry.org/) for dependency management.
- Python 3.8+.

## Installation

### 1. Install Python using `asdf`

Make sure `asdf` is installed by following the instructions at [asdf-vm.com](https://asdf-vm.com/guide/getting-started.html).

1. Add the Python plugin:

   ```bash
   asdf plugin-add python
   ```

2. Install the required Python version:

   ```bash
   asdf install python 3.13.0
   ```

3. Set the installed version as the local version for the project:

   ```bash
   asdf local python 3.13.0
   ```

4. Verify the Python version:

   ```bash
   python --version
   ```

### 2. Install `poetry` 
1. Install `poetry` using `asdf`
```bash
asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git

asdf install
```

OR

Install Poetry by following the instructions at [python-poetry.org](https://python-poetry.org/docs/#installation).

### 3. Install Dependencies using `poetry`

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/billionaires-rag-query.git
   cd billionaires-rag-query
   ```

3. Install the dependencies:

   ```bash
   poetry install
   ```

   This will create a virtual environment and install all required packages.

### 3. Activate the Poetry Environment

To activate the virtual environment managed by Poetry, run:

```bash
poetry shell
```

### 4. Run the Program

Once the Poetry environment is active, run the program using:

```bash
poetry run python main.py
```


## Usage

### 1. Prepare the Environment

Set up libraries for table extraction and tabular display:

```python
import pandas as pd
from beautifultable import BeautifulTable
import camelot
```

### 2. Extract Billionaires Data

Use Camelot to extract the billionaires list from a PDF file:

```python
df = get_tables("./World_Billionaires_Wikipedia.pdf", pages=[3])
```

### 3. Convert Data Formats

Convert the extracted tables into various formats like JSON, CSV, Markdown, and more:

```python
eval_df = prepare_data_formats(df)
```

### 4. Query with LLMs

Set up a connection to an OpenAI model and run queries using the tabular data as context:

```python
query = "Who is the richest person in 2023?"
result_df = run_question_test(query, eval_df)
```

### 5. Display Results

Display the LLM's response for each data format:

```python
table = BeautifulTableformat(query, result_df, 150)
print(table)
```

## Example Output

- **Query**: "What is Elon Musk's net worth?"
- **Output**: A table displaying responses for each data format, showing the model's ability to interpret and respond accurately based on the billionaires list.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License.