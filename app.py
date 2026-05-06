import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="NICU Neonatal Calculator",
    page_icon="🩺",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("NICU Neo Calc")

st.markdown(
    "<a id='dr-EL-Okta184'></a>",
    unsafe_allow_html=True
)

st.markdown("---")

# =========================================
# INPUT
# =========================================

st.header("Input")

col1, col2 = st.columns(2)

with col1:

    bb = st.number_input(
        "Berat badan (kg)",
        0.5,
        10.0,
        3.0
    )

    usia = st.number_input(
        "Usia neonatus (hari)",
        1,
        30,
        1
    )

    jenis = st.selectbox(
        "Jenis neonatus",
        ["Term", "Prematur"]
    )

    dextrose = st.selectbox(
        "Dextrose",
        [5, 10, 12.5, 15]
    )

with col2:

    protein = st.number_input(
        "Protein (g/kgBB/hari)",
        1.0,
        4.0,
        1.5
    )

    kcl_target = st.number_input(
        "Maintenance KCl (mEq/kgBB)",
        1.0,
        3.0,
        2.0
    )

    ca_target = st.number_input(
        "Ca Gluconas (cc/kgBB)",
        0.5,
        1.0,
        0.5
    )

    delta_na = st.number_input(
        "Delta Na",
        0.0,
        20.0,
        10.0
    )

    delta_k = st.number_input(
        "Delta K",
        0.0,
        5.0,
        1.0
    )
# =========================================
# AUTO FLUID
# =========================================

if jenis == "Term":

    if usia == 1:
        cairan = 80

    elif usia == 2:
        cairan = 100

    elif usia == 3:
        cairan = 120

    elif usia == 4:
        cairan = 140

    else:
        cairan = 160

else:

    if usia == 1:
        cairan = 100

    elif usia == 2:
        cairan = 120

    elif usia == 3:
        cairan = 140

    elif usia == 4:
        cairan = 160

    else:
        cairan = 180

# =========================================
# MAIN CALCULATION
# =========================================

total_cairan = bb * cairan

ml_jam = total_cairan / 24

microdrip = ml_jam

# GIR

gir = (dextrose * ml_jam * 0.167) / bb

# Aminosteril

protein_total = protein * bb

aminosteril = protein_total / 0.06

# KCl

kcl = kcl_target * bb

# Ca gluconas

ca = ca_target * bb

# Sisa cairan

sisa = total_cairan - (
    aminosteril +
    kcl +
    ca
)

sisa_jam = sisa / 24

# Hiponatremia

na_deficit = delta_na * bb * 0.6

nacl3 = na_deficit / 0.5

# Hipokalemia

delta_k = 1

koreksi_k = delta_k * 0.4 * bb

# Hipoglikemia

d10 = 2 * bb

# Resusitasi

resus = 10 * bb

# =========================================
# OUTPUT
# =========================================

st.markdown("---")

st.header("Maintenance")

st.info(
    f"Kebutuhan cairan: {cairan} mL/kgBB/hari"
)

col3, col4, col5 = st.columns(3)

with col3:

    st.metric(
        "Total Cairan",
        f"{total_cairan:.1f} mL/hari"
    )

    st.metric(
        "Kecepatan Infus",
        f"{ml_jam:.1f} mL/jam"
    )

with col4:

    st.metric(
        "Microdrip",
        f"{microdrip:.1f} tetes/menit"
    )

    st.metric(
        "GIR",
        f"{gir:.2f} mg/kg/min"
    )

    st.metric(
        "Aminosteril 6%",
        f"{aminosteril:.1f} mL"
    )

with col5:

    st.metric(
        "Maintenance KCl",
        f"{kcl:.1f} mL"
    )

    st.metric(
        "Ca Gluconas",
        f"{ca:.1f} mL"
    )

st.success(
    f"Sisa cairan maintenance: {sisa:.1f} mL/hari"
)

st.info(
    f"Sisa cairan per jam: {sisa_jam:.1f} mL/jam"
)

# =========================================
# GIR WARNING
# =========================================

if gir < 4:
    st.warning("GIR rendah")

elif gir > 12:
    st.error("GIR terlalu tinggi")

else:
    st.success("GIR normal")

# =========================================
# HYPONATREMIA
# =========================================

st.markdown("---")

st.header("Koreksi Hiponatremia")

col6, col7 = st.columns(2)

with col6:

    st.metric(
        "Defisit Natrium",
        f"{na_deficit:.1f} mEq"
    )

with col7:

    st.metric(
        "NaCl 3%",
        f"{nacl3:.1f} mL"
    )

# =========================================
# HYPOKALEMIA
# =========================================

st.markdown("---")

st.header("Koreksi Hipokalemia")

st.metric(
    "Kebutuhan KCl",
    f"{koreksi_k:.2f} mL"
)

# =========================================
# HYPOGLYCEMIA
# =========================================

st.markdown("---")

st.header("Koreksi Hipoglikemia")

st.metric(
    "Bolus D10%",
    f"{d10:.1f} mL"
)

# =========================================
# RESUSITATION
# =========================================

st.markdown("---")

st.header("Resusitasi Cairan")

st.metric(
    "NaCl 0,9% / RL",
    f"{resus:.1f} mL"
)

# =========================================
# TRANSFUSION
# =========================================

st.markdown("---")

st.header("Transfusi")

transfusion = st.selectbox(
    "Jenis Transfusi",
    ["PRC", "FFP", "TC"]
)

dose = st.slider(
    "Dosis mL/kgBB",
    10,
    15,
    15
)

transfusion_volume = dose * bb

st.metric(
    f"Volume {transfusion}",
    f"{transfusion_volume:.1f} mL"
)

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.caption("NICU Neo Calc")
st.caption("Developed by dr. EL.Okta.184")