# Speedtest CLI Script

Sebuah script Python sederhana untuk mengukur kecepatan **Download** dan **Upload** menggunakan library `speedtest-cli`

## How To Works

Script ini memanfaatkan library `speedtest-cli` untuk melakukan pengujian kecepatan internet dengan mengukur kecepatan unduh (download) dan unggah (upload) dalam satuan Megabit per detik (Mbps)

## Information 

Pastikan kamu sudah menginstal Python dan library `speedtest-cli` di terminal kamu

### Installation

1. **Python 3.x** harus sudah terpasang. Kamu bisa mengecek dengan menjalankan cmd berikut:

    ```bash
    python --version
    ```

2. Instal **speedtest-cli** menggunakan pip:

    ```bash
    pip install speedtest-cli
    ```

## Penggunaan

Setelah instalasi selesai, kamu bisa menjalankan script dengan cara berikut:

1. Salin kode berikut ke dalam file Python, misalnya `speedtest_script.py`:

    ```python
    import speedtest

    def run_speedtest():
        st = speedtest.Speedtest()

        st.get_best_server()

        download_speed = st.download() / 1_000_000  # Ubah dari bit/s ke Mbit/s
        upload_speed = st.upload() / 1_000_000      # Ubah dari bit/s ke Mbit/s

        # Results
        print(f"Download: {download_speed:.2f} Mbps")
        print(f"Upload: {upload_speed:.2f} Mbps")

    if __name__ == "__main__":
        run_speedtest()
    ```

2. Jalankan script dengan perintah:

    ```bash
    python speedtest_script.py
    ```

3. Hasil dari kecepatan (download) dan (upload) akan ditampilkan di terminal dalam format berikut:

    ```
    Download: 50.23 Mbps
    Upload: 10.45 Mbps
    ```

## Examples Code 

- **`speedtest.Speedtest()`**: Inisialisasi objek untuk menjalankan speedtest
- **`st.get_best_server()`**: Memilih server terbaik berdasarkan latency
- **`st.download()`**: Mengukur kecepatan download dan hasilnya dikonversi dari bit per detik ke Megabit per detik (Mbps)
- **`st.upload()`**: Mengukur kecepatan upload dan hasilnya juga dikonversi dari bit per detik ke Megabit per detik (Mbps)
