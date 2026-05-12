import pandas as pd

def print_columns(table):
    print(table.columns)


def print_info(table):
    print(table.info())

def print_describe(table):
    print(table.describe())

def print_analyze(table, not_printed):
    # Clean the exclude list (lowercase and strip spaces)
    cleaned_not_printed = [str(item).strip().lower() for item in not_printed]
    
    for col in table.columns:
        # Clean the column name for the check
        col_check = str(col).strip().lower()
        
        if col_check not in cleaned_not_printed:
            items = (table[col].dropna().astype(str).value_counts().sort_index())
            print(f"Column: {col}")
            print("─" * 40)
            for value, count in items.items():
                print(f'==>  "{value}" - {count} count')
            print("\n")