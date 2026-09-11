# 🚗 Analisis Data Penjualan Otomotif Multi-Cabang Indonesia (2025)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib & Seaborn](https://img.shields.io/badge/Visualization-Matplotlib%20%26%20Seaborn-orange.svg)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

Repositori ini memuat proyek **analisis data komprehensif (*end-to-end*)** pada transaksi jaringan dealer otomotif resmi di **10 kota besar di Indonesia** sepanjang tahun operasional 2025. Proyek ini mencakup eksplorasi kinerja finansial, tren musiman, adopsi kendaraan listrik (*Electric Vehicle* / EV), efektivitas program tukar tambah (*trade-in*), serta mitigasi risiko retur (*cancellation & refund*).

Tersedia dalam bentuk **modul Python modular**, **Jupyter Notebook interaktif 10 bab**, serta **lembar kerja praktis Google Colab** beserta solusinya.

---

## 📌 Ringkasan Eksekutif & Metrik Kunci (2025 KPIs)

Berdasarkan analisis terhadap **10.000 transaksi** penjualan:

| Metrik Bisnis | Capaian 2025 | Catatan & Konteks Analisis |
|:---|:---:|:---|
| **Total Transaksi Masuk** | `10.000` | Seluruh catatan faktur masuk dari 10 cabang |
| **Tingkat Penyelesaian (*Completed*)** | `89,7%` (8.966 transaksi) | Transaksi sah yang berhasil serah terima unit |
| **Total Omzet Kotor (*Gross Revenue*)** | **Rp 3,29 Triliun** | Akumulasi nilai penjualan sebelum potongan tukar tambah |
| **Total Kas Bersih Masuk (*Net Revenue*)** | **Rp 2,77 Triliun** | Penerimaan kas bersih setelah pengurangan nilai *trade-in* |
| **Total Unit Terjual** | `9.342` Unit | Kombinasi kendaraan ICE konvensional dan EV |
| **Rata-Rata Nilai Transaksi (AOV)** | `Rp 366,6 Juta` | Nilai rata-rata kotor per transaksi *completed* |
| **Penetrasi Pembiayaan Kredit** | `62,5%` | Mayoritas konsumen mengandalkan lembaga pembiayaan |
| **Penetrasi Tukar Tambah (*Trade-In*)** | `35,3%` | Pendorong penting peningkatan volume penjualan |
| **Tingkat Pembatalan (*Cancellation Rate*)** | `5,42%` | 542 pesanan dibatalkan sebelum pengiriman unit |
| **Tingkat Retur (*Refund Rate*)** | `4,92%` | 492 transaksi dikembalikan pasca-administrasi |

---

## 💡 Temuan Utama (Key Analytical Insights)

1. **Dominasi Pasar Regional**:
   - **Jakarta** memimpin kontribusi pendapatan terbesar di antara 10 cabang operasional, disusul oleh kota-kota metropolitan sekunder (Surabaya, Bandung, Medan).
2. **Preferensi Konsumen & Tren EV**:
   - Model paling laris adalah **Honda HR-V 1.5 E CVT**, mempertegas dominasi segmen Compact SUV dan MPV keluarga di pasar Indonesia.
   - Segmen Kendaraan Listrik (*City Car EV*, contoh: **Wuling Air ev**) menunjukkan pertumbuhan volume yang stabil, membuktikan kesiapan pasar perkotaan dalam menyerap mobilitas ramah lingkungan.
3. **Pola Pembiayaan & Ketergantungan Leasing**:
   - Sebanyak **62,5%** transaksi dilakukan melalui skema kredit, menegaskan bahwa kemitraan strategis dengan perusahaan *leasing* (*multifinance*) adalah kunci kelancaran konversi penjualan.
4. **Anomali Finansial Program Trade-In**:
   - Terdeteksi **251 transaksi** dengan *Net Sales* bertanda negatif (`trade_in > total`), di mana taksiran harga mobil lama konsumen melebihi harga mobil baru yang dibeli sehingga memicu skema *cashback* / pengembalian kas kepada konsumen.
5. **Kualitas Operasional Cabang**:
   - Rata-rata tingkat pembatalan (5,42%) dan retur (4,92%) tersebar bervariasi antar cabang; cabang dengan waktu tunggu unit (*indent*) lebih lama cenderung memiliki rasio pembatalan lebih tinggi.

---

## 📊 Visualisasi Analisis Kunci

Seluruh grafik visualisasi diproduksi dengan resolusi tinggi (300 DPI) dan tersimpan di folder [`outputs/figures/`](outputs/figures/):

