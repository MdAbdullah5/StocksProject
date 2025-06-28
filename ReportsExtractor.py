from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import aiohttp, asyncio, csv, io
from scraper import process_company

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# CORS middleware (allow frontend JS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store scraped results
scraped_data = []

class URLRequest(BaseModel):
    url: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/scrape")
async def scrape_url(request: URLRequest):
    url = request.url.strip()
    if not url:
        return JSONResponse({"error": "Empty URL"}, status_code=400)

    async with aiohttp.ClientSession(headers={"User-Agent": "Mozilla/5.0"}) as session:
        result = await process_company(session, url)

    # Keep only the first 50 characters of extracted text
    result["annual_text"] = (result.get("annual_text") or "")[:50]
    result["quarterly_text"] = (result.get("quarterly_text") or "")[:50]
    result["press_text"] = (result.get("press_text") or "")[:50]

    scraped_data.append(result)
    return result

@app.get("/download")
def download_csv():
    output = io.StringIO()
    writer = csv.writer(output)

    headers = ["Company URL", "Annual PDF","Annual Text", "Quarterly PDF","Quarterly Text", "Press Release","Press Text", "Start", "End", "Status"]
    writer.writerow(headers)

    for row in scraped_data:
        writer.writerow([
            row.get("company_url", ""),
            row.get("annual_pdf", ""),
            row.get("annual_text",""),
            row.get("quarterly_pdf", ""),
            row.get("quarterly_text", ""),
            row.get("press_release_url", ""),
            row.get("press_text",""),
            row.get("start_time", ""),
            row.get("end_time", ""),
            row.get("status", "")
        ])

    output.seek(0)
    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=scraped_data.csv"}
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("ReportsExtractor:app", host="127.0.0.1", port=8000, reload=True)