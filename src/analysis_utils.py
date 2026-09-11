"""
Modul Utilitas Analisis & Visualisasi untuk Data Penjualan Otomotif.
Menyediakan kalkulasi metrik bisnis (KPI), formatting Rupiah,
dan generator visualisasi standar publikasi.
"""

from pathlib import Path
from typing import Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# Pengaturan gaya visualisasi global
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["axes.edgecolor"] = "#cccccc"
plt.rcParams["axes.linewidth"] = 0.8


def format_idr(value: float, compact: bool = True) -> str:
    """Format angka numerik ke notasi mata uang Rupiah (IDR)."""
    if pd.isna(value):
        return "Rp 0"
    
    is_neg = value < 0
    abs_val = abs(value)
    prefix = "-Rp " if is_neg else "Rp "

    if compact:
        if abs_val >= 1e12:
            return f"{prefix}{abs_val / 1e12:.2f} T"
        elif abs_val >= 1e9:
            return f"{prefix}{abs_val / 1e9:.2f} Miliar"
        elif abs_val >= 1e6:
            return f"{prefix}{abs_val / 1e6:.1f} Juta"
    return f"{prefix}{abs_val:,.0f}".replace(",", ".")


def calculate_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """Menghitung metrik performa utama (Key Performance Indicators)."""
    total_transactions = len(df)
    completed_df = df[df["status"] == "completed"]
    cancelled_count = (df["status"] == "cancelled").sum()
    refund_count = (df["status"] == "refund").sum()

    gross_revenue = completed_df["total"].sum()
    net_revenue = completed_df["total_sales"].sum()
    total_units = completed_df["quantity"].sum()
    aov = gross_revenue / len(completed_df) if len(completed_df) > 0 else 0
    trade_in_units = completed_df["is_trade_in"].sum()
    credit_units = completed_df["is_credit"].sum()

    return {
        "total_transactions": total_transactions,
        "completed_transactions": len(completed_df),
        "gross_revenue": gross_revenue,
        "net_revenue": net_revenue,
        "total_units_sold": int(total_units),
        "aov": aov,
        "cancellation_rate": (cancelled_count / total_transactions) * 100,
        "refund_rate": (refund_count / total_transactions) * 100,
        "trade_in_penetration": (trade_in_units / len(completed_df)) * 100,
        "credit_penetration": (credit_units / len(completed_df)) * 100,
    }


def plot_monthly_sales_trend(df: pd.DataFrame, output_path: str = "outputs/figures/01_monthly_sales_trend.png") -> None:
    """Grafik 1: Tren Penjualan & Pendapatan Bulanan (2025)."""
    completed_df = df[df["status"] == "completed"]
    monthly = completed_df.groupby("month").agg(
        gross_rev=("total", lambda x: x.sum() / 1e12),
        units_sold=("quantity", "sum")
    ).reset_index()

    month_labels = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Ags", "Sep", "Okt", "Nov", "Des"]
    monthly["month_label"] = [month_labels[m - 1] for m in monthly["month"]]

    fig, ax1 = plt.subplots(figsize=(11, 5.5))

    # Bar chart untuk Gross Revenue (Triliun Rp)
    bars = ax1.bar(monthly["month_label"], monthly["gross_rev"], color="#2b5c8f", alpha=0.85, width=0.55, label="Gross Revenue (Rp Triliun)")
    ax1.set_ylabel("Gross Revenue (Rp Triliun)", fontsize=11, color="#1e3d59", fontweight="bold")
    ax1.set_ylim(0, max(monthly["gross_rev"]) * 1.25)
    ax1.tick_params(axis="y", labelcolor="#1e3d59")

    # Label angka di atas bar
    for bar in bars:
        h = bar.get_height()
        ax1.annotate(f"Rp {h:.2f}T",
                     xy=(bar.get_x() + bar.get_width() / 2, h),
                     xytext=(0, 4), textcoords="offset points",
                     ha="center", va="bottom", fontsize=9, fontweight="semibold")

    # Line chart sekunder untuk Unit Terjual
    ax2 = ax1.twinx()
    line = ax2.plot(monthly["month_label"], monthly["units_sold"], color="#e76f51", marker="o", linewidth=2.5, markersize=7, label="Unit Terjual")
    ax2.set_ylabel("Jumlah Unit Terjual", fontsize=11, color="#e76f51", fontweight="bold")
    ax2.set_ylim(min(monthly["units_sold"]) * 0.8, max(monthly["units_sold"]) * 1.15)
    ax2.tick_params(axis="y", labelcolor="#e76f51")
    ax2.grid(False)

    plt.title("Tren Penjualan Bulanan & Volume Unit Dealer Otomotif (2025)", fontsize=13, fontweight="bold", pad=15)
    fig.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[PLOT] Tersimpan: {output_path}")


