import streamlit as st #스트림릿
from PIL import Image # 사진불러오기
st.write('# 컴퓨터 부품 선택') # 큰 글씨

st.write('원하는 사양의 컴퓨터 부품 선택을 도와드립니다') # 작은 글씨

doing = st.radio( #3가지 용도중 선택
    "어떠한 용도로 사용하시나요?",
    ('게이밍', '영상편집','웹서핑'))

if doing == '게이밍': # 게이밍을 고른경우 cpu gpu 선택
    st.write('게이밍은 높은 사양의 그래픽 성능을 요구합니다.')
    image = Image.open('gpu.jpg')
    st.image(image, caption='gpu.jpg')
    
    
    
elif doing == '영상편집': #영상편집을 고른경우 cpu gpu 선택
    st.write("영상편집은 cpu의 연산성능이 중요합니다.")
    image = Image.open('edit.jpg')
    st.image(image, caption='edit.jpg')
  
    
elif doing == '웹서핑': # 웹서핑을 고른경우 cpu 선택
    st.write("웹서핑은 높은 사양을 필요로 하지 않습니다")
    image = Image.open('web.jpg')
    st.image(image, caption='web.jpg')


if doing == '게이밍': #게이밍을 고른 경우 실행.
    cpu = st.select_slider( #cpu 고르는 옵션
    'CPU를 고르세요',
    options=['i5', 'i7', 'i9', 'r5_5600x', 'r7_7600x', 'r7_7800x3d', ])
    st.write('선택한 CPU :', cpu)
    gpu = st.select_slider( #gpu 고르는 옵션
    'GPU를 고르세요',
    options=['RTX3060', 'RTX4060', 'RTX4070', 'RTX4080', 'RX7600', 'RX7700XT', ])
    st.write('선택한 GPU :', gpu)
    
elif doing == '영상편집': #영상편집 고른경우 실행
    cpu = st.select_slider( #cpu 고르는 옵션
    'CPU를 고르세요',
    options=['i7', 'i9','7800x3d', ])
    st.write('선택한 CPU :', cpu)
    gpu = st.select_slider( #gpu 고르는 옵션
    'GPU를 고르세요',
    options=['RTX3060', 'RTX4060', 'RX7600' ])
    st.write('선택한 GPU :', gpu)
    
elif doing == '웹서핑': #웹서핑 고른경우 실행
    cpu = st.select_slider( #cpu 고르는 옵션
    'CPU를 고르세요. gpu는 굳이 필요하지 않습니다.',
    options=['r5_5500', '5600g', 'i3', 'i5'])
    st.write('선택한 CPU :', cpu)
    
    
if cpu == 'i3': #각 부품에 해당하는 가격
    cpu_cpu_price = 80000
elif cpu == 'r5_5500': #각 부품에 해당하는 가격
    cpu_cpu_price = 100000  
elif cpu == '5600g': #각 부품에 해당하는 가격
    cpu_cpu_price = 90000  
elif cpu == 'i5': #각 부품에 해당하는 가격
    cpu_price = 100000
elif cpu == 'i7': #각 부품에 해당하는 가격
    cpu_price = 150000
elif cpu == 'i9': #각 부품에 해당하는 가격
    cpu_price = 200000
elif cpu == 'R5_5600x': #각 부품에 해당하는 가격
    cpu_price = 130000
elif cpu == 'R7_7600x': #각 부품에 해당하는 가격
    cpu_price = 220000
elif cpu == 'R7_7800XT': #각 부품에 해당하는 가격
    cpu_price = 300000
    
if gpu == 'RTX3060': #각 부품에 해당하는 가격
    gpu_price = 300000
elif gpu == 'RTX4070': #각 부품에 해당하는 가격
    gpu_price = 360000    
elif gpu == 'RTX4080': #각 부품에 해당하는 가격
    gpu_price = 460000    
elif gpu == 'RX7600': #각 부품에 해당하는 가격
    gpu_price = 250000
elif gpu == 'RX7700XT': #각 부품에 해당하는 가격
    gpu_price = 400000
st.write('# CPU :', cpu)  
st.write('# GPU :', gpu)  
price = cpu_price + gpu_price #총 비용
st.write('# 총 비용 :', price)  



money = st.slider('최대 지불 가능 금액을 선택하세요', 0, 2000000, 0) #현재 가지고 있는 비용 입력
if money < price: #현재 가지고 있는 비용이 부족한경우
    st.write('금액이', price - money, '원 부족합니다.')
elif money > price: # 구매가능한 경우
    st.write('구매가능합니다.') 
    st.balloons() #풍선효과
    if st.button('추천 사이트 들어가기'):
        st.write('http://shop.danawa.com/main/')
    else:
        st.write('감사합니다.')


