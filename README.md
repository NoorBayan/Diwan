# Diwan (ديوان): The Largest Classified Dataset of Arabic Poetry

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Diwan/main/images/DiwanLogo.png" width = "200px"/>
 </p>

Diwan is the largest classified dataset of Arabic poetry, consisting of nearly half a million poems and over 15 million individual verses. This comprehensive collection covers a wide range of poetic forms, meters, styles, and themes from the beginning of Arabic poetry to the present day. The dataset is structured into various categories to facilitate research in Arabic literature, prosody, and natural language processing.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Data Description](#data-description)
- [Methodology](#methodology)
- [Current Release Information](#current-release-information)
- [Explore Diwan on Google Colab](#explore-diwan-on-google-colab)
- [Future Updates](#future-updates)
- [How to Use the Dataset](#how-to-use-the-dataset)
- [License](#license)
- [Contributing](#contributing)

---

## Project Overview

Diwan (ديوان) aims to archive and classify Arabic poetry, serving as a valuable resource for researchers, linguists, and enthusiasts. With data collected from various sources, including web archives, poet websites, and historical books, Diwan offers a structured and searchable dataset that spans multiple eras, countries, and poetic forms.

This project was developed with the following goals:
1. To cover all poems from the beginning of Arabic poetry to the modern era.
2. To classify these poems into detailed categories based on poetic genre, style, language, meter, period, country, and other characteristics.

The dataset can be used for a variety of tasks, including meter identification, automatic poem generation, topic classification, plagiarism detection, and more.

---

## Data Description

The Diwan dataset is meticulously structured into multiple categories, offering an extensive view of Arabic poetry. The categorization makes it easier to explore the various dimensions of Arabic poetic tradition:

 <p align="center">
   <img src = "https://raw.githubusercontent.com/NoorBayan/Diwan/main/images/Poems_Analysis.png" width = "800px"/>
 </p>

### Key Categories:

- **Poetic Genre**: Includes both traditional and modern poetic arts.
- **Artistic Forms**: Covers eight traditional poetic forms and four modern ones.
- **Language**: Poems are classified as Classical (فصيح) or Colloquial (عامي) Arabic.
- **Style**: Encompasses traditional styles, free verse, prose poetry, and popular poetry.
- **Historical Period**: Poetry is categorized across eight distinct eras of Arabic history.
- **Country of the Poet**: Poets are classified by their country, spanning 120 different countries.
- **Primary Meter**: Based on the 16 classic meters of Arabic prosody.
- **Detailed Meter**: Includes four additional subcategories for more precise classification.
- **Verse Type**: Classified into monostich (single-line poems) or distich (two-line verses).
- **Poetic Themes**: Explores fourteen different poetic themes or purposes.
- **Poet Information**: Contains details about the poet, such as name and gender.
- **Poem Content**: The full text of each poem, including all individual verses.

Each category plays a critical role in making the Diwan dataset a comprehensive and valuable resource for Arabic poetry research.

---

## Methodology

The development of Diwan followed a structured three-phase approach:
 <p align="center">
   <img src = "https://raw.githubusercontent.com/NoorBayan/Diwan/main/images/DiwanMethodology.png" width = "800px"/>
 </p>
### 1. Data Collection

Our primary goal was to archive all Arabic poems from the earliest days to the present. To achieve this:
- We collected data from **three main sources**: online poetry repositories, poet websites, and historical books and articles.
- A total of 12 repositories, 56 poet blogs, and 203 websites were scanned and processed using custom web crawlers and extraction algorithms.
- An algorithm was developed to recognize and extract poetic text from various sources, ensuring minimal data loss.

### 2. Data Preprocessing

After collecting the data, we performed several preprocessing steps:
- **Merging and Cleaning**: The data, spread across 211 files, was merged and standardized. Missing values were labeled and structured into a table format.
- **Non-Arabic Content Filtering**: The dataset was filtered to remove any non-Arabic content, including foreign characters and unnecessary symbols like diacritics and elongation marks.
- **Data Transformation**: This step ensured the consistency and structure of the dataset. We normalized column values, standardized classifications, and eliminated duplicates. All data was coded to reduce size and ensure efficient processing.

### 3. Corpus Annotation

In the final phase, we annotated the dataset with detailed poetic labels. 
- We referred to seven authoritative sources on Arabic prosody and consulted two experts in Arabic poetry. 
- Custom algorithms were developed to automate this annotation process, ensuring a consistent and rich dataset for further use.

---

## Current Release Information

- **Total Poems**: Nearly **400,000** poems
- **Total Verses**: Over **14 million** verses

The dataset is categorized by poetic genre, meter, style, theme, and other features, making it suitable for a wide range of applications in research and development.

---

## Explore Diwan on Google Colab

To explore the full details of the Diwan dataset and interact with its extensive features, access our interactive Google Colab notebook. This notebook provides an easy-to-use interface for searching, analyzing, and learning more about the Diwan dataset.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/your-notebook-link)

---

## Future Updates

We are currently in the process of increasing the dataset to:
- **Total Poems**: Nearly **500,000** poems
- **Total Verses**: Over **15 million** individual verses

Additional classifications and refinements will be included in upcoming releases to further enhance the richness of the Diwan dataset.

---

## How to Use the Dataset

The Diwan dataset can be used for various research purposes:
- **Meter identification**: Detect the prosodic meter of Arabic poems.
- **Topic classification**: Automatically classify poems by theme or purpose.
- **Poem generation**: Train models to generate Arabic poetry.
- **Plagiarism detection**: Use the dataset to identify duplicate or plagiarized content.
- **Multi-label classification**: Explore how poems can belong to multiple categories simultaneously.

For detailed instructions on how to use the dataset, refer to the [Google Colab notebook](https://colab.research.google.com/your-notebook-link).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contributing

We welcome contributions from the community. Please feel free to open an issue or submit a pull request if you have any suggestions or improvements.

---
