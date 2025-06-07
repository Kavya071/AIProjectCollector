# 🤖 AI Project Collector

AI Project Collector is a Python-based web scraping tool that uses Selenium and BeautifulSoup to collect AI-related project listings from Freelancer.com. It cleans, structures, and exports the data into an Excel file, making it easy for developers and researchers to explore trends in the freelance AI job market.

---

## 📁 Project Structure

* **s.py**: Main Python script that handles scraping, cleaning, and exporting data.
* **projects\_data\_cleaned.xlsx**: Output Excel file containing structured data of scraped AI projects.

---

## 🛠️ Technologies Used

* **Python**: Primary language for scripting.
* **Selenium**: Automates browser interaction for dynamic web scraping.
* **BeautifulSoup**: Parses and extracts data from HTML.
* **Pandas**: Organizes and exports data into Excel format.
* **openpyxl**: Engine used by Pandas to write Excel files.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Kavya071/AIProjectCollector.git
cd AIProjectCollector
```

### 2. Install Dependencies

```bash
pip install pandas selenium beautifulsoup4 openpyxl
```

### 3. Setup ChromeDriver

* Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) compatible with your Chrome version.
* Update the path in `s.py` here:

```python
service = Service('path/to/chromedriver')
```

### 4. Run the Script

```bash
python s.py
```

The script will scrape AI job listings from pages 1 to 40 on Freelancer.com and save the data to `projects_data_cleaned.xlsx`.

---

## 📊 Features

* Scrapes AI-related freelance projects across multiple pages.
* Extracts title, average bid, skills, bid count, and description.
* Cleans illegal/unprintable characters.
* Exports clean structured data to an Excel file.

---

## 📧 Contact

For queries or suggestions:

* **Email**: [bhardwajkavya099@gmail.com](mailto:bhardwajkavya099@gmail.com)

---

