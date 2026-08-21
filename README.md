# 💻 Laptop Finder 500+ — Smart Recommendation System

A Python-based tool that helps users find the **best laptops** according to their budget, purpose, and hardware requirements.  
It uses **Pandas** to process a dataset of laptops and applies filters plus a custom **scoring algorithm** to recommend the top options.

---

## ✨ Features
- 📊 Reads laptop data from `laptops.csv`  
- 🧹 Cleans and converts numeric fields (Price, RAM, SSD)  
- 🎯 Filters laptops based on:
  - Budget (₹)  
  - Purpose (Gaming, Coding, Student)  
  - Minimum RAM (8–64 GB)  
  - Minimum SSD (512 GB–2 TB)  
  - Processor type (Intel, Ryzen, Any)  
  - GPU type (Integrated, RTX, Any)  
- ⭐ Scores laptops using weighted criteria:
  - RAM & SSD capacity  
  - Purpose match  
  - GPU suitability (RTX/GTX for gaming)  
  - CPU tier (Ryzen 7/i7, Ryzen 5/i5, etc.)  
- 🏆 Displays the **Top 10 laptops** sorted by score and price  
- 🥇 Highlights the **Best Laptop** with direct product link  
- 💡 Suggests fallback laptops if no exact matches are found  

---

## 📂 Installation
Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/your-username/laptop-finder.git
cd laptop-finder

Install dependencies:
pip install pandas

Install dependencies:

🚀 Usage
Run the script in any Python environment:
python laptop_finder.py


example output
🏆 TOP 10 LAPTOPS
====================================================================================================

💻 ASUS ROG Strix G15
💰 Price      : ₹ 59,999
🧠 Processor  : Ryzen 7
⚡ RAM        : 16 GB
💾 SSD        : 512 GB
🎮 GPU        : RTX 3060
🎯 Category   : Gaming
⭐ Score      : 105
🔗 Product    : https://example.com/asus-rog-strix
----------------------------------------------------------------------------------------------------

🥇 BEST LAPTOP FOR YOU
============================================================
Brand      : ASUS
Model      : ROG Strix G15
Price      : ₹ 59,999
Processor  : Ryzen 7
RAM        : 16 GB
SSD        : 512 GB
GPU        : RTX 3060
Score      : 105

🔗 DIRECT PRODUCT LINK:
https://example.com/asus-rog-strix


📌 Future Improvements
Add more categories (e.g., Business, Content Creation).

Improve scoring weights for different purposes.

Export results to CSV or JSON.

Build a GUI version with Tkinter or PyQt.

📜 License
This project is licensed under the MIT License.


---

👉 Replace `your-username` in the `git clone` link with your actual GitHub username.  
