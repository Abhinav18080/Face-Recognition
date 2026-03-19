import face_recognition
import cv2
import numpy as np
import webbrowser
import time
import subprocess

def is_website_open(target_url):
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

    process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, vendathesadhanam = process.communicate()
    return stdout.decode('utf-8').strip() == 'true'

video_capture = cv2.VideoCapture(0)

abhi_image = face_recognition.load_image_file("abhi.jpeg")
abhi_face_encoding = face_recognition.face_encodings(abhi_image)[0]

adarsh_image = face_recognition.load_image_file("adarsh.jpeg")
adarsh_face_encoding = face_recognition.face_encodings(adarsh_image)[0]

known_face_encoding = [
    abhi_face_encoding,
    adarsh_face_encoding
]

known_face_names = [
    "Abhinav Manosh Pillai",
    "Adarsh Manosh Pillai"
]

#variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
opentabscondition = True
chrome_path = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome')

while True:
    ret, frame = video_capture.read()

    if not ret or frame is None:
        print("Failed to grab frame from camera. Exiting...")
        break

    if process_this_frame:
        small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)

        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name= known_face_names[best_match_index]
                if opentabscondition and name == "Abhinav Manosh Pillai":          
                    print("This is Abhinav. Going to open tabs now")   
                    urls = [
                        'https://www.atptour.com/en',
                        'https://www.amazon.com',
                        'https://www.thalappakatti.us/'
                    ]

                    for url in urls:
                        if is_website_open(url) == False:
                            subprocess.Popen(['open', '-a', 'Google Chrome', url])
                            time.sleep(0.5)
                            print("url: "+ url)
                        else:
                            print(url + " is already open")

                    opentabscondition = False
                elif opentabscondition and name == "Adarsh Manosh Pillai":
                    print("This is Adarsh. Going to open tabs now")   
                    urls = [
                        'https://docs.python.org/3/library/webbrowser.html',
                        'https://www.amazon.com',
                        'https://www.thalappakatti.us/'
                    ]

                    for url in urls:
                        if is_website_open(url) == False:
                            subprocess.Popen(['open', '-a', 'Google Chrome', url])
                            time.sleep(0.5)
                            print("url: "+ url)
                        else:
                            print(url + " is already open")

                    opentabscondition = False
            else:    
                print("Error. Dont know who you are")

            face_names.append(name)
        
    process_this_frame = not process_this_frame

    for(top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)

        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0,0,255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom -6), font, 1.0, (255, 255, 255), 1)
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or opentabscondition == False:
        print("Tabs opened. Exiting now.....")
        break

video_capture.release()
cv2.destroyAllWindows