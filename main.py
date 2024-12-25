import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_domain_availability(domain):
    url = f"https://whois.az/{domain}"
    
    try:
        response = requests.get(url, timeout=10)  # Bağlantı zaman aşımı eklendi
        response.raise_for_status()  # HTTP hatalarını yakala
    except requests.RequestException as e:
        raise Exception(f"Error: Failed to connect to WHOIS.az - {e}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    result_div = soup.find("div", class_="result")  # "result" div kontrolü
    
    if result_div and "domain is free" in result_div.text.lower():
        return True
    elif result_div:
        return False
    else:
        raise Exception("Error: Unexpected page structure. Please check the HTML layout of WHOIS.az.")

# E-posta gönderme fonksiyonu
def send_email(to_email, domain):
    from_email = "abdulrhmanrhimzad26@gmail.com"  # Kendi e-posta adresinizi buraya ekleyin
    password = "A123456!main.py"            # E-posta şifrenizi buraya ekleyin
    
    subject = f"Domain Available: {domain}"
    body = f"The domain {domain} is available for purchase. Act quickly!"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        print(f"Email sent to {to_email} successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    domain = "online.az"
    admin_email = "abdulrhmanrhimzad26@gmail.com"
    
    try:
        is_available = check_domain_availability(domain)
        if is_available:
            print(f"{domain} is available!")
            send_email(admin_email, domain)
        else:
            print(f"{domain} is not available.")
    except Exception as e:
        print(f"An error occurred: {e}")
