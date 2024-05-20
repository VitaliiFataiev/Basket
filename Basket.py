import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Заголовок програми
st.title('Система Ведення Статистики Матчів Баскетболу')

# Меню навігації
menu = ['Жива статистика', 'Інтерактивна аналітика', 'Історичні дані', 'Профілі гравців']
choice = st.sidebar.selectbox('Меню', menu)

# Дані для прикладу
data = {
    'Гравець': ['Гравець 1', 'Гравець 2', 'Гравець 3', 'Гравець 4'],
    'Очки': [20, 15, 10, 5],
    'Підбирання': [5, 7, 3, 2],
    'Асисти': [7, 5, 2, 1],
    'Перехоплення': [2, 1, 3, 0],
    'Блок-шоти': [1, 0, 2, 1],
    'Втрати': [3, 2, 1, 4]
}
df = pd.DataFrame(data)

if choice == 'Жива статистика':
    st.subheader('Жива статистика')
    st.write('Збір даних про гру в реальному часі.')
    # Відображення таблиці статистики
    st.table(df)

elif choice == 'Інтерактивна аналітика':
    st.subheader('Інтерактивна аналітика')
    st.write('Візуалізація даних у вигляді графіків та діаграм.')

    # Вибір типу графіку
    chart_type = st.selectbox('Тип графіку', ['Bar Chart', 'Line Chart', 'Scatter Plot'])

    if chart_type == 'Bar Chart':
        bar_chart = alt.Chart(df).mark_bar().encode(
            x='Гравець',
            y='Очки'
        )
        st.altair_chart(bar_chart, use_container_width=True)
    elif chart_type == 'Line Chart':
        line_chart = alt.Chart(df).mark_line().encode(
            x='Гравець',
            y='Очки'
        )
        st.altair_chart(line_chart, use_container_width=True)
    elif chart_type == 'Scatter Plot':
        scatter_plot = alt.Chart(df).mark_circle(size=100).encode(
            x='Підбирання',
            y='Асисти',
            color='Гравець',
            tooltip=['Гравець', 'Очки', 'Підбирання', 'Асисти', 'Перехоплення', 'Блок-шоти', 'Втрати']
        ).interactive()
        st.altair_chart(scatter_plot, use_container_width=True)

elif choice == 'Історичні дані':
    st.subheader('Історичні дані')
    st.write('Збереження та аналіз статистики за попередні сезони.')
    # Зараз це демонстраційні дані, тут ви можете додати можливість завантаження даних або інших способів отримання історичних даних.
    st.table(df)

elif choice == 'Профілі гравців':
    st.subheader('Профілі гравців')
    st.write('Детальна інформація про кожного гравця, включаючи їхні досягнення та прогрес.')

    # Вибір гравця
    player_choice = st.selectbox('Виберіть гравця', df['Гравець'])

    # Відображення профілю гравця
    player_data = df[df['Гравець'] == player_choice]
    st.write(f"### {player_choice}")
    st.write(player_data)

