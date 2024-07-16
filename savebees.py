import streamlit as st

# 언어 선택 기능
if 'language' not in st.session_state:
    st.session_state.language = 'Korean'

# 언어 변경 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("한국어"):
        st.session_state.language = 'Korean'
with col2:
    if st.button("English"):
        st.session_state.language = 'English'

# CSS 스타일 적용
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap');
        body {{
            background-color: #f5f5dc;
            font-family: 'Nanum Gothic', sans-serif;
            color: #ffd700;  /* 진한 개나리 노랑색 */
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2em;
            margin: 0 auto;
            width: 90%;
            max-width: 1200px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }}
        .content {{
            width: 100%;
            border-radius: 10px;
            padding: 2em;
            text-align: left;
            background-color: rgba(255, 255, 255, 0.3);
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .stButton button {{
            margin: 10px 0;
            width: 100%;
            border-radius: 10px;
            border: 1px solid #ffd700;  /* 진한 개나리 노랑색 */
            padding: 15px 30px;
            color: #ffd700;  /* 진한 개나리 노랑색 */
            background-color: #ffffff;
            font-size: 1.2em;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
        }}
        .stButton button:hover {{
            background-color: #ffd700;  /* 진한 개나리 노랑색 */
            color: #ffffff;
            cursor: pointer;
        }}
        h1 {{
            color: #ffd700;  /* 진한 개나리 노랑색 */
            text-align: center;
            font-weight: 700;
            margin-bottom: 0.5em;
        }}
        .header {{
            font-size: 2em;
            font-weight: bold;
            color: #ffd700;  /* 진한 개나리 노랑색 */
            text-align: center;
            margin-bottom: 1em;
        }}
        .section {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            font-size: 1.2em;
            color: #333333;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            animation: fadeIn 0.5s ease-in-out;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        .center {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 1em; /* Add margin if needed */
        }}
    </style>
""", unsafe_allow_html=True)

# 메인 화면 제목 및 내용
if st.session_state.language == 'Korean':
    st.title("꿀벌: 자연의 작은 영웅을 보호하자")

    st.write("""
        꿀벌은 우리 생태계와 농업에 없어서는 안 될 중요한 역할을 합니다. 그러나 최근 몇 년 동안 꿀벌의 개체 수가 급격히 감소하고 있어 큰 우려를 낳고 있습니다. 이 웹사이트에서는 꿀벌의 중요성, 꿀벌 감소의 원인, 꿀벌 보호를 위한 노력을 다룹니다.
    """)

    summaries = {
        "꿀벌 개체수 감소의 이유": """
            최근 몇 년 동안 꿀벌의 개체 수가 급격히 감소하고 있습니다. 그 이유는 농업에 사용되는 살충제, 서식지 파괴, 기후 변화 등 다양합니다. 네오니코티노이드 계열의 살충제는 꿀벌의 신경계를 교란시키며, 도시화와 농업 확대로 인해 꿀벌이 살고 먹이를 찾을 수 있는 장소가 줄어들고 있습니다. 또한, 기후 변화로 인해 꿀벌이 먹이로 삼는 꽃의 개화 시기가 변화하고, 이상 기후 현상으로 인해 꿀벌의 생존 환경이 악화되고 있습니다.
        """,
        "꿀벌 복원을 위한 노력": """
            꿀벌을 보호하고 복원하기 위한 다양한 노력이 전 세계적으로 이루어지고 있습니다. 살충제 사용을 규제하는 법안들이 도입되고 있으며, 많은 단체들이 꿀벌이 좋아하는 야생 꽃을 심고 서식지를 조성하고 있습니다. 또한, 도시 지역에서도 꿀벌을 위한 녹지를 확대하려는 시도가 이루어지고 있습니다. 이러한 노력들은 꿀벌뿐만 아니라 전체 생태계에 긍정적인 영향을 미치고 있습니다.
        """,
        "개인이 할 수 있는 일": """
            개인적으로도 꿀벌 보호에 기여할 수 있는 방법이 많습니다. 예를 들어, 집 주변에 꿀벌이 좋아하는 꽃을 심거나 살충제 사용을 줄이는 것이 큰 도움이 됩니다. 또한, 지역 농부들이 꿀벌 친화적인 농업을 할 수 있도록 지지하고, 꿀벌 보호 단체에 기부하는 것도 좋은 방법입니다. 꿀벌을 보호하는 것은 결국 우리의 식량 안보를 지키는 일과 직결됩니다.
        """
    }
else:
    st.title("Bees: Protecting Nature's Small Heroes")

    st.write("""
        Bees play an indispensable role in our ecosystem and agriculture. However, in recent years, the number of bees has been rapidly declining, causing great concern. This website covers the importance of bees, the reasons for their decline, and efforts to protect them.
    """)

    summaries = {
        "Reasons for the Decline in Bee Population": """
            In recent years, the number of bees has been rapidly declining. The reasons are varied, including pesticides used in agriculture, habitat destruction, and climate change. Neonicotinoid pesticides disrupt the nervous systems of bees, while urbanization and agricultural expansion have reduced the places where bees can live and find food. Additionally, climate change has altered the blooming periods of flowers that bees feed on, and extreme weather events have worsened the bees' survival environment.
        """,
        "Efforts to Restore Bees": """
            Various efforts are being made worldwide to protect and restore bees. Legislation regulating pesticide use is being introduced, and many organizations are planting wildflowers that bees love and creating habitats. Efforts are also being made to expand green spaces for bees in urban areas. These efforts have a positive impact on the entire ecosystem, not just bees.
        """,
        "What Individuals Can Do": """
            There are many ways individuals can contribute to bee conservation. For example, planting flowers that bees love around your home or reducing pesticide use can be very helpful. Supporting local farmers in adopting bee-friendly agricultural practices and donating to bee conservation organizations are also great ways to help. Protecting bees ultimately safeguards our food security.
        """
    }

# 요약 내용 버튼
if st.button("꿀벌 개체수 감소의 이유" if st.session_state.language == 'Korean' else "Reasons for the Decline in Bee Population"):
    st.write(summaries["꿀벌 개체수 감소의 이유" if st.session_state.language == 'Korean' else "Reasons for the Decline in Bee Population"])

if st.button("꿀벌 복원을 위한 노력" if st.session_state.language == 'Korean' else "Efforts to Restore Bees"):
    st.write(summaries["꿀벌 복원을 위한 노력" if st.session_state.language == 'Korean' else "Efforts to Restore Bees"])

if st.button("개인이 할 수 있는 일" if st.session_state.language == 'Korean' else "What Individuals Can Do"):
    st.write(summaries["개인이 할 수 있는 일" if st.session_state.language == 'Korean' else "What Individuals Can Do"])
