import av
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_webrtc import (
    WebRtcMode,
    webrtc_streamer,
    RTCConfiguration,
)
from src.face_rec import Face_recognition

face_recognition = Face_recognition
# from tensorflow.keras.models import load_model

# from sources.config import (
#     IMAGE_EXAMPLE,
#     IMAGE_TYPES,
#     MODEL_CONFIG,
#     MODEL_FACE_DETECTOR,
#     MODEL_MASK_DETECTOR,
#     RTC_CONFIGURATION,
# )
# from sources.detect_mask_image import detect_mask_in_image

# Setting custom Page Title and Icon with changed layout and sidebar state
st.set_page_config(
    page_title="Face Mask Detector",
    page_icon="😷",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load models
# prototxtPath = MODEL_CONFIG
# weightsPath = MODEL_FACE_DETECTOR
# faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
# maskNet = load_model(MODEL_MASK_DETECTOR)
# example_image = IMAGE_EXAMPLE
# print("[INFO] loaded face mask detector model")


class VideoProcessor:
    def recv(self, frame):
        image = frame.to_ndarray(format="bgr24")
        image = face_recognition.recogny_face(image)
        return av.VideoFrame.from_ndarray(image, format="bgr24")


def local_css(file_name):
    # Method for reading styles.css and applying necessary changes to HTML
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def choose_webcam():
    st.sidebar.markdown('Click "START" to connect this app to a server')
    st.sidebar.markdown("It may take a minute, please wait...")
    webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
    )


def main():
    local_css("styles.css")
    st.markdown(
        '<h6 align="center">TT HACKATHON - Feb 2022</h6>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h1 align="center">😷 Face Mask Detection</h1>',
        unsafe_allow_html=True,
    )
    st.set_option("deprecation.showfileUploaderEncoding", False)
    choice = st.sidebar.radio(
        "Select an input option:",
        ["Image", "Webcam"],
    )
    # if choice == "Image":
    #     choose_image()

    if choice == "Webcam":
        choose_webcam()


if __name__ == "__main__":
    main()
