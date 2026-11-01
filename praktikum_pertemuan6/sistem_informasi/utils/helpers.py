# File: sistem_informasi/utils/helpers.py
# Berisi fungsi-fungsi pembantu (utilitas)

def cetak_garis():
    """Mencetak garis pemisah."""
    print("-" * 40)

def format_output(data_dict):
    """Mencetak dictionary dengan rapi."""
    for kunci, nilai in data_dict.items():
        print(f"  {kunci.upper()}: {nilai}")