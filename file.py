import cv2
import streamlit as st

st.write("""
#Lip Reader
# """)
uploaded_video = st.file_uploader("upload a file")
# file = video_file.read()
st.video(uploaded_video) 



vidcap = cv2.VideoCapture(uploaded_video)

success,image = vidcap.read('out.mp4')
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
