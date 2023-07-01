import streamlit as st
# from steamlit_lottie import st_lottie
# import requests

st.set_page_config(
	page_title = "my webpage",
	page_icon = ":tada:",
	layout = "wide"
	)


#def load_lottieurl(url):
# 	r = requests.get(url)
# 	if r.status_code != 200:
# 		return None
# 	return r.json()

# lottie_coding = load_lottieurl(
# 	"https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
# 	)


with st.container():
	st.subheader("hi i am seven :wave:")
	st.title("i am from TOGO")
	st.write("i am a developer")
	st.write("learn more at https://python.org")


with st.container():
	st.write('---')
	left_column , right_column = st.columns(2)
	with left_column:
		st.header("what i do ")
		st.write("##")
		st.write(
			"""
		i can teach python and develope webdite 
		and games for peoples
		""")

	with right_column:
		# st_lottie(
		# 	lottie_coding,
		# 	height = 300,
		# 	key = "coding"
		# 	)
		pass


with st.container():
	st.write("---")
	st.subheader("my projects")
	st.write("##")
	image_column, text_column = st.columns((1, 2))

	with image_column:
		#insert img
		st.write("image columns")


	with text_column:
		st.subheader("integrate lottie animations")
		st.write(
			"""
			learn how to use streamlit lottie animations 
			in python 
			""")
		st.markdown("[watch video... ] (https://youtu.be/TXSOitGoINE)")
