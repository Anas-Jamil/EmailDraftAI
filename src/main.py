import openai
import win32com.client as win32
import datetime

# Get today's date
today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")

# Set your OpenAI API key
openai.api_key = ''

def GetContext():
    Name = input("Your Name: ")
    Email = input("Recipient Email: ")
    Context = input("Context: ")
    return {
        'Name': Name,
        'Email': Email,
        'Context': Context,
    }

def generate_email_content(context):
    body_prompt = f"Write a professional email based on the following context: {context['Context']}. Include the recipient's email: {context['Email']} and your name: {context['Name']}. PLEASE DO NOT INCLUDE SUBJECT IN THE BODY"
    return generate_gpt_response(body_prompt)

def send_email(context, email_content):
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNamespace('MAPI')

    mailItem = olApp.CreateItem(0)
    mailItem.BodyFormat = 1
    
    mailItem.Body = email_content
    
    subject_prompt = f"Give me a subject for an email based on the following body: {mailItem.Body}. I just need the subject, nothing with the body."
    mailItem.Subject = generate_gpt_response(subject_prompt)
    
    mailItem.To = context['Email']
    mailItem.Sensitivity = 2
    mailItem.Display()

def generate_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200  # Adjust max tokens as needed
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating GPT-3 response: {e}")
        return ""

if __name__ == "__main__":
    context = GetContext()
    GetMail(context)