| No | Visualisasi | Deskripsi & Insight Bisnis |
|:---:|:---|:---|
| **01** | [**Tren Penjualan Bulanan**](outputs/figures/01_monthly_sales_trend.png) | Pola dinamika omzet kotor, kas bersih, dan volume unit sepanjang Januari – Desember 2025. |
| **02** | [**Performa 10 Cabang**](outputs/figures/02_branch_performance.png) | Perbandingan omzet kotor vs kas bersih serta total unit terjual di tiap cabang dealer. |
| **03** | [**Top Produk & Kategori**](outputs/figures/03_top_products_and_categories.png) | Ranking 10 model mobil terlaris dan kontribusi pendapatan per kategori kendaraan (MPV, SUV, EV, dsb.). |
| **04** | [**Distribusi Pembayaran & Trade-In**](outputs/figures/04_payment_and_tradein_distribution.png) | Proporsi transaksi Tunai vs Kredit, penetrasi Trade-In, dan rasio nilai tukar tambah terhadap harga beli. |
| **05** | [**Tingkat Pembatalan & Refund**](outputs/figures/05_cancellation_and_refund_rates.png) | Evaluasi rasio risiko operasional per cabang untuk mitigasi layanan dan stok. |

---

## 📂 Struktur Direktori Proyek

```text
analis/
│
├── PRD.md                             # Project Requirements Document (Spesifikasi Lengkap & Hipotesis)
├── README.md                          # Dokumentasi Utama & Panduan Proyek (File ini)
├── requirements.txt                   # Spesifikasi dependensi pustaka Python
├── skills.sh                          # Helper tool manajemen skill analitik (skills.sh)
├── skills-lock.json                   # Lock file versi skill
│
├── data.csv                           # Dataset mentah (10.000 transaksi x 16 atribut)
├── data_cleaned.csv                   # Dataset bersih hasil pembersihan & rekayasa fitur
│
├── src/                               # Modul Python produksi (reusable & modular)
│   ├── __init__.py                    # Package init
│   ├── data_loader.py                 # Pipeline otomatisasi pembersihan & feature engineering
│   └── analysis_utils.py              # Perhitungan KPI, visualisasi berstandar publikasi & report generator
│
├── notebooks/                         # Lingkungan eksplorasi interaktif
│   └── 01_eda_and_insights.ipynb      # Notebook komprehensif 10 bab analisis end-to-end
│
├── colab_notebook.ipynb               # Lembar kerja tugas studi kasus Google Colab (5 Soal + Solusi)
├── colab_questions.md                 # Dokumentasi soal tugas asli Colab
├── build_notebook.py                  # Skrip penyusun otomatis notebook komprehensif
├── solve_colab.py                     # Skrip injeksi solusi interaktif ke notebook Colab
├── extract_colab.py                   # Skrip utilitas ekstraksi sel Colab
│
├── outputs/                           # Artefak hasil analisis
│   ├── figures/                       # Grafik visualisasi data beresolusi tinggi (PNG)
│   │   ├── 01_monthly_sales_trend.png
│   │   ├── 02_branch_performance.png
│   │   ├── 03_top_products_and_categories.png
│   │   ├── 04_payment_and_tradein_distribution.png
│   │   └── 05_cancellation_and_refund_rates.png
│   └── summary_report.md              # Laporan ringkasan eksekutif dan rekomendasi bisnis
│
└── .agents/skills/                    # Skill agen AI pendukung analitika data
    ├── data-analysis-jupyter/         # Panduan best-practice visualisasi & pandas
    └── exploratory-data-analysis/     # Kerangka kerja audit data terstandar
```

---

## 🛠️ Kamus Data & Rekayasa Fitur (*Feature Engineering*)

### 1. Data Mentah (`data.csv`)
Dataset terdiri dari **10.000 baris × 16 kolom**, mencatat detail pesanan:
- **Atribut Transaksi**: `order_id`, `sales_date`, `status` (`completed`, `cancelled`, `refund`).
- **Atribut Pelanggan & Wilayah**: `customer_name`, `branch`, `branch_address`.
- **Atribut Produk**: `product_name`, `category`, `color`, `price`, `quantity`.
- **Atribut Keuangan**: `payment_type`, `trade_in`, `discount`, `total`, `total_sales`.

### 2. Fitur Tambahan (`data_cleaned.csv`)
Pipeline pada [`src/data_loader.py`](src/data_loader.py) menambahkan fitur-fitur analitik berikut:
- `sales_date`: Dikonversi ke tipe data `datetime64[ns]`.
- `year`, `month`, `month_name`, `quarter`, `day_name`: Fitur dekomposisi waktu untuk analisis musiman.
- `brand`: Merek pabrikan yang diekstraksi dari nama produk (Toyota, Honda, Daihatsu, Wuling, Suzuki, dll.).
- `is_credit`: Penanda boolean transaksi yang menggunakan skema pembiayaan kredit.
- `is_trade_in`: Penanda boolean keikutsertaan program tukar tambah.
- `trade_in_ratio`: Rasio nilai tukar tambah terhadap harga total pembelian (`trade_in / total`).
- `has_negative_net_sales`: Penanda transaksi dengan nilai kas masuk negatif (*cashback* trade-in).
- Optimasi tipe data: Kolom berulang dikonversi ke tipe `category` untuk efisiensi memori.

---------

## 🚀 Panduan Memulai & Cara Menjalankan

