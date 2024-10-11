import csv
from typing import Dict, List


def load_sales_data(filename: str) -> List[Dict[str, str]]:
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def calculate_total_sales(sales_data: List[Dict[str, str]]) -> Dict[str, float]:
    total_sales = {}
    for row in sales_data:
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])
        total_sales[product] = total_sales.get(product, 0) + quantity * price
    return total_sales


def calculate_total_quantity(sales_data: List[Dict[str, str]]) -> Dict[str, int]:
    total_quantity = {}
    for row in sales_data:
        product = row["product"]
        quantity = int(row["quantity"])
        total_quantity[product] = total_quantity.get(product, 0) + quantity
    return total_quantity


def calculate_average_price(sales_data: List[Dict[str, str]]) -> Dict[str, float]:
    total_price = {}
    total_count = {}
    for row in sales_data:
        product = row["product"]
        price = float(row["price"])
        total_price[product] = total_price.get(product, 0) + price
        total_count[product] = total_count.get(product, 0) + 1
    return {
        product: total_price[product] / total_count[product] for product in total_price
    }


# Oppgave
"""
Legg til funksjonalitet som kalkulerer produkt med høyest total salgsverdi. 
Det vil si, om laptop har solgt for totalt 20,000 kroner og det er det høyeste totalt, 
så skal koden regne ut og printe ut dette
"""
# Løsningsforslag

def calculate_highest_sales_product(total_sales: Dict[str, float]) -> Dict[str, float]:
    highest_product = max(total_sales, key=total_sales.get)
    highest_value = total_sales[highest_product]
    return {highest_product: highest_value}


def display_results(results: Dict[str, float], title: str) -> None:
    print(f"\n{title}")
    for product, value in results.items():'
        print(f"{product}: {value:.2f}")


filename = "sales.csv"
sales_data = load_sales_data(filename)

total_sales = calculate_total_sales(sales_data)
display_results(total_sales, "Total Sales per Product")

total_quantity = calculate_total_quantity(sales_data)
display_results(total_quantity, "Total Quantity Sold per Product")

average_price = calculate_average_price(sales_data)
display_results(average_price, "Average Price per Product")

highest_sales_product = calculate_highest_sales_product(total_sales)
display_results(highest_sales_product, "Product with Highest Total Sales Value")
