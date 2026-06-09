
import streamlit as st

st.set_page_config(page_title="遺產分配計算器", layout="centered")

st.title("遺產分配計算器（台灣法規簡化版）")

st.write("此工具用於簡化計算法定繼承與應繼分（非法律意見）")

estate = st.number_input("遺產總額（NTD）", min_value=0, value=10000000, step=1000000)

spouse = st.checkbox("有配偶")

children = st.number_input("子女數量", min_value=0, value=0, step=1)

parents = st.number_input("父母數量", min_value=0, value=0, step=1)

siblings = st.number_input("兄弟姐妹數量", min_value=0, value=0, step=1)

level = []

if st.button("計算分配"):
    heirs = 0

    if spouse:
        heirs += 1
    heirs += children + parents + siblings

    if heirs == 0:
        st.error("沒有法定繼承人")
    else:
        share = estate / heirs

        st.success(f"每一位繼承人分得：約 {share:,.0f} NTD")

        st.write("分配結果：")
        if spouse:
            st.write(f"- 配偶：{share:,.0f} NTD")
        if children > 0:
            st.write(f"- 子女（每人）：{share:,.0f} NTD")
        if parents > 0:
            st.write(f"- 父母（每人）：{share:,.0f} NTD")
        if siblings > 0:
            st.write(f"- 兄弟姐妹（每人）：{share:,.0f} NTD")
