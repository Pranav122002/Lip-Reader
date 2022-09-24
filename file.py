import cv2
import os
import streamlit as st

st.write("""
#Lip Reader
# """)


def save_uploadedfile(uploadedfile):
    with open(os.path.join("tempDir", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())

    return st.success("Saved File:{} to tempDir".format(uploadedfile.name))


datafile = st.file_uploader("Upload file",type=[ 'mp4'])

if datafile is not None:
   file_details = {"FileName":datafile.name,"FileType":datafile.type}
   save_uploadedfile(datafile)