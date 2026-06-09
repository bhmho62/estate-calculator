import streamlit as st

st.title("NTD 遺產分配計算器")

st.write("輸入 X, Y, Z, W（預設 W = 15,000,000）")

# Inputs
X = st.number_input("X 金額", value=0.0)
Y = st.number_input("Y 金額", value=0.0)
Z = st.number_input("Z 金額", value=0.0)
W = st.number_input("W 金額", value=15000000.0)

total = X + Y + Z + W
A = X + Y + Z

st.subheader("選擇分配方案")
mode = st.radio(
    "方案",
    ["方案 1（女生10% / 男生70%）", "方案 2（女生20% of XYZ + W給男生）"]
)

st.write(f"總金額：{total:,.0f} NTD")

# =========================
# 方案 1
# =========================
if mode == "方案 1（女生10% / 男生70%）":

    girl = 0.10 * total
    boy = 0.70 * total / 2

    st.subheader("結果")

    st.write("👩 每個女生：")
    st.success(f"{girl:,.0f} NTD")

    st.write("👨 每個男生：")
    st.success(f"{boy:,.0f} NTD")

# =========================
# 方案 2
# =========================
else:

    girl = 0.20 * A
    boy = (0.40 * A + W) / 2

    st.subheader("結果")

    st.write("👩 每個女生（只算 X+Y+Z）：")
    st.success(f"{girl:,.0f} NTD")

    st.write("👨 每個男生（含 W 分配）：")
    st.success(f"{boy:,.0f} NTD")

# =========================
# Breakdown
# =========================
st.divider()
st.subheader("拆解")

st.write(f"X+Y+Z = {A:,.0f}")
st.write(f"W = {W:,.0f}")
