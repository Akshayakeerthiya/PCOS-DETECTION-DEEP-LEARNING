import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path
import base64


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="PCOS Detection",
    page_icon="🩺",
    layout="centered"
)


# ============================================================
# BACKGROUND IMAGE
# ============================================================

background_path = Path("background.png")

if background_path.exists():
    with open(background_path, "rb") as f:
        background_base64 = base64.b64encode(f.read()).decode()
else:
    background_base64 = ""


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ======================================================
       FULL PAGE BACKGROUND
       ====================================================== */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(255, 255, 255, 0.08),
                rgba(255, 255, 255, 0.08)
            ),
            url("data:image/png;base64,{background_base64}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}


    /* ======================================================
       PAGE WIDTH
       ====================================================== */

    .block-container {{
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}


    /* ======================================================
       MAIN HEADING
       ====================================================== */

    .main-title {{
        text-align: center;
        font-size: 46px;
        font-weight: 900;

        color: #43134F !important;

        margin-bottom: 5px;

        text-shadow:
            0 2px 6px rgba(255, 255, 255, 0.5);
    }}


    /* ======================================================
       SUB HEADING
       ====================================================== */

    .sub-title {{
        text-align: center;
        font-size: 19px;
        font-weight: 700;

        color: #5A315F !important;

        margin-bottom: 30px;

        text-shadow:
            0 1px 5px rgba(255, 255, 255, 0.4);
    }}


    /* ======================================================
       CONTAINER / FRAME
       ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.88) !important;

        border: 2px solid #C982C4 !important;

        border-radius: 20px !important;

        box-shadow:
            0 8px 25px rgba(70, 15, 80, 0.15);
    }}


    /* ======================================================
       ⭐ HEADING COLORS
       ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] h1,
    [data-testid="stVerticalBlockBorderWrapper"] h2,
    [data-testid="stVerticalBlockBorderWrapper"] h3,
    [data-testid="stVerticalBlockBorderWrapper"] h4,
    [data-testid="stVerticalBlockBorderWrapper"] h5,
    [data-testid="stVerticalBlockBorderWrapper"] h6 {{
        color: #4A174F !important;

        font-weight: 900 !important;
    }}


    /* ======================================================
       PROJECT OVERVIEW HEADING
       ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"]
    h3 {{
        color: #4A174F !important;
    }}


    /* ======================================================
       NORMAL TEXT INSIDE FRAMES
       ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] p {{
        color: #402C43 !important;

        font-size: 16px !important;

        line-height: 1.65 !important;
    }}


    /* ======================================================
       BOLD TEXT
       ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] strong {{
        color: #4A174F !important;

        font-weight: 900 !important;
    }}


    /* ======================================================
       LIST TEXT
       ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] li {{
        color: #402C43 !important;
    }}


    /* ======================================================
       ALL MARKDOWN HEADINGS
       ====================================================== */

    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4,
    [data-testid="stMarkdownContainer"] h5,
    [data-testid="stMarkdownContainer"] h6 {{
        color: #4A174F !important;

        font-weight: 900 !important;
    }}


    /* ======================================================
       ALL MARKDOWN NORMAL TEXT
       ====================================================== */

    [data-testid="stMarkdownContainer"] p {{
        color: #402C43 !important;
    }}


    [data-testid="stMarkdownContainer"] strong {{
        color: #4A174F !important;
    }}


    /* ======================================================
       UPLOAD TITLE
       ====================================================== */

    .section-title {{
        font-size: 23px;

        font-weight: 900;

        color: #43134F !important;

        margin-bottom: 12px;

        text-shadow:
            0 2px 6px rgba(255, 255, 255, 0.4);
    }}


    /* ======================================================
       FILE UPLOADER
       ====================================================== */

    [data-testid="stFileUploader"] {{
        background: rgba(255, 255, 255, 0.88) !important;

        border: 2px dashed #A94CA2 !important;

        border-radius: 20px;

        padding: 20px;

        box-shadow:
            0 8px 25px rgba(70, 15, 80, 0.12);
    }}


    [data-testid="stFileUploader"] label {{
        color: #402C43 !important;

        font-weight: 700 !important;
    }}


    [data-testid="stFileUploader"] section {{
        color: #402C43 !important;
    }}


    [data-testid="stFileUploader"] small {{
        color: #5A4260 !important;
    }}


    [data-testid="stFileUploader"] button {{
        color: #4A174F !important;
    }}


    /* ======================================================
       IMAGE
       ====================================================== */

    [data-testid="stImage"] {{
        border-radius: 14px;

        overflow: hidden;
    }}


    /* ======================================================
       METRIC LABEL
       ====================================================== */

    [data-testid="stMetricLabel"] {{
        color: #4A174F !important;

        font-weight: 800 !important;
    }}


    /* ======================================================
       CONFIDENCE VALUE
       ====================================================== */

    [data-testid="stMetricValue"] {{
        color: #7D2676 !important;

        font-weight: 900 !important;
    }}


    /* ======================================================
       CAPTION
       ====================================================== */

    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] * {{
        color: #5A4260 !important;
    }}


    /* ======================================================
       PROGRESS BAR
       ====================================================== */

    [data-testid="stProgressBar"] > div > div > div {{
        background-color: #A94CA2 !important;
    }}


    /* ======================================================
       PREDICTION ALERT
       ====================================================== */

    [data-testid="stAlert"] {{
        border-radius: 14px;
    }}


    [data-testid="stAlert"] p {{
        color: #4A174F !important;

        font-weight: 900 !important;
    }}


    /* ======================================================
       PCOS SUGGESTION BUTTON
       ====================================================== */

    div.stButton > button {{
        width: 100%;

        height: 52px;

        border-radius: 15px;

        background: linear-gradient(
            90deg,
            #6F1D75,
            #A9369D
        ) !important;

        color: white !important;

        font-size: 16px;

        font-weight: 800;

        border: 1px solid #C982C4 !important;

        box-shadow:
            0 7px 20px rgba(40, 5, 50, 0.25);
    }}


    div.stButton > button p {{
        color: white !important;
    }}


    div.stButton > button:hover {{
        background: linear-gradient(
            90deg,
            #58145F,
            #8F2D86
        ) !important;

        color: white !important;
    }}


    /* ======================================================
       SUGGESTION TEXT
       ====================================================== */

    .suggestion-content {{
        color: #402C43 !important;

        font-size: 16px;

        line-height: 1.7;
    }}


    .suggestion-content p {{
        color: #402C43 !important;
    }}


    .suggestion-content strong {{
        color: #4A174F !important;

        font-weight: 900 !important;
    }}


    /* ======================================================
       FOOTER
       ====================================================== */

    footer {{
        visibility: hidden;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MAIN HEADING
# ============================================================

st.markdown(
    '<div class="main-title">🩺 PCOS Detection</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'PCOS Detection from Ovarian Ultrasound Images'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

with st.container(border=True):

    st.subheader("Project Overview")

    st.write(
        "This application uses deep learning to analyze "
        "ovarian ultrasound images and classify them into "
        "PCOS and Non-PCOS categories using a trained "
        "ResNet50 model."
    )


# ============================================================
# UPLOAD SECTION
# ============================================================

st.markdown(
    '<div class="section-title">'
    '📤 Upload Ultrasound Image'
    '</div>',
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "Choose an ultrasound image",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return tf.keras.models.load_model(
        "pcos_resnet50_model.keras"
    )


model = load_model()


# ============================================================
# IMAGE UPLOADED
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")


    # ========================================================
    # UPLOADED IMAGE
    # ========================================================

    with st.container(border=True):

        st.subheader(
            "Uploaded Ultrasound Image"
        )

        st.image(
            image,
            use_container_width=True
        )


    # ========================================================
    # IMAGE PREPROCESSING
    # ========================================================

    resized_image = image.resize(
        (224, 224)
    )

    image_array = np.array(
        resized_image
    )

    image_array = image_array / 255.0

    image_array = np.expand_dims(
        image_array,
        axis=0
    )


    # ========================================================
    # MODEL PREDICTION
    # ========================================================

    prediction = model.predict(
        image_array,
        verbose=0
    )

    probability = float(
        prediction[0][0]
    )


    # ========================================================
    # CLASS MAPPING
    #
    # infected = 0
    # notinfected = 1
    # ========================================================

    if probability >= 0.5:

        result = "NON-PCOS"

        confidence = probability * 100

    else:

        result = "PCOS"

        confidence = (1 - probability) * 100


    # ========================================================
    # CONFIDENCE LEVEL
    # ========================================================

    if confidence >= 90:

        confidence_text = "HIGH CONFIDENCE"

    elif confidence >= 75:

        confidence_text = "GOOD CONFIDENCE"

    else:

        confidence_text = "LOW CONFIDENCE"


    # ========================================================
    # PREDICTION RESULT
    # ========================================================

    with st.container(border=True):

        st.subheader(
            "🔬 Prediction Result"
        )


        if result == "PCOS":

            st.error("PCOS")

        else:

            st.success("NON-PCOS")


        st.metric(
            label="Model Confidence",
            value=f"{confidence:.2f}%"
        )


        st.progress(
            min(confidence / 100, 1.0)
        )


        st.caption(
            confidence_text
        )


    # ========================================================
    # PCOS MANAGEMENT SUGGESTIONS
    # ========================================================

    if result == "PCOS":

        st.write("")

        show_suggestions = st.button(
            "💡 PCOS Management Suggestions"
        )


        if show_suggestions:

            with st.container(border=True):

                st.subheader(
                    "💡 PCOS Management Suggestions"
                )

                st.markdown(
                    """
                    <div class="suggestion-content">

                    <p>
                    <strong>
                    1. Consult a healthcare professional
                    </strong>
                    </p>

                    <p>
                    Seek proper evaluation and confirmation from
                    a qualified healthcare professional.
                    </p>


                    <p>
                    <strong>
                    2. Maintain regular physical activity
                    </strong>
                    </p>

                    <p>
                    Regular physical activity can support overall
                    health and metabolic well-being.
                    </p>


                    <p>
                    <strong>
                    3. Follow a balanced diet
                    </strong>
                    </p>

                    <p>
                    Include vegetables, fruits, whole grains and
                    protein-rich foods as part of a balanced diet.
                    </p>


                    <p>
                    <strong>
                    4. Maintain healthy lifestyle habits
                    </strong>
                    </p>

                    <p>
                    Adequate sleep and stress management can
                    support overall well-being.
                    </p>


                    <p>
                    <strong>
                    5. Follow medical advice
                    </strong>
                    </p>

                    <p>
                    Take prescribed medicines only according to
                    the advice of your healthcare professional.
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )
