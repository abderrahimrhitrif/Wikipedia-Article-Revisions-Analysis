# Wikipedia Article Revisions Analysis

## Overview
A data engineering and analytics project that queries the MediaWiki API to fetch Wikipedia articles and revision history, storing them for temporal distribution analysis and word cloud text visualization.

## Architecture & Pipeline
1. **API Ingestion (`wikidata.py`)**: Queries the MediaWiki API (`api.php`) for category members and fetches article text, extracts, and revision timestamps (`rvlimit: max`).
2. **Data Persistence**: Exports collected article data and revisions to CSV (`articles.csv`).
3. **Visual Analytics (`visualize.ipynb`)**: Parses revision timestamps, generates word clouds from article extracts, and plots temporal revision trends.

## Data
- **Source**: MediaWiki API (`en.wikipedia.org/w/api.php`) extracting artificial intelligence article categories and revision timestamps.

## Method & Algorithms
- **API Scraping & Pagination**: Handles MediaWiki continuation parameters (`cmcontinue`) to paginate through category members and revision histories.
- **Time-Series EDA**: Parses ISO timestamps into datetime objects and aggregates revisions by date.

## Verified Results & Metrics
- Successfully queried Wikipedia category members, extracted article text extracts and revision histories, and generated word clouds and temporal distribution plots.

## Limitations & Caveats
- Relies on live MediaWiki API availability and category membership stability.

## Run Instructions
```bash
python wikidata.py
jupyter notebook visualize.ipynb
```

## CV Bullet Points
- Built a data collection and analysis pipeline querying the MediaWiki API for article extracts and revision history timestamps.
- Processed temporal time-series data to visualize Wikipedia revision frequency distributions and generated text word clouds using Python.

## Claims to Avoid
- Do not claim large-scale web scraping infrastructure beyond standard API client scripts.
