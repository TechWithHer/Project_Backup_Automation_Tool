Here is a complete and professional **`docs/03_Developer_Guide.md`** file for your `Project10_Backup_Automation_Tool`. It follows **industry standards** and covers all aspects a developer would need to contribute, extend, test, or deploy the project.

---

### ✅ `docs/03_Developer_Guide.md`

```markdown
# 👨‍💻 Developer Guide - Backup Automation Tool

## 📌 Purpose

This guide is for developers who want to:
- Understand the codebase
- Extend features or contribute
- Run the tool locally
- Set up tests and CI/CD
- Deploy to production or cloud

---

## 🧱 Project Structure

```

Project10\_Backup\_Automation\_Tool/
├── main.py
├── backup/
│   └── compressor.py
├── storage/
│   └── s3\_uploader.py
├── utils/
│   ├── logger.py
│   └── helpers.py
├── tests/
│   ├── test\_main.py
│   ├── test\_compressor.py
│   └── test\_s3\_uploader.py
├── docs/
├── logs/
├── backups/
├── requirements.txt
├── .env.example
└── README.md

````

---

## 🏃‍♂️ Getting Started

### 🔧 Prerequisites
- Python 3.10+
- AWS account (for S3 access)
- pip, virtualenv (recommended)
- Git

### 📥 Installation

```bash
git clone https://github.com/yourname/Project10_Backup_Automation_Tool.git
cd Project10_Backup_Automation_Tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

## ⚙️ Environment Setup

1. Copy `.env.example` to `.env` and update with your AWS credentials:

```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=ap-southeast-1
S3_BUCKET_NAME=your-bucket-name
```

2. Ensure `.env` is listed in `.gitignore`

---

## 🧠 Codebase Overview

| File/Folder              | Purpose                                   |
| ------------------------ | ----------------------------------------- |
| `main.py`                | CLI handler and orchestrator              |
| `backup/compressor.py`   | Logic to compress files/folders           |
| `storage/s3_uploader.py` | Uploads files to S3                       |
| `utils/logger.py`        | Logs all backup actions                   |
| `utils/helpers.py`       | Common helper functions (e.g., timestamp) |
| `tests/`                 | Unit tests for all modules                |
| `backups/`               | Stores local backups                      |
| `logs/`                  | Contains all log files                    |

---

## ✅ How It Works

1. User provides:

   * Source file/folder path
   * Backup format (.zip, .tar.gz, etc.)
   * Custom name (optional)
   * Upload to S3: Yes/No

2. System compresses source → creates backup

3. If enabled, backup is uploaded to AWS S3

4. All steps are logged to `logs/backup.log`

---

## 🧪 Running Tests

Unit tests use `pytest`:

```bash
pip install pytest
pytest tests/
```

To run a specific test:

```bash
pytest tests/test_compressor.py
```

---

## 🚀 Deployment (Optional)

This tool is CLI-based but can be:

* Scheduled via **cron** or **task scheduler**
* Integrated with CI/CD using GitHub Actions
* Deployed to AWS EC2 or Dockerized

---

## 🤝 Contributing

### Git Workflow

```bash
git checkout -b feature/my-feature
# make changes
git add .
git commit -m "Add: feature xyz"
git push origin feature/my-feature
```

Create a Pull Request with a detailed description.

### Coding Standards

* Follow **PEP8** (autoformat using `black`)
* Add **docstrings** to all functions
* Write/extend tests when adding features

---

## 🧭 Developer Responsibilities

| Task                     | Mandatory |
| ------------------------ | --------- |
| Logging                  | ✅         |
| Writing tests            | ✅         |
| Using `.env` for secrets | ✅         |
| Avoid hardcoding paths   | ✅         |
| Follow Git workflow      | ✅         |

---

## 💡 Example Extensions

| Feature                   | Complexity | Guide                      |
| ------------------------- | ---------- | -------------------------- |
| Add GUI (Tkinter or PyQt) | Medium     | Wrap around CLI logic      |
| Add email alerts          | Medium     | Use `smtplib` in `utils/`  |
| Encrypt backup files      | Advanced   | Use `cryptography` module  |
| Add retry for S3 upload   | Easy       | Use `boto3` retry strategy |

---

## 🧷 Helpful Commands

| Command          | Use Case                 |
| ---------------- | ------------------------ |
| `python main.py` | Run CLI                  |
| `pytest`         | Run all tests            |
| `black .`        | Format code              |
| `deactivate`     | Exit virtual environment |

---

## 🔗 References

* [AWS S3 boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
* [PEP8 Guidelines](https://peps.python.org/pep-0008/)
* [pytest Docs](https://docs.pytest.org/en/7.1.x/)

---

```

### 📍 Place This File Here:

```

docs/
├── 01\_User\_Guide.md
├── 02\_Architecture.md
├── 03\_Developer\_Guide.md    ✅ <--- This file
├── 07\_Use\_Case\_Stories.md

```

---

Would you like me to also generate:
- `.env.example` file content?
- `CONTRIBUTING.md` for open source-style contributions?

Let me know!
```
