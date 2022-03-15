import tkinter as tk
import cv2

MEDIA_RAW = cv2.VideoCapture("Media/VideoDemo.mp4")


def continue_video():
    print("Go next?")

box_list = [(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)]

window = tk.Tk()
window.title("Labelling")
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=70, weight=1)
window.resizable(False, False)

fr_checks = tk.Frame(window)
fr_btn = tk.Frame(window)

check_list = []
check_var_list = []

for x in range(len(box_list)):

    check_var_list.append(tk.IntVar())

    check_list.append(tk.Checkbutton(fr_checks, text = "Person " + str(x), variable = check_var_list[x], onvalue = 1, offvalue = 0, height = 2, width = 10))

    check_list[x].grid(row=x , column=0 , sticky="ew" , padx=5 , pady=5)

btn_ok = tk.Button(fr_btn, text="OK", command=continue_video)

fr_checks.grid(row=0, column=0, sticky="ns")
fr_btn.grid(row=1, column=0, sticky="ns")
btn_ok.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

while cv2.waitKey(1) < 0:

    #Grab the frame from the threaded video stream
    hasFrame, image = MEDIA_RAW.read()

    if not hasFrame:
        cv2.waitKey()
        cv2.destroyAllWindows()
        break

    cv2.imshow("VIDEO_LOC" , image)

    window.mainloop()

MEDIA_RAW.release()

#Close all windows
cv2.destroyAllWindows()