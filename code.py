
#!/usr/bin/env python3
# XTAN TKJ TOOLKIT
# Educational network and Linux utilities

import os
import sys
import socket
import subprocess
import ipaddress
import platform
import urllib.request
from datetime import datetime

VERSION = "1.0.0"
REPORT = "laporan_tkj.txt"

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"


def run_command(args, timeout=15):
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip() or result.stderr.strip() or \
            f"Perintah selesai (kode {result.returncode})."
    except FileNotFoundError:
        return "Perintah tidak tersedia. Instal paket yang diperlukan."
    except subprocess.TimeoutExpired:
        return "Waktu pemeriksaan habis."
    except Exception as exc:
        return f"Terjadi error: {exc}"


def pause():
    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")


def header():
    os.system("clear")
    print(CYAN + BOLD + r"""
 __  __ _____ _   _   _   _ _  __
 \ \/ /|_   _| \ | | | | | | |/ /
  \  /   | | |  \| | | | | | ' /
  /  \   | | | |\  | | |_| | . \
 /_/\_\  |_| |_| \_|  \___/|_|\_\

        TKJ TOOLKIT v1.0
        POWERED BY XTAN
""" + RESET)


def save_report(title, content):
    try:
        with open(REPORT, "a", encoding="utf-8") as file:
            file.write(f"\n[{datetime.now()}] {title}\n")
            file.write(content + "\n")
        print(GREEN + f"Laporan disimpan: {REPORT}" + RESET)
    except OSError as exc:
        print(RED + f"Gagal menyimpan: {exc}" + RESET)


def network_info():
    print(CYAN + "\n=== INFORMASI JARINGAN ===" + RESET)
    outputs = []

    for title, command in [
        ("Alamat IP dan interface", ["ip", "addr", "show"]),
        ("Routing / gateway", ["ip", "route", "show"]),
        ("DNS resolver", ["cat", "/etc/resolv.conf"]),
    ]:
        result = run_command(command)
        outputs.append(f"{title}\n{result}")
        print(f"\n{BOLD}{title}{RESET}\n{result}")

    save_report("Informasi Jaringan", "\n".join(outputs))
    pause()


def ping_test():
    host = input("Masukkan domain/IP tujuan: ").strip()

    if not host or any(c.isspace() for c in host):
        print(RED + "Input tidak valid." + RESET)
        pause()
        return

    try:
        socket.getaddrinfo(host, None)
    except socket.gaierror:
        print(RED + "Domain tidak ditemukan atau jaringan bermasalah." + RESET)
        pause()
        return

    count = "4"
    command = ["ping", "-c", count, "-W", "3", host]
    print(f"\nMenguji koneksi ke {host}...\n")
    result = run_command(command, timeout=20)
    print(result)
    save_report(f"Ping: {host}", result)
    pause()


def dns_lookup():
    domain = input("Masukkan domain (contoh: example.com): ").strip()

    if not domain or any(c.isspace() for c in domain):
        print(RED + "Domain tidak valid." + RESET)
        pause()
        return

    print("\n=== DNS LOOKUP ===")
    result = run_command(["nslookup", domain])
    print(result)
    save_report(f"DNS Lookup: {domain}", result)
    pause()


def subnet_calculator():
    print("\n=== KALKULATOR SUBNET IPv4 ===")
    value = input("Masukkan IPv4/CIDR (contoh 192.168.1.10/24): ").strip()

    try:
        net = ipaddress.ip_interface(value)
        network = net.network
        data = (
            f"IP address : {net.ip}\n"
            f"Prefix     : /{network.prefixlen}\n"
            f"Netmask    : {network.netmask}\n"
            f"Network    : {network.network_address}\n"
            f"Broadcast  : {network.broadcast_address}\n"
            f"Total IP   : {network.num_addresses}\n"
            f"Host usable: {max(0, network.num_addresses - 2) if network.prefixlen < 31 else network.num_addresses}"
        )
        print("\n" + GREEN + data + RESET)
        save_report("Kalkulator Subnet", data)
    except ValueError:
        print(RED + "Format IPv4/CIDR tidak valid." + RESET)

    pause()


