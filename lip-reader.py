import cv2
import os
import streamlit as st


st.title("Lip Reader")


def save_uploaded_file(uploadedfile):
    with open(os.path.join("videos", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved file : {} in videos folder ...".format(uploadedfile.name))


uploaded_video = st.file_uploader("Upload video",type=['mp4', 'mkv'])

if uploaded_video is not None:
    file_details = {"FileName":uploaded_video.name,"FileType":uploaded_video.type,"FileSize":uploaded_video.size}
    save_uploaded_file(uploaded_video)


vidcap = cv2.VideoCapture('videos/{}'.format(uploaded_video.name))
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames/frame%d.jpg" % count, image)           
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1