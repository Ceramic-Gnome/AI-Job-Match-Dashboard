import streamlit as st


def skill_badge(skill, matched=True):
    if matched:
        color = "#2E8B57"
        icon = "✅"
    else:
        color = "#C0392B"
        icon = "❌"

    st.markdown(
        f"""
        <span style="
            display:inline-block;
            background-color:{color};
            color:white;
            padding:4px 10px;
            margin:3px;
            border-radius:12px;
            font-size:0.85rem;
        ">
        {icon} {skill}
        </span>
        """,
        unsafe_allow_html=True,
    )
