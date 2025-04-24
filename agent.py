import subprocess
import webbrowser

redirect_url = "https://www.pornhub.com"
script = '''
try
    do shell script "echo Authenticated!" with administrator privileges
    return "authenthicated"
on error errMsg number errNum
    return "failed"
end try
'''
try:
    result = subprocess.check_output(["osascript", "-e", script], text = True).strip()
    if result == "authenticated":
        print("✅ macOS authentication succesful")
        subprocess.run(["afplay", "Sound effect.mp3"])
        subprocess.run(['osascript',"-e", 'set volume output volume 100'])
        webbrowser.open(redirect_url)
    elif result == "failed":
        print("❌ macOS authentication failed.")
        subprocess.run(["afplay", "Sound effect.mp3"])
        subprocess.run(['osascript',"-e", 'set volume output volume 100'])
        webbrowser.open(redirect_url)
except subprocess.CalledProcessError:
    print("❌ macOS authentication failed.")
    subprocess.run(["afplay", "Sound effect.mp3"])
    subprocess.run(['osascript',"-e", 'set volume output volume 100'])
    webbrowser.open(redirect_url)