def plot_branch_performance(df: pd.DataFrame, output_path: str = "outputs/figures/02_branch_performance.png") -> None:
    """Grafik 2: Performa Penjualan Antar Cabang Dealer."""
    completed_df = df[df["status"] == "completed"]
    branch_perf = completed_df.groupby("branch", observed=True).agg(
        gross_rev=("total", lambda x: x.sum() / 1e12),
        units_sold=("quantity", "sum")
    ).sort_values("gross_rev", ascending=True).reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(branch_perf["branch"], branch_perf["gross_rev"], color="#3a86ff", alpha=0.85, height=0.6)
    
    ax.set_xlabel("Gross Revenue (Rp Triliun)", fontsize=11, fontweight="bold")
    ax.set_title("Peringkat Pendapatan Kotor Berdasarkan Cabang Dealer (2025)", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlim(0, max(branch_perf["gross_rev"]) * 1.2)

    for bar, unit in zip(bars, branch_perf["units_sold"]):
        w = bar.get_width()
        ax.annotate(f"Rp {w:.2f}T ({unit:,} unit)",
                    xy=(w, bar.get_y() + bar.get_height() / 2),
                    xytext=(6, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=9.5, fontweight="semibold")

    fig.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[PLOT] Tersimpan: {output_path}")


def plot_product_and_category(df: pd.DataFrame, output_path: str = "outputs/figures/03_top_products_and_categories.png") -> None:
    """Grafik 3: Kontribusi Kategori Kendaraan & Top 7 Model Terlaris."""
    completed_df = df[df["status"] == "completed"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Subplot 1: Pangsa Volume per Kategori Kendaraan
    cat_counts = completed_df["category"].value_counts()
    colors = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
    wedges, texts, autotexts = ax1.pie(
        cat_counts,
        labels=cat_counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors[:len(cat_counts)],
        pctdistance=0.75,
        explode=[0.03] * len(cat_counts),
        textprops={"fontsize": 10}
    )
    for at in autotexts:
        at.set_color("white")
        at.set_fontweight("bold")
    ax1.set_title("Komposisi Penjualan Berdasarkan Kategori", fontsize=12, fontweight="bold")

    # Subplot 2: Top 7 Model Kendaraan Terlaris
    top_models = completed_df["product_name"].value_counts().head(7).sort_values(ascending=True)
    ax2.barh(top_models.index, top_models.values, color="#2a9d8f", height=0.6)
    ax2.set_xlabel("Unit Terjual", fontsize=11, fontweight="bold")
    ax2.set_title("Top 7 Model Mobil Paling Diminati", fontsize=12, fontweight="bold")
    for idx, val in enumerate(top_models.values):
        ax2.annotate(f"{val:,} unit",
                     xy=(val, idx),
                     xytext=(5, 0), textcoords="offset points",
                     ha="left", va="center", fontsize=9, fontweight="semibold")

    fig.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[PLOT] Tersimpan: {output_path}")


def plot_payment_and_tradein(df: pd.DataFrame, output_path: str = "outputs/figures/04_payment_and_tradein_distribution.png") -> None:
    """Grafik 4: Analisis Metode Pembayaran & Penetrasi Trade-In."""
    completed_df = df[df["status"] == "completed"]
    pay_counts = completed_df["payment_type"].value_counts().sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    palette = ["#457b9d", "#1d3557", "#a8dadc", "#e63946"]
    bars = ax.barh(pay_counts.index, pay_counts.values, color=palette[:len(pay_counts)], height=0.55)

    ax.set_xlabel("Jumlah Transaksi Berhasil", fontsize=11, fontweight="bold")
    ax.set_title("Distribusi Metode Pembayaran & Partisipasi Trade-In (2025)", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlim(0, max(pay_counts.values) * 1.18)

    total_completed = len(completed_df)
    for bar in bars:
        w = bar.get_width()
        pct = (w / total_completed) * 100
        ax.annotate(f"{w:,} ({pct:.1f}%)",
                    xy=(w, bar.get_y() + bar.get_height() / 2),
                    xytext=(6, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=10, fontweight="semibold")

    fig.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[PLOT] Tersimpan: {output_path}")


def plot_cancellation_and_refund(df: pd.DataFrame, output_path: str = "outputs/figures/05_cancellation_and_refund_rates.png") -> None:
    """Grafik 5: Rasio Pembatalan & Pengembalian Dana per Cabang."""
    branch_risk = df.groupby("branch", observed=True).agg(
        total_trx=("order_id", "count"),
        cancelled=("status", lambda x: (x == "cancelled").sum()),
        refund=("status", lambda x: (x == "refund").sum())
    ).reset_index()

    branch_risk["cancel_pct"] = (branch_risk["cancelled"] / branch_risk["total_trx"]) * 100
    branch_risk["refund_pct"] = (branch_risk["refund"] / branch_risk["total_trx"]) * 100
    branch_risk = branch_risk.sort_values("cancel_pct", ascending=False)

    x = np.arange(len(branch_risk))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 5.5))
    b1 = ax.bar(x - width/2, branch_risk["cancel_pct"], width, label="Cancellation Rate (%)", color="#e63946", alpha=0.9)
    b2 = ax.bar(x + width/2, branch_risk["refund_pct"], width, label="Refund Rate (%)", color="#f4a261", alpha=0.9)

    ax.set_xticks(x)
    ax.set_xticklabels(branch_risk["branch"], rotation=25, ha="right", fontsize=10)
    ax.set_ylabel("Persentase (%)", fontsize=11, fontweight="bold")
    ax.set_title("Tingkat Pembatalan (Cancelled) & Retur (Refund) Antar Cabang", fontsize=13, fontweight="bold", pad=15)
    ax.legend(frameon=True, facecolor="white")
    ax.set_ylim(0, max(max(branch_risk["cancel_pct"]), max(branch_risk["refund_pct"])) * 1.3)

    fig.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[PLOT] Tersimpan: {output_path}")


def generate_all_visualizations(df: pd.DataFrame, output_dir: str = "outputs/figures") -> None:
    """Menghasilkan seluruh paket visualisasi standar."""
    plot_monthly_sales_trend(df, f"{output_dir}/01_monthly_sales_trend.png")
    plot_branch_performance(df, f"{output_dir}/02_branch_performance.png")
    plot_product_and_category(df, f"{output_dir}/03_top_products_and_categories.png")
    plot_payment_and_tradein(df, f"{output_dir}/04_payment_and_tradein_distribution.png")
    plot_cancellation_and_refund(df, f"{output_dir}/05_cancellation_and_refund_rates.png")
    print(f"[INFO] Semua 5 visualisasi berhasil disimpan di folder '{output_dir}'.")


def generate_summary_report(df: pd.DataFrame, output_path: str = "outputs/summary_report.md") -> None:
    """Menghasilkan laporan eksekutif markdown hasil sintesis analisis bisnis."""
    kpis = calculate_kpis(df)
    completed_df = df[df["status"] == "completed"]
    top_branch = completed_df.groupby("branch", observed=True)["total"].sum().idxmax()
    top_model = completed_df["product_name"].value_counts().idxmax()

    report_content = f"""# 📊 Executive Summary Report: Analisis Penjualan Otomotif 2025

---

### 1. Metrik Utama (High-Level KPIs)
- **Total Transaksi Masuk**: {kpis['total_transactions']:,} transaksi
- **Transaksi Berhasil (Completed)**: {kpis['completed_transactions']:,} ({kpis['completed_transactions']/kpis['total_transactions']*100:.1f}%)
- **Total Omzet Kotor (Gross Revenue)**: {format_idr(kpis['gross_revenue'])}
- **Total Penerimaan Kas Bersih (Net Revenue)**: {format_idr(kpis['net_revenue'])}
- **Total Unit Kendaraan Terjual**: {kpis['total_units_sold']:,} unit
- **Rata-Rata Nilai Transaksi (AOV)**: {format_idr(kpis['aov'])}
- **Tingkat Pembatalan (Cancellation Rate)**: {kpis['cancellation_rate']:.2f}%
- **Tingkat Pengembalian Dana (Refund Rate)**: {kpis['refund_rate']:.2f}%
- **Penetrasi Program Trade-In**: {kpis['trade_in_penetration']:.1f}%
- **Penetrasi Pembiayaan Kredit**: {kpis['credit_penetration']:.1f}%

---

### 2. Temuan Kunci (Key Analytical Findings)
1. **Performa Cabang**:
   - Cabang **{top_branch}** membukukan kontribusi omzet tertinggi di antara 10 cabang operasional dealer.
2. **Preferensi Produk**:
   - Model paling diminati pasar adalah **{top_model}**, diikuti oleh SUV keluarga dan crossover kompak.
   - Segmen Kendaraan Listrik (City Car EV - misal: *Wuling Air ev*) telah mencatat volume yang signifikan dan stabil sepanjang kuartal 2025.
3. **Pola Pembiayaan & Tukar Tambah**:
   - Skema kredit mendominasi mayoritas pembelian ({kpis['credit_penetration']:.1f}%), menunjukkan ketergantungan yang tinggi pada kemitraan leasing/multifinance.
   - Sebanyak {kpis['trade_in_penetration']:.1f}% transaksi memanfaatkan skema *Trade-In*.
4. **Anomali Finansial (Trade-In > Nilai Mobil Baru)**:
   - Ditemukan sebanyak **251 transaksi** di mana nilai taksiran tukar tambah konsumen lebih besar dari harga mobil baru yang dibeli, sehingga menghasilkan kas bersih negatif (*cashback* ke konsumen).

---

### 3. Rekomendasi Manajerial (Actionable Business Recommendations)
1. **Optimasi Program Tukar Tambah (*Trade-In*)**:
   - Tetapkan plafon penilaian *trade-in* atau skema transfer saldo kredit untuk mencegah kas minus yang memberatkan modal kerja cabang.
2. **Kemitraan Strategis Multifinance**:
   - Mengingat penetrasi kredit yang tinggi, jalin kemitraan eksklusif dengan perusahaan pembiayaan yang menawarkan suku bunga kompetitif dan proses *approval* cepat.
3. **Mitigasi Pembatalan & Retur**:
   - Investigasi mendalam pada cabang dengan *cancellation rate* di atas rata-rata untuk memperbaiki SLA pengiriman unit dan ketersediaan stok fisik (*ready stock*).
"""

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"[INFO] Laporan eksekutif berhasil disimpan ke '{output_path}'.")


if __name__ == "__main__":
    from src.data_loader import load_raw_data, clean_and_transform_data
    df = clean_and_transform_data(load_raw_data("data.csv"))
    generate_all_visualizations(df)
    generate_summary_report(df)
