# Wikipedia Article Revisions Analysis

## Overview

This project consists of two main scripts:
1. **wikidata.py**: Fetches articles from the "Artificial Intelligence" category on Wikipedia, retrieves details for each article, and saves the information to a CSV file.
2. **visualize.ipynb**: Analyzes and visualizes the revision history of the articles using charts.

## Installation

To run this project, you need to have Python installed along with the necessary libraries. You can install the required libraries using pip:

```bash
pip install requests pandas matplotlib wordcloud
```

## Usage

1. **Fetching Article Data**

   Run `wikidata.py` to fetch articles from the "Artificial Intelligence" category and save the details to `articles.csv`. This file will include the title, URL, extract, and revision timestamps of each article.

   ```bash
   python wikidata.py
   ```

2. **Visualizing Revisions**

   Open and run `visualize.ipynb` in Jupyter Notebook or JupyterLab. This script will read the `articles.csv` file, process the revision timestamps, and generate the following charts:
   
   - **Number of Wikipedia Artificial Intelligence Article Revisions Over Time**: A time series plot showing the number of revisions per day.
   - **Distribution of Wikipedia Artificial Intelligence Article Revisions Over Time**: A histogram showing the distribution of revisions over time.

   To open `visualize.ipynb`, navigate to the directory containing the file and run:

   ```bash
   jupyter notebook visualize.ipynb
   ```

## Charts

### 1. Number of Wikipedia Artificial Intelligence Article Revisions Over Time

This line plot shows the number of revisions made to Wikipedia articles in the "Artificial Intelligence" category over time. It provides insights into how active the editing has been for this category.
![image](https://github.com/user-attachments/assets/2683e35c-9c9b-4917-b692-224322e201fc)


### 2. Distribution of Wikipedia Artificial Intelligence Article Revisions Over Time

This histogram illustrates the distribution of revision timestamps. It helps in understanding the frequency of revisions and any noticeable patterns in the activity levels.
![image](https://github.com/user-attachments/assets/74fd336c-4f3b-47e2-8e51-47a19511d32b)


## License

This project is licensed under the MIT License.

## Acknowledgements

- Wikipedia API for providing article data.
- Python libraries `requests`, `pandas`, `matplotlib`, and `wordcloud` for data processing and visualization.