### 1. Prasyarat Sistem
- Python versi **3.10** atau yang lebih baru.
- Manajer paket `pip`.

### 2. Kloning Repositori & Instalasi Dependensi
```bash
# Masuk ke direktori proyek
cd analis

# Instal dependensi pustaka
pip install -r requirements.txt
```

### 3. Menjalankan Pipeline Pembersihan Data
Eksekusi modul [`data_loader.py`](src/data_loader.py) untuk memproses data mentah menjadi `data_cleaned.csv`:
```bash
python -m src.data_loader
```

### 4. Menghasilkan Grafik Visualisasi & Laporan Eksekutif
Eksekusi modul [`analysis_utils.py`](src/analysis_utils.py) untuk memperbarui seluruh grafik di [`outputs/figures/`](outputs/figures/) dan laporan [`outputs/summary_report.md`](outputs/summary_report.md):
```bash
python -m src.analysis_utils
```

### 5. Membuka Jupyter Notebook Interaktif
Untuk menelusuri seluruh tahapan analisis interaktif (audit, visualisasi, dan narasi bisnis):
```bash
jupyter notebook notebooks/01_eda_and_insights.ipynb
```

### 6. Menjalankan Tugas Google Colab
Tersedia berkas [`colab_notebook.ipynb`](colab_notebook.ipynb) yang dirancang untuk pembelajaran terpandu (5 soal latihan analitik):
- Untuk mengekstrak pertanyaan: `python extract_colab.py`
- Untuk menginjeksi solusi otomatis: `python solve_colab.py`

---

## 📖 Struktur Analisis di Jupyter Notebook

Notebook [`notebooks/01_eda_and_insights.ipynb`](notebooks/01_eda_and_insights.ipynb) disusun secara terstruktur ke dalam 10 bab:

1. **Pengenalan & Kerangka Analisis**: Latar belakang bisnis, tujuan, dan perumusan hipotesis.
2. **Pemuatan & Audit Kualitas Data**: Pengecekan dimensi, *missing values*, data duplikat, dan tipe data.
3. **Pembersihan Data & Rekayasa Fitur**: Transformasi datetime, pemisahan brand, dan kalkulasi rasio keuangan.
4. **Analisis Univariat & Distribusi Data**: Sebaran harga kendaraan, volume pembelian, dan diskon.
5. **Analisis Tren Penjualan Musiman**: Perbandingan kuartalan (Q1–Q4) dan dinamika bulanan sepanjang 2025.
6. **Evaluasi Performa Antar-Cabang**: Pemetaan omzet kotor, kas bersih, dan efisiensi 10 cabang operasional.
7. **Analisis Portofolio Produk & Tren EV**: Pemeringkatan model terlaris dan adopsi mobil listrik perkotaan.
8. **Dinamika Pembayaran & Anomali Trade-In**: Komparasi tunai vs kredit serta analisis 251 kasus nilai tukar tambah berlebih.
9. **Analisis Risiko Operasional**: Tingkat *cancellation* dan *refund* untuk perbaikan logistik dealer.
10. **Kesimpulan Eksekutif & Rekomendasi Bisnis**: Sintesis temuan dan aksi strategis untuk manajemen.

---

## 🎯 Rekomendasi Strategis Manajerial

1. **Manajemen Likuiditas & Plafon Program Trade-In**:
   - Terapkan batas maksimum (*capping*) penilaian unit tukar tambah atau alihkan sisa dana lebih (*excess trade-in value*) menjadi saldo perawatan/aksesoris berkala, guna memitigasi risiko arus kas negatif (*cash deficit*).
2. **Kemitraan Multifinance Agresif**:
   - Mempertimbangkan tingginya porsi kredit (62,5%), buat program pembiayaan bersama eksklusif (*joint promo*) dengan DP ringan dan suku bunga kompetitif untuk memacu penjualan model MPV & SUV.
3. **Perluasan Infrastruktur & Edukasi Segmen EV**:
   - Respons tingginya minat terhadap City Car EV dengan menyediakan fasilitas *fast-charging station* gratis di area showroom dan bundel paket *home-charging installation*.
4. **Perbaikan SLA & Manajemen Stok Indent**:
   - Prioritaskan pemenuhan alokasi unit pada cabang-cabang dengan rasio pembatalan tinggi untuk memangkas masa tunggu pelanggan dan menurunkan *cancellation rate*.

---

## 📋 Dependensi & Teknologi

- **Bahasa Pemrograman**: [Python 3.10+](https://www.python.org/)
- **Manipulasi & Transformasi Data**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualisasi Data**: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Lingkungan Komputasi**: [Jupyter Notebook](https://jupyter.org/) / Google Colab

---

## 📄 Lisensi & Dokumentasi Terkait

- Spesifikasi kebutuhan lengkap: lihat [PRD.md](PRD.md)
- Ringkasan eksekutif: lihat [outputs/summary_report.md](outputs/summary_report.md)
- Soal studi kasus Colab: lihat [colab_questions.md](colab_questions.md)
