"""
AI Personal Expense Categorizer
Simple keyword-based + rule based categorizer.
Can be upgraded to ML later.
"""

from collections import defaultdict
import re


CATEGORIES = {
    "Food": ["swiggy", "zomato", "restaurant", "cafe", "food", "lunch", "dinner", "breakfast", "pizza", "burger", "chai", "coffee", "mcdonald", "kfc", "dominos", "biryani"],
    "Travel": ["uber", "ola", "rapido", "metro", "bus", "train", "flight", "petrol", "fuel", "taxi", "cab", "irctc", "indigo", "spicejet"],
    "Shopping": ["amazon", "flipkart", "myntra", "ajio", "meesho", "shopping", "clothes", "shoes", "mall", "store"],
    "Bills": ["electricity", "water", "gas", "internet", "wifi", "mobile", "recharge", "bill", "rent", "emi", "loan"],
    "Entertainment": ["netflix", "prime", "hotstar", "spotify", "movie", "cinema", "pvr", "inox", "game", "steam"],
    "Health": ["pharmacy", "medicine", "hospital", "doctor", "clinic", "apollo", "medplus", "gym", "fitness"],
    "Education": ["course", "udemy", "coursera", "book", "tuition", "college", "school", "exam"],
    "Other": []
}


def categorize(text: str) -> str:
    text = text.lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in text:
                return cat
    return "Other"


def extract_amount(text: str):
    """Try to find amount like 250 or Rs.250 or ₹250"""
    match = re.search(r'(?:rs\.?|₹|inr)?\s*(\d+(?:\.\d{1,2})?)', text.lower())
    if match:
        return float(match.group(1))
    return 0.0


def main():
    print("=" * 55)
    print("   AI Personal Expense Categorizer")
    print("=" * 55)
    print("Paste expense lines (example: 'Swiggy order 320' or 'Uber to office 180')")
    print("Type 'summary' to see totals, 'quit' to exit")
    print()

    expenses = []  # list of (text, category, amount)

    while True:
        line = input("> ").strip()
        if not line:
            continue
        if line.lower() in ['quit', 'exit', 'q']:
            break
        if line.lower() == 'summary':
            print("\n--- SUMMARY ---")
            totals = defaultdict(float)
            for _, cat, amt in expenses:
                totals[cat] += amt
            for cat, total in sorted(totals.items(), key=lambda x: -x[1]):
                print(f"{cat:15} : ₹{total:.2f}")
            print(f"{'TOTAL':15} : ₹{sum(totals.values()):.2f}")
            print("---------------\n")
            continue

        cat = categorize(line)
        amount = extract_amount(line)
        expenses.append((line, cat, amount))
        print(f"  → Category: {cat} | Amount: ₹{amount:.2f}")


if __name__ == "__main__":
    main()
