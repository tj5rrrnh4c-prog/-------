import streamlit as st

# Настраиваем заголовок вкладки в браузере
st.set_page_config(page_title="Контроль поломок Колледжа", layout="centered")

# Красивый заголовок на странице
st.title("📱 Сообщить о поломке в колледже")
st.write("Заполните форму, и информация сразу будет передана ИИ и сотрудникам УПК.")

# 1. Поле для загрузки фото поломки
uploaded_file = st.file_uploader("Загрузите или сделайте фото поломки", type=["jpg", "jpeg", "png"])

# Если фото загружено, сразу показываем его на экране
if uploaded_file is not None:
    st.image(uploaded_file, caption="Выбранное фото поломки", use_container_width=True)

# 2. Текстовое поле для описания
description = st.text_area(
    label="Что именно сломалось?", 
    placeholder="Например: Испортилась дверь, сломалась ручка в 305 кабинете..."
)

# 3. Кнопка отправки заявки
if st.button("Отправить заявку", type="primary"):
    if not description and not uploaded_file:
        st.error("Пожалуйста, добавьте описание или фото поломки!")
    else:
        # Здесь будет связь с бэкендом твоего Тимлида
        st.success("🎉 Заявка успешно отправлена! ИИ уже обрабатывает запрос.")
        st.balloons() # Делаем красивую анимацию шариков при успехе
