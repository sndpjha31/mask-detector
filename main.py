import tkinter
from tkinter.filedialog import askopenfilename
import os

pythonEnv = 'C:/Users/jhasn/anaconda3/envs/face_mask_env/python.exe'
dirPath = os.getcwd().replace('\\', '/')


def createModel():
    if os.path.exists(dirPath+"/face_mask_detector.model"):
        print("Model already Exists")
    else:
        os.system(f'cmd /k "{pythonEnv} {dirPath}/train_mask_detector.py --dataset dataset"')


def pickImage():
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    os.system(f'cmd /k "{pythonEnv} {dirPath}/detect_mask_fromImage.py --image {filename}"')


def detectStream():
    window.destroy()
    os.system(f'cmd /k "{pythonEnv} {dirPath}/detect_mask_fromVideo.py"')


window = tkinter.Tk()


RunModelButton = tkinter.Button(window, text='Create Model', command=createModel)
RunModelButton.pack()

DetectImageButton = tkinter.Button(window, text="Detect from Image", command=pickImage)
DetectImageButton.pack()

DetectVideoButton = tkinter.Button(window, text='Detect from Web-Cam', command=detectStream)
DetectVideoButton.pack()


window.mainloop()