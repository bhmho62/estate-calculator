import streamlit as st

st.set_page_config(
    page_title="NTD 遺產分配計算器",
    page_icon="💰",
    layout="centered"
)

st.title("💰 NTD 遺產分配計算器")

st.write("請輸入各項資產金額")

# =========================
# Inputs
# =========================

二聖 = st.number_input(
    "二聖 金額",
    min_value=0.0,
    value=0.0,
    step=100000.0
)

股票 = st.number_input(
    "股票 金額",
    min_value=0.0,
    value=0.0,
    step=100000.0
)

現金 = st.number_input(
    "現金 金額",
    min_value=0.0,
    value=0.0,
    step=100000.0
)

永樂街 = st.number_input(
    "永樂街 金額",
    min_value=0.0,
    value=15000000.0,
    step=100000.0
)

total = 二聖 + 股票 + 現金 + 永樂街

st.divider()

# =========================
# Mode Selection
# =========================

mode = st.radio(
    "選擇分配方案",
    (
        "方案 1（女生10%，男生各35%）",
        "方案 2（自訂分配）"
    )
)

st.write(f"### 總資產：{total:,.0f} NTD")

# =========================
# Plan 1
# =========================

if mode == "方案 1（女生10%，男生各35%）":

    girl = total * 0.10
    boy = total * 0.35

    st.subheader("分配結果")

    st.write("👩 每位女生")
    st.success(f"{girl:,.0f} NTD")

    st.write("👨 每位男生")
    st.success(f"{boy:,.0f} NTD")

# =========================
# Plan 2
# =========================

else:

    # 二聖 + 股票
    common_share = 0.20 * (二聖 + 股票)

    # 現金
    girl_cash = 現金 / 6
    boy1_cash = (2 * 現金) / 6
    boy2_cash = 現金 / 6

    # 永樂街
    boy1_house = (2 / 3) * 永樂街
    boy2_house = (1 / 3) * 永樂街

    # Total
    girl = common_share + girl_cash

    boy1 = common_share + boy1_cash + boy1_house
    boy2 = common_share + boy2_cash + boy2_house

    st.subheader("分配結果")

    st.write("👩 女1")
    st.success(f"{girl:,.0f} NTD")

    st.write("👩 女2")
    st.success(f"{girl:,.0f} NTD")

    st.write("👩 女3")
    st.success(f"{girl:,.0f} NTD")

    st.write("👨 男1")
    st.success(f"{boy1:,.0f} NTD")

    st.write("👨 男2")
    st.success(f"{boy2:,.0f} NTD")

    distributed_total = (
        girl * 3 +
        boy1 +
        boy2
    )

    st.divider()

    st.write("### 驗算")

    st.write(f"分配總額：{distributed_total:,.0f} NTD")
    st.write(f"資產總額：{total:,.0f} NTD")

    difference = total - distributed_total

    if abs(difference) < 1:
        st.success("✅ 分配總額與資產總額一致")
    else:
        st.error(f"❌ 差額：{difference:,.0f} NTD")

# =========================
# Asset Breakdown
# =========================

st.divider()

st.subheader("資產明細")

st.write(f"二聖：{二聖:,.0f} NTD")
st.write(f"股票：{股票:,.0f} NTD")
st.write(f"現金：{現金:,.0f} NTD")
st.write(f"永樂街：{永樂街:,.0f} NTD")
st.write(f"總資產：{total:,.0f} NTD")
