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
Enter your hackerone username: johndoe
Enter IP or domain: example.com
```

## 📌 Sample Output

```
Scanning Ports: 100%|████████████████████████████| 65535/65535
Port 80 responded with status code: 200
Port 443 responded with status code: 403

Total open HTTP ports with the header: 2
Open HTTP ports: [80, 443]
```

## 📁 Project Structure

```
http-port-scanner/
├── scanner.py           # Main scanner script
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it
```

## 💡 Notes

- Only uses **30 threads** to comply with HackerOne's infrastructure guidelines.
- You can customize timeouts, headers, or ports if needed.
- Use responsibly. This tool is for ethical research only.

## 🛡️ Disclaimer

This tool is intended for **authorized security research** only. Do **not** scan systems you do not have permission to test. The author assumes no liability for misuse.

## 🧑‍💻 Author

Made with ❤️ by [@basit67](https://github.com/basit67)
