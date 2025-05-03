# 🔍 HTTP Port Scanner (HackerOne Edition)

A fast, multithreaded Python tool to scan all 65,535 TCP ports for HTTP responses on a given target. Designed for **HackerOne reconnaissance**, it includes a custom HTTP header with your HackerOne username and shows real-time progress.

## 📥 Clone This Repo

```bash
git clone https://github.com/basit67/HTTP-Port-Scanner-HackerOne-Edition
cd HTTP-Port-Scanner-HackerOne-Edition
```

## ⚙️ Features

- ✅ Scans all TCP ports (1–65535)
- 🚀 Multithreaded (30 threads — HackerOne safe)
- 📈 Real-time progress bar via `tqdm`
- 🌐 Uses custom header: `X-HackerOne-Research`
- 🧠 Smart: detects common HTTP response codes
- ⚡ Optimized with persistent `requests.Session`

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## 📄 Usage

```bash
python scanner.py
```

Then follow the prompts:

```
