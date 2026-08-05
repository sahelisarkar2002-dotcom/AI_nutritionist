import google.genai as genai
import streamlit as st

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key= GOOGLE_API_KEY)

st.set_page_config(
 page_title= "BMI Calculator with AI Nutritionist",
 page_icon= "💪",
 layout= "centered"
)
st.title("AI Diet Planner & Fitness Advisor")
st.write("Calculate your BMI and receive personalized AI Health advice.")

st.divider()
gender = st.selectbox("Gender:", ["Male", "Female"])
age = st.number_input("Enter Age:")
wt = st.slider("Enter your weight in kilograms:", 1.0, 200.00, 70.0)
ht = st.slider("Enter your height in meters:", 1.0, 2.5, 1.7)

bmi = wt / (ht ** 2)
if bmi < 18.5:
 category = "Underweight"
elif bmi < 25:
 category = "Normal"
elif bmi < 30:
 category = "Overweight"
else:
 category = "Obese"

st.success(f"Category: {category}")
st.write(f"Your BMI is: {bmi:.2f}")
#Water Intake

water = wt * 35 / 1000
st.info(f"💧 Recommended Water Intake: {water:.1f} L/day")

prompt = f'''You are an expert nutritionist and fitness coach. User details: Age as {age}, Gender as {gender}, Weight as {wt}, Height as {ht}, BMI as {bmi}, BMI_Category as {category}, Water_Intake as {water} "Provide:

1.Health Summary
2. Diet Suggestions
3. Breakfast
4. Lunch
5. Dinner
6. Healthy Snacks
7. Workout Plan
8. Foods to Avoid
9. Daily Tips
Keep your response easy to understand.'''

if st.button('AI Diet Plan:'):
 st.write("Analyzing your BMI with AI...")

response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt)
st.write(response.text)