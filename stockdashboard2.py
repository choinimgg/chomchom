import streamlit as st
import FinanceDataReader as fdr
import plotly.graph_objects as go

# Streamlit 앱의 제목 설정
st.title("날짜별 주식가격 캔들차트")

#날짜와 종목명 입력 받기
start_date = st.date_input("시작 날짜")
end_date = st.date_input("종료 날짜")
stock_code = st.text_input("종목 코드")

# FinanceDataReader를 사용하여 주식 데이터 가져오기
df = fdr.DataReader(stock_code, start_date, end_date)

# 그래프 그리기
fig = go.Figure(data=go.Candlestick(x=df.index,
                                   open=df['Open'],
                                   high=df['High'],
                                   low=df['Low'],
                                   close=df['Close']))

# 그래프 설정
fig.update_layout(title=f'{stock_code} 주식 가격',
                  yaxis_title='주식 가격',
                  xaxis_rangeslider_visible=False)

# 그래프 출력
st.plotly_chart(fig)
