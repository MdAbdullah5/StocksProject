
# 📄 PDF Report Extractor for Investor Relations Pages

This project is an **asynchronous PDF scraping and extraction tool** built with `aiohttp`, `BeautifulSoup`, and `pdfminer`. It scans company investor relations pages, detects links to **Annual Reports**, **Quarterly Reports**, and **Press Releases**, extracts text content from available PDF files, and saves the results to a structured Excel report.

---

## 🗂 Project Structure

- **`scraper.py`**  
  Contains all the core scraping logic:
  - `save_to_excel()` – Writes results to an Excel file.
  - `fetch()` – Asynchronously fetches content from a URL.
  - `get_pdf_links_from_page()` – Extracts PDF and press release links.
  - `download_and_extract_pdf()` – Extracts text from a given PDF URL.
  - `process_company()` – Orchestrates the scraping for each company.

- **`ReportsExtractor.py`**  
  Optional module that exposes the scraping functionality as an API using **FastAPI**.

---

## 🚀 How It Works

1. Loops through a list of company investor relations URLs.
2. Detects links related to:
   - Annual Reports (`*.pdf` containing "annual")
   - Quarterly Reports (`*.pdf` containing "quarterly")
   - Press Releases (either PDF or HTML)
3. Downloads and parses text content from PDFs using `pdfminer`.
4. Saves extracted content to an Excel file using `openpyxl`.

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install aiohttp beautifulsoup4 pdfminer.six openpyxl
```

---

## 🏁 Running the Script

Run the scraper from the command line:

```bash
python scraper.py
```

> Output will be saved to `company_reports.xlsx`.

---

## 🌐 FastAPI Integration (Optional)

You can expose the scraper as a web API using `ReportsExtractor.py`.

To run the FastAPI app:

```bash
uvicorn ReportsExtractor:app --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the API.

---

## 📤 Output Format

The Excel file contains the following columns:

- SNo
- Company URL
- Annual Report URL
- Quarterly Report URL
- Press Release URL
- Extracted Annual Report Text (truncated)
- Extracted Quarterly Report Text (truncated)
- Extracted Press Text (truncated)
- Start Time
- End Time
- Status

---

## 📌 Notes

- PDF parsing uses `pdfminer.six`, which works best with text-based PDFs.
- The tool is optimized for English/German report structures but can be customized.
- Text is truncated to 500 characters per field for Excel readability.

---



---

## 🚀 How to Run This Project

Follow these steps to get started:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2️⃣ Set Up Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
bash
pip install -r requirements.txt


4️⃣ Run the FastAPI Web App
python ReportsExtractor.py

## 👨‍💻 Author

Mohammed Abdullah Habeeb


