# 🚗 Analisis Data Penjualan Otomotif Multi-Cabang Indonesia (2025)

Proyek analisis data end-to-end dengan Python untuk menganalisis performa penjualan, perilaku konsumen, adopsi kendaraan listrik, dan program tukar tambah (trade-in) di 10 kota di Indonesia.

---

## 📂 Struktur Direktori Proyek

```text
analis/
│
├── PRD.md                       # Project Requirements Document (Spesifikasi Lengkap)
├── README.md                    # Dokumentasi Navigasi & Panduan Proyek
├── requirements.txt             # Daftar dependensi Python
├── skills.sh                    # Helper shortcut untuk manajemen skill (skills.sh)
│
├── data.csv                     # Raw data transaksi (10.000 baris)
├── data_cleaned.csv             # Data bersih hasil feature engineering
│
├── .agents/skills/              # Skill AI pendukung pembelajaran (skills.sh)
│   ├── data-analysis-jupyter/   # Panduan penulisan kode Pandas & visualisasi
│   └── exploratory-data-analysis/ # Panduan audit & EDA terstruktur
│
├── src/                         # Modul Python reusable
│   ├── __init__.py
│   ├── data_loader.py           # Pipeline pembersihan data & feature engineering
│   └── analysis_utils.py        # Utilitas visualisasi & kalkulasi metrik bisnis
│
├── notebooks/
│   └── 01_eda_and_insights.ipynb # Jupyter Notebook pembelajaran interaktif
│
└── outputs/
    ├── figures/                 # Ekspor grafik berkualitas tinggi (PNG)
    │   ├── 01_monthly_sales_trend.png
    │   ├── 02_branch_performance.png
    │   ├── 03_top_products_and_categories.png
    │   ├── 04_payment_and_tradein_distribution.png
    │   └── 05_cancellation_and_refund_rates.png
    └── summary_report.md        # Laporan eksekutif ringkas temuan bisnis
```

---

## 🚀 Cara Menjalankan Proyek

### 1. Instalasi Dependensi
Pastikan Python 3.10+ telah terpasang, lalu instal paket yang diperlukan:
```bash
pip install -r requirements.txt
```

### 2. Menjalankan Pipeline Pembersihan Data
Jalankan modul pembersih data untuk menghasilkan `data_cleaned.csv`:
```bash
python -m src.data_loader
```

### 3. Membuka Jupyter Notebook Interaktif
Buka notebook pembelajaran untuk melihat analisis langkah demi langkah:
```bash
jupyter notebook notebooks/01_eda_and_insights.ipynb
```

### 4. Menghasilkan Grafik & Laporan
Jalankan skrip generator visualisasi untuk memperbarui grafik di folder `outputs/figures/`:
```bash
python -m src.analysis_utils
```