def http_headers():
    print("\n=== HTTP HEADER CHECK ===")
    url = input("URL situs yang ingin diperiksa: ").strip()

    if not url.startswith(("http://", "https://")):
        print(RED + "URL wajib memakai http:// atau https://." + RESET)
        pause()
        return

    try:
        request = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "Xtan-TKJ-Toolkit/1.0"}
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            lines = [f"Status HTTP: {response.status}"]
            lines.extend(f"{key}: {value}" for key, value in response.headers.items())
            result = "\n".join(lines)
    except Exception as exc:
        result = f"Pemeriksaan gagal: {exc}"

    print(result)
    save_report(f"HTTP Header: {url}", result)
    pause()


def traceroute_test():
    host = input("Domain/IP tujuan: ").strip()

    if not host or any(c.isspace() for c in host):
        print(RED + "Input tidak valid." + RESET)
        pause()
        return

    try:
        socket.getaddrinfo(host, None)
    except socket.gaierror:
        print(RED + "Domain tidak ditemukan." + RESET)
        pause()
        return

    print("\nTraceroute dapat dibatasi jaringan atau operator.\n")
    result = run_command(["traceroute", "-m", "12", "-w", "2", host], timeout=35)
    print(result)
    save_report(f"Traceroute: {host}", result)
    pause()


def system_info():
    data = (
        f"Sistem: {platform.system()}\n"
        f"Versi: {platform.version()}\n"
        f"Arsitektur: {platform.machine()}\n"
        f"Python: {platform.python_version()}\n"
        f"Hostname: {socket.gethostname()}\n"
        f"Waktu: {datetime.now()}"
    )
    print("\n" + data)
    save_report("Informasi Sistem", data)
    pause()


def linux_guide():
    print(CYAN + """
=== PANDUAN PERINTAH LINUX ===

File & folder:
  pwd                 Lokasi direktori saat ini
  ls -la              Daftar file
  cd nama_folder      Pindah direktori
  mkdir folder_baru   Buat direktori
  cp file tujuan      Salin file
  mv file tujuan      Pindahkan/ubah nama
  cat nama_file       Baca isi file

Jaringan:
  ip addr             Informasi interface/IP
  ip route            Tabel routing
  ping -c 4 1.1.1.1   Uji koneksi
  nslookup example.com DNS lookup
  curl -I https://example.com
                      Lihat HTTP headers

Sistem:
  uname -a            Informasi kernel
  df -h               Ruang penyimpanan
  free -h             Penggunaan RAM jika tersedia
  ps                  Proses yang berjalan
  top                 Pantau proses
  pkg search nama     Cari paket Termux
  pkg install nama    Instal paket

Gunakan perintah hanya pada perangkat
dan jaringan yang kamu berhak periksa.
""" + RESET)
    pause()


def main():
    while True:
        header()
        print(" [1] Informasi jaringan")
        print(" [2] Ping / latency test")
        print(" [3] DNS lookup")
        print(" [4] Kalkulator subnet IPv4")
        print(" [5] HTTP header checker")
        print(" [6] Traceroute")
        print(" [7] Informasi sistem")
        print(" [8] Panduan perintah Linux")
        print(" [9] Keluar")
        print("\n" + CYAN + "Powered by Xtan" + RESET)

        choice = input("\nPilih menu [1-9]: ").strip()

        actions = {
            "1": network_info,
            "2": ping_test,
            "3": dns_lookup,
            "4": subnet_calculator,
            "5": http_headers,
            "6": traceroute_test,
            "7": system_info,
            "8": linux_guide,
        }

        if choice == "9":
            print(GREEN + "Terima kasih telah belajar bersama Xtan." + RESET)
            break
        elif choice in actions:
            try:
                actions[choice]()
            except KeyboardInterrupt:
                print("\nPemeriksaan dibatalkan.")
                pause()
            except Exception as exc:
                print(RED + f"Terjadi error: {exc}" + RESET)
                pause()
        else:
            print(RED + "Pilihan tidak tersedia." + RESET)
            pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
        sys.exit(0)
  
