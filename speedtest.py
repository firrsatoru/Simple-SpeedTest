import speedtest

def run_speedtest():
    st = speedtest.Speedtest()
    
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Ubah Dari bit/s ke Mbit/s
    upload_speed = st.upload() / 1_000_000      # Ubah Dari bit/s ke Mbit/s

    # Results
    print(f"Download: {download_speed:.2f} Mbps")
    print(f"Upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    run_speedtest()
