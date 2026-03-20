# 00 — Installation

The first step is getting Python up and running on your machine. This lesson covers installation on Windows and macOS, and how to verify everything is working correctly.

---

## Installing Python on Windows

1. Go to [python.org/downloads](https://python.org/downloads) and click **Download Python**.
2. Once downloaded, double-click the installer.

> ⚠️ **Important**: Before clicking "Install", make sure to check the box **"Add Python to PATH"**. Without this, Python won't be accessible from the command line.

3. Follow the installer steps without customising anything unless you know what you're doing.
4. Click **Install** and wait for it to finish.

### Verify the installation

Open the Command Prompt and run:

```bash
python --version
```

You should see something like `Python 3.13.5`.

---

## Installing Python on macOS

Many Macs come with Python pre-installed. To check, open the Terminal (`Cmd + Space`, type "Terminal") and run:

```bash
python3 --version
```

If you see a version number, you're good to go. If not, install it using one of the following methods.

### Option 1 — Download from python.org

1. Go to [python.org/downloads](https://python.org/downloads).
2. Click the download button (it auto-detects your OS).
3. Open the downloaded file and follow the installer steps.

### Option 2 — Install with Homebrew (recommended)

If you have [Homebrew](https://brew.sh/) installed, you can install Python directly from the terminal:

```bash
brew install python
```

This automatically installs the latest version and configures everything correctly.

### Verify the installation

```bash
python3 --version
```

You should see something like `Python 3.13.5`.

---

## Which version should I use?

Always use **Python 3.10 or higher**. Python 2 is no longer supported and you will not encounter it in modern AI engineering projects.

Throughout this repository, we will use `python` on Windows and `python3` on macOS/Linux. Both refer to the same thing — the difference is just how each OS handles the command name.

---

## Next steps

With Python installed, you are ready to start coding. In the next lesson we will write our first lines of Python and understand how the language works.