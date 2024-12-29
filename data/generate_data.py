import csv
import json
import random
from datetime import datetime, timedelta
from textblob import TextBlob

# Helper function to generate mock data
def generate_random_data():
    products = [101, 102, 103, 104, 105]
    customers = [1001, 1002, 1003, 1004, 1005]
    ratings = [1, 2, 3, 4, 5]
    review_texts = [
        "Excellent quality, exceeded my expectations!",
        "Good product, but could be improved.",
        "Terrible, do not buy this product.",
        "Okay, but not as good as expected.",
        "I love it! Highly recommend.",
        "Not worth the price, poor quality."
    ]
    
    return {
        'product_id': random.choice(products),
        'customer_id': random.choice(customers),
        'rating': random.choice(ratings),
        'review_date': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),
        'review_text': random.choice(review_texts)
    }

# 1. Generate CSV file (Source A)
def generate_csv():
    with open('source_a_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['review_id', 'product_id', 'customer_id', 'rating', 'review_date', 'review_text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for review_id in range(1, 1001):
            data = generate_random_data()
            writer.writerow({
                'review_id': review_id,
                'product_id': data['product_id'],
                'customer_id': data['customer_id'],
                'rating': data['rating'],
                'review_date': data['review_date'],
                'review_text': data['review_text']
            })
    print("CSV file generated: source_a_data.csv")

# 2. Generate JSON file (Source B)
def generate_json():
    reviews = []
    for review_id in range(1, 501):
        data = generate_random_data()
        reviews.append({
            'review_id': review_id,
            'product_id': data['product_id'],
            'customer_id': data['customer_id'],
            'rating': data['rating'],
            'review_date': data['review_date'],
            'review_text': data['review_text']
        })
    
    with open('source_b_data.json', 'w') as jsonfile:
        json.dump(reviews, jsonfile, indent=4)
    print("JSON file generated: source_b_data.json")

# 3. Generate raw text file (Source C)
def generate_raw_text_file():
    with open('source_c_data.txt', 'w') as file:
        for review_id in range(1, 701):
            data = generate_random_data()
            file.write(f"{data['rating']}|{data['product_id']}|{data['customer_id']}|{data['rating']}|{data['review_date']}|{data['review_text']}\n")
    print("Text file generated: source_c_data.txt")

# Generate all data files
def generate_all_data():
    generate_csv()
    generate_json()
    generate_raw_text_file()

# Main execution
if __name__ == "__main__":
    generate_all_data()
