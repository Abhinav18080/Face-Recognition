Things to do:
- Add adarsh's urls
- check if the website is open, if its not then open it else open the next url in the list thats not open
- make it so that this thing runs everytime you unlock the laptop


this is a code snipped for the second point from gemini: 
import subprocess

def is_website_open_mac(target_url):
    script = f'''
    tell application "Google Chrome"
        set windowList to windows
        repeat with aWindow in windowList
            set tabList to tabs of aWindow
            repeat with aTab in tabList
                if URL of aTab contains "{target_url}" then
                    return true
                end if
            end repeat
        end repeat
    end tell
    return false
    '''
    process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8').strip() == 'true'

# Example Usage:
target = "youtube.com"
if is_website_open_mac(target):
    print(f"The website {target} is open.")
else:
    print(f"The website {target} is not open.")
