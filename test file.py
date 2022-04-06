### 모듈설치, 데이터불러오기, 특정 컬럼 추출

import numpy as np
import pandas as pd
import io
import re

# df = pd.read_csv('C:/BEK/미니프로젝트/youtube1.csv', encoding='UTF-8')




from konlpy.tag import Okt
import re
tokenizer = Okt()
def text_preprocessing(text,tokenizer):
    
    stopwords = ['을', '를', '이', '가', '은', '는']
    
    txt = re.sub('[^가-힣a-z]', ' ', text)
    token = tokenizer.morphs(txt)
    token = [t for t in token if t not in stopwords]
        
    return token

ex_text = "나는 을 를 이 가 등등을 없애서 깔끔하게 전처리를 시도해볼것이다. 가능할까? 호로로로로로"
example_pre= text_preprocessing(ex_text,tokenizer)