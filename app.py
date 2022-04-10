# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek


Sex = {0:"Male", 1:"Female"}
ExerciseAngina = {0:"N", 1:"Y"}
ST_Slope = {0:"Up", 1:"Flat"}
RestingECG = {0:"Normal", 1:"ST"}
ChestPainType = {0:"ATA", 1:"NAP", 2:"ASY"}

filename = "model2.sv"
model = pickle.load(open(filename,'rb'))


sex_d = {0:"Women",1:"Man"}
pclass_d = {0:"First",1:"Second", 2:"Third"}
embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():

	st.set_page_config(page_title="Heart Disease")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://health.clevelandclinic.org/wp-content/uploads/sites/3/2020/01/mildHeartAttack-866257238-770x553.jpg")

	with overview:
		st.title("Heart Disease")

	with left:
		_Sex = st.radio( "Gender", list(Sex.keys()), format_func=lambda x : Sex[x] )
		_ChestPainType = st.radio( "ChestPainType", list(ChestPainType.keys()), format_func=lambda x : ChestPainType[x] )
		_RestingECG = st.radio( "RestingECG", list(RestingECG.keys()), format_func=lambda x : RestingECG[x] )
		_ExerciseAngina = st.radio( "ExerciseAngina", list(ExerciseAngina.keys()), format_func=lambda x : ExerciseAngina[x] )
		_ST_Slope = st.radio( "ST_Slope", list(ST_Slope.keys()), format_func=lambda x : ST_Slope[x] )

	with right:
		_Age = st.slider("Age", value=1, min_value=1, max_value=80)
		_RestingBP = st.slider("RestingBP", value=1, min_value=0, max_value=200)
		_Cholesterol = st.slider("Cholesterol", value=1, min_value=0, max_value=700)
		_FastingBS = st.slider("FastingBS", value=1, min_value=0, max_value=1)
		_MaxHR = st.slider("MaxHR", value=1, min_value=50, max_value=250)
		_Oldpeak = st.slider("Oldpeak", min_value=-10, max_value=10)



	data = [[_Age, _Sex, _ChestPainType, _RestingBP, _Cholesterol, _FastingBS, _RestingECG, _MaxHR,  _ExerciseAngina, _Oldpeak, _ST_Slope]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Chance of heard disease:")
		st.write("Prob {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
