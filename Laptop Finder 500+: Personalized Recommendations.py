import pandas as pd
import webbrowser

FILE = "laptops.csv"

# Load database
try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    print("❌ laptops.csv not found!")
    exit()

# Clean column names
df.columns = df.columns.str.strip()

# Convert numbers
for column in ["Price", "RAM", "SSD"]:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(subset=["Price", "RAM", "SSD"], how="any")


# -------------------------------
# USER INPUT
# -------------------------------

print("=" * 60)
print("        💻 LAPTOP FINDER 500+")
print("   Smart Laptop Recommendation System")
print("=" * 60)

print("\nTotal laptops:", len(df))

budget = float(input("\n💰 Maximum budget ₹: "))

print("\nPurpose:")
print("1. Gaming")
print("2. Coding")
print("3. Student")

purpose_choice = input("Choose: ")

purpose = {
    "1": "Gaming",
    "2": "Coding",
    "3": "Student"
}.get(purpose_choice, "Student")


print("\nMinimum RAM:")
print("1. 8 GB")
print("2. 16 GB")
print("3. 32 GB")
print("4. 64 GB")

ram_choice = input("Choose: ")

ram_values = {
    "1": 8,
    "2": 16,
    "3": 32,
    "4": 64
}

required_ram = ram_values.get(ram_choice, 8)


print("\nMinimum SSD:")
print("1. 512 GB")
print("2. 1 TB")
print("3. 2 TB")

ssd_choice = input("Choose: ")

ssd_values = {
    "1": 512,
    "2": 1024,
    "3": 2048
}

required_ssd = ssd_values.get(ssd_choice, 512)


print("\nProcessor:")
print("1. Intel")
print("2. Ryzen")
print("3. Any")

processor_choice = input("Choose: ")

if processor_choice == "1":
    processor_filter = "intel"
elif processor_choice == "2":
    processor_filter = "ryzen"
else:
    processor_filter = "any"


print("\nGPU:")
print("1. Integrated")
print("2. RTX")
print("3. Any")

gpu_choice = input("Choose: ")

if gpu_choice == "1":
    gpu_filter = "integrated"
elif gpu_choice == "2":
    gpu_filter = "rtx"
else:
    gpu_filter = "any"


# -------------------------------
# FILTER LAPTOPS
# -------------------------------

results = df[
    (df["Price"] <= budget) &
    (df["RAM"] >= required_ram) &
    (df["SSD"] >= required_ssd)
].copy()

# Processor filter
if processor_filter != "any" and "Processor" in df.columns:
    results = results[
        results["Processor"].astype(str).str.lower().str.contains(processor_filter)
    ]

# GPU filter
if "GPU" in df.columns:
    if gpu_filter == "rtx":
        results = results[results["GPU"].astype(str).str.lower().str.contains("rtx")]
    elif gpu_filter == "integrated":
        results = results[results["GPU"].astype(str).str.lower().str.contains("integrated")]


# -------------------------------
# RECOMMENDATION SCORE
# -------------------------------

def score_laptop(row):
    score = 0

    # RAM
    if row["RAM"] >= required_ram:
        score += 20

    # SSD
    if row["SSD"] >= required_ssd:
        score += 20

    # Purpose
    if "Category" in row and str(row["Category"]).lower() == purpose.lower():
        score += 25

    # GPU
    gpu = str(row.get("GPU", "")).lower()
    if purpose == "Gaming":
        if "rtx" in gpu:
            score += 30
        elif "gtx" in gpu:
            score += 20
        else:
            score += 5

    # CPU
    cpu = str(row.get("Processor", "")).lower()
    if "ryzen 7" in cpu or "core i7" in cpu:
        score += 10
    elif "ryzen 5" in cpu or "core i5" in cpu:
        score += 8
    elif "ryzen 3" in cpu or "core i3" in cpu:
        score += 5

    return score


# -------------------------------
# SHOW RESULTS
# -------------------------------

if results.empty:
    print("\n❌ No laptop found!")
    print("👉 Suggestion: Try increasing your budget or lowering requirements.")
    # Fallback: show closest laptops above budget
    fallback = df[
        (df["RAM"] >= required_ram) &
        (df["SSD"] >= required_ssd)
    ].sort_values(by="Price").head(5)
    if not fallback.empty:
        print("\n💡 Closest matches (slightly above budget):")
        for _, laptop in fallback.iterrows():
            print(f"- {laptop['Brand']} {laptop['Model']} (₹{laptop['Price']})")

else:
    results["Score"] = results.apply(score_laptop, axis=1)
    results = results.sort_values(by=["Score", "Price"], ascending=[False, True])

    print("\n\n🏆 TOP 10 LAPTOPS")
    print("=" * 100)

    for _, laptop in results.head(10).iterrows():
        print("\n💻", laptop.get("Brand", ""), laptop.get("Model", ""))
        print("💰 Price      : ₹", laptop["Price"])
        print("🧠 Processor  :", laptop.get("Processor", "N/A"))
        print("⚡ RAM        :", laptop["RAM"], "GB")
        print("💾 SSD        :", laptop["SSD"], "GB")
        print("🎮 GPU        :", laptop.get("GPU", "N/A"))
        print("🎯 Category   :", laptop.get("Category", "N/A"))
        print("⭐ Score      :", laptop["Score"])
        if "Link" in laptop and pd.notna(laptop["Link"]):
            print("🔗 Product    :", laptop["Link"])
        print("-" * 100)

    # -------------------------------
    # BEST LAPTOP
    # -------------------------------
    best = results.iloc[0]
    print("\n🥇 BEST LAPTOP FOR YOU")
    print("=" * 60)
    print("Brand      :", best.get("Brand", ""))
    print("Model      :", best.get("Model", ""))
    print("Price      : ₹", best["Price"])
    print("Processor  :", best.get("Processor", "N/A"))
    print("RAM        :", best["RAM"], "GB")
    print("SSD        :", best["SSD"], "GB")
    print("GPU        :", best.get("GPU", "N/A"))
    print("Score      :", best["Score"])

    if "Link" in best and pd.notna(best["Link"]):
        print("\n🔗 DIRECT PRODUCT LINK:")
        print(best["Link"])
        open_link = input("\nOpen the best laptop product page? (yes/no): ")
        if open_link.lower() == "yes":
            webbrowser.open(best["Link"])

    print("\n✅ Search completed!")
