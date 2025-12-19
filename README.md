## Web scraping app for finding supermarket discounts

## 📦 Setup
1. Clone the repository
```
https://github.com/YoanaAneva/Find-Promos.git
```
2. Create a virtual environment
* Windows
```
python -m venv venv
venv\Scripts\activate
```
* macOS / Linux
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. From the project root run
```
python -m streamlit run app.py
```
## 🛠 Tech Stack
* Python 3.10
* BeautifulSoup & Requests
* Selenium (for JS-heavy sites)
* Streamlit (UI)