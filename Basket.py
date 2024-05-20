import streamlit as st
import pandas as pd
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

# Функція для редагування статистики гравця
def edit_stats(player, points, rebounds, assists, steals, blocks, turnovers):
    df.loc[df['Гравець'] == player, 'Очки'] = points
    df.loc[df['Гравець'] == player, 'Підбирання'] = rebounds
    df.loc[df['Гравець'] == player, 'Асисти'] = assists
    df.loc[df['Гравець'] == player, 'Перехоплення'] = steals
    df.loc[df['Гравець'] == player, 'Блок-шоти'] = blocks
    df.loc[df['Гравець'] == player, 'Втрати'] = turnovers

if choice == 'Жива статистика':
    st.subheader('Жива статистика')
    st.write('Збір даних про гру в реальному часі.')

    # Вибір гравця для редагування
    player_choice = st.selectbox('Виберіть гравця для редагування', df['Гравець'])

    # Поточна статистика вибраного гравця
    player_data = df[df['Гравець'] == player_choice].iloc[0]
    points = st.number_input('Очки', value=player_data['Очки'])
    rebounds = st.number_input('Підбирання', value=player_data['Підбирання'])
    assists = st.number_input('Асисти', value=player_data['Асисти'])
    steals = st.number_input('Перехоплення', value=player_data['Перехоплення'])
    blocks = st.number_input('Блок-шоти', value=player_data['Блок-шоти'])
    turnovers = st.number_input('Втрати', value=player_data['Втрати'])

    if st.button('Зберегти зміни'):
        edit_stats(player_choice, points, rebounds, assists, steals, blocks, turnovers)
        st.success(f'Статистика для {player_choice} оновлена!')
    
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
    historical_data = {
        'Дата': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05'],
        'Гравець': ['Гравець 1', 'Гравець 2', 'Гравець 3', 'Гравець 4', 'Гравець 1'],
        'Очки': [20, 15, 10, 5, 22],
        'Підбирання': [5, 7, 3, 2, 6],
        'Асисти': [7, 5, 2, 1, 8],
        'Перехоплення': [2, 1, 3, 0, 2],
        'Блок-шоти': [1, 0, 2, 1, 1],
        'Втрати': [3, 2, 1, 4, 3]
    }
    historical_df = pd.DataFrame(historical_data)
    
    st.table(historical_df)

elif choice == 'Профілі гравців':
    st.subheader('Профілі гравців')
    st.write('Детальна інформація про кожного гравця, включаючи їхні досягнення та прогрес.')

    # Вибір гравця
    player_choice = st.selectbox('Виберіть гравця', df['Гравець'])

    # Відображення профілю гравця
    player_data = df[df['Гравець'] == player_choice]
    st.write(f"### {player_choice}")
    st.write(player_data)

    # Історичні дані для вибраного гравця
    player_history = historical_df[historical_df['Гравець'] == player_choice]
    st.write(f"Історія виступів {player_choice}:")
    st.table(player_history)
