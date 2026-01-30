
# Windows Movie Maker 2012 RPC

Adds a Rich Presence to your Discord profile when using Windows Movie Maker 2012 desktop app

## ⚙️ How it works?

This script will find the PID of WMM 2012 to get the window title and use it to display a nice-looking RPC using the python library [PyPresence](https://github.com/qwertyquerty/pypresence).
> This is NOT a Discord bot. It uses Discord Rich Presence via a local client ID.

## 📜 Requirements

- Windows
- Python 3.8+
- Discord (desktop)
- Windows Movie Maker 2012

## ⭐ The Rich Presence displays

- Windows Movie Maker 2012
- Current project name (from window title)
- Custom icon

## 🛠️ How to use?

1. [Go to Discord Developers Portal](https://discord.com/developers/applications)
2. Add this image to RPC assets: `https://files.catbox.moe/njypo8.png`  and name it "wmm"
3. Download this repository
4. Edit `config.json` to use your application client_id instead of the default one
5. Run setup.bat
6. Run start.bat and wait

## ❌ How to stop?

⚠️ Make sure to stop the program using **Ctrl + C**.  
Closing the window directly may cause the Rich Presence to stay active until Discord is restarted.

## 📸 Screenshot


![ss](https://files.catbox.moe/dzia4z.png)

## ❗SECURITY DISCLAIMER (read carefully)

As far as I know, there are no well-known CVEs about WMM **2012** (the 2012 specifically since it's the only version that I haven't seen listed in public CVE databases)
That said, this does **not** guarantee that the software is free of vulnerabilities.

Windows Movie Maker is an old, discontinued application, so basic security precautions are strongly recommended.

### Recommended precautions

- Prevent the software from accessing the web (via a firewall rule)
- Make sure you only open trusted project files (not random ones) (as there might be vulnerabilities with specially crafted files that could execute arbitrary code on the local user's account)
- Run WMM as standard user (never admin)
- Enable Windows Exploit Protection for `moviemaker.exe`
  * DEP: On
  * ASLR: On
  * CFG: On (if available)
- Only open:
  * Your own footage
  * Files from trusted sources
- (Optional) use a virtual machine
