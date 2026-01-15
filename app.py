import streamlit as st
import pandas as pd

st.title("Любими неща – класна анкета")

# --- ИНИЦИАЛИЗАЦИЯ НА ДАННИТЕ ---
if "colors" not in st.session_state:
    st.session_state.colors = {
        "Червен": 0,
        "Син": 0,
        "Зелен": 0,
        "Жълт": 0
    }

if "sports" not in st.session_state:
    st.session_state.sports = {
        "Футбол": 0,
        "Баскетбол": 0,
        "Волейбол": 0,
        "Плуване": 0
    }

if "classes" not in st.session_state:
    st.session_state.classes = {
        "5 клас": 0,
        "6 клас": 0,
        "7 клас": 0
    }

if "grades" not in st.session_state:
    st.session_state.grades = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }

# --- ИЗБОР ---
st.subheader("Попълни анкетата")

selected_class = st.selectbox("Клас:", list(st.session_state.classes.keys()))
color = st.selectbox("Любим цвят:", list(st.session_state.colors.keys()))
sport = st.selectbox("Любим спорт:", list(st.session_state.sports.keys()))
grade = st.selectbox("Оценка:", list(st.session_state.grades.keys()))

if st.button("Запази избора"):
    st.session_state.classes[selected_class] += 1
    st.session_state.colors[color] += 1
    st.session_state.sports[sport] += 1
    st.session_state.grades[grade] += 1
    st.success("Изборът е записан успешно!")

st.divider()

# --- РЕЗУЛТАТИ ---
st.subheader("Резултати")

st.write("📘 По класове")
classes_df = pd.DataFrame.from_dict(
    st.session_state.classes, orient="index", columns=["Брой"]
)
st.bar_chart(classes_df)

st.write("🎨 Любими цветове")
colors_df = pd.DataFrame.from_dict(
    st.session_state.colors, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)

st.write("⚽ Любими спортове")
sports_df = pd.DataFrame.from_dict(
    st.session_state.sports, orient="index", columns=["Брой"]
)
st.bar_chart(sports_df)

st.write("📝 Оценки")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(grades_df)
