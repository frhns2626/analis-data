"""
Modul Data Loader & Preprocessing untuk Analisis Penjualan Otomotif.
Menangani pembacaan data mentah, validasi tipe data, penanganan anomali,
dan rekayasa fitur (feature engineering).
"""

from pathlib import Path
import pandas as pd
import numpy as np


def extract_brand(product_name: str) -> str:
    """Mengekstrak nama brand/pabrikan dari nama produk kendaraan."""
    if not isinstance(product_name, str):
        return "Unknown"
    return product_name.split()[0]


def load_raw_data(file_path: str = "data.csv") -> pd.DataFrame:
    """Membaca file raw CSV dan memverifikasi keberadaannya."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File data tidak ditemukan pada path: {path.resolve()}")
    df = pd.read_csv(path)
    print(f"[INFO] Raw data berhasil dimuat: {df.shape[0]:,} baris, {df.shape[1]} kolom.")
    return df


def clean_and_transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Melakukan pembersihan data dan rekayasa fitur:
    - Konversi tanggal ke datetime
    - Ekstraksi fitur waktu (month, quarter, day_name)
    - Ekstraksi brand kendaraan
    - Kategorisasi tipe pembayaran dan status trade-in
    - Penanganan anomali net sales negatif
    """
    cleaned_df = df.copy()

    # 1. Konversi format tanggal
    cleaned_df["sales_date"] = pd.to_datetime(cleaned_df["sales_date"], errors="coerce")

    # 2. Rekayasa Fitur Waktu (Temporal Features)
    cleaned_df["year"] = cleaned_df["sales_date"].dt.year
    cleaned_df["month"] = cleaned_df["sales_date"].dt.month
    cleaned_df["month_name"] = cleaned_df["sales_date"].dt.strftime("%b")
    cleaned_df["quarter"] = "Q" + cleaned_df["sales_date"].dt.quarter.astype(str)
    cleaned_df["day_name"] = cleaned_df["sales_date"].dt.day_name()

    # 3. Rekayasa Fitur Produk
    cleaned_df["brand"] = cleaned_df["product_name"].apply(extract_brand)

    # 4. Rekayasa Fitur Finansial & Pembayaran
    cleaned_df["is_credit"] = cleaned_df["payment_type"].str.contains("Kredit", case=False, na=False)
    cleaned_df["is_trade_in"] = cleaned_df["payment_type"].str.contains("Trade In", case=False, na=False)
    
    # Rasio nilai tukar tambah terhadap harga kotor (total)
    cleaned_df["trade_in_ratio"] = np.where(
        cleaned_df["total"] > 0,
        (cleaned_df["trade_in"] / cleaned_df["total"]).round(4),
        0.0
    )

    # Menandai anomali trade-in melebihi total tagihan (cashback / saldo minus)
    cleaned_df["has_negative_net_sales"] = cleaned_df["total_sales"] < 0

    # 5. Konversi tipe data kategorikal untuk efisiensi memori
    categorical_cols = ["branch", "category", "brand", "payment_type", "status", "quarter"]
    for col in categorical_cols:
        if col in cleaned_df.columns:
            cleaned_df[col] = cleaned_df[col].astype("category")

    return cleaned_df


def save_cleaned_data(df: pd.DataFrame, output_path: str = "data_cleaned.csv") -> None:
    """Menyimpan data hasil pembersihan ke CSV."""
    df.to_csv(output_path, index=False)
    print(f"[INFO] Data bersih berhasil disimpan ke '{output_path}'.")


def run_pipeline(input_path: str = "data.csv", output_path: str = "data_cleaned.csv") -> pd.DataFrame:
    """Menjalankan seluruh pipeline pembersihan dan transformasi."""
    raw_df = load_raw_data(input_path)
    clean_df = clean_and_transform_data(raw_df)
    
    print("\n--- Ringkasan Validasi Pipeline ---")
    print(f"Total Transaksi: {len(clean_df):,}")
    print(f"Rentang Waktu  : {clean_df['sales_date'].min().date()} s/d {clean_df['sales_date'].max().date()}")
    print(f"Jumlah Cabang  : {clean_df['branch'].nunique()} cabang")
    print(f"Jumlah Model   : {clean_df['product_name'].nunique()} model ({clean_df['brand'].nunique()} merek)")
    print(f"Status Counts  :\n{clean_df['status'].value_counts().to_string()}")
    print(f"Transaksi Net Sales Negatif (Trade-In > Total): {clean_df['has_negative_net_sales'].sum():,} transaksi")

    save_cleaned_data(clean_df, output_path)
    return clean_df


if __name__ == "__main__":
    run_pipeline()
