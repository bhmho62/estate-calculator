import streamlit as st

st.title("NTD 遺產分配計算器")

st.write("輸入 X, Y, Z, W（預設 W = 15,000,000）")

# =========================
# Inputs
# =========================
X = st.number_input("X 金額", value=0.0)
Y = st.number_input("Y 金額", value=0.0)
Z = st.number_input("Z 金額", value=0.0)
W = st.number_input("W 金額", value=15000000.0)

total = X + Y + Z + W
A = X + Y  # 用於 X+Y 的分配

st.subheader("選擇分配方案")
mode = st.radio(
    "方案",
    [
        "方案 1（女生10% / 男生70%）",
        "方案 2（女生20% + Z六等分 + W分配）"
    ]
)

st.write(f"總金額：{total:,.0f} NTD")

# =========================
# 方案 1
# =========================
if mode == "方案 1（女生10% / 男生70%）":

    girl = 0.10 * total
    boy = (0.70 * total) / 2

    st.subheader("結果")

    st.write("👩 每個女生：")
    st.success(f"{girl:,.0f} NTD")

    st.write("👨 每個男生：")
    st.success(f"{boy:,.0f} NTD")

# =========================
# 方案 2
# =========================
else:

    # X + Y：女生20%
    girl_xy = 0.20 * (X + Y)

    # Z：六等分
    girl_z = Z / 6
    boy1_z = (2 * Z) / 6
    boy2_z = Z / 6

    # W：男1 2/3, 男2 1/3
    boy1_w = (2/3) * W
    boy2_w = (1/3) * W

    # 最終合計
    girl = girl_xy + girl_z

    boy1 = girl_xy + boy1_z + boy1_w
    boy2 = girl_xy + boy2_z + boy2_w

    st.subheader("結果")

    st.write("👩 每個女生：")
    st.success(f"{girl:,.0f} NTD")

    st.write("👨 男1：")
    st.success(f"{boy1:,.0f} NTD")

    st.write("👨 男2：")
    st.success(f"{boy2:,.0f} NTD")

# =========================
# Breakdown
# =========================
st.divider()
st.subheader("拆解")

st.write(f"X + Y = {X + Y:,.0f}")
st.write(f"Z = {Z:,.0f}")
st.write(f"W = {W:,.0f}")
