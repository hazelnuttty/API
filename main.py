from flask import Flask, jsonify
import random
import base64
import string

app = Flask(__name__)

# daftar pap bisa kamu tambah seenaknyaa
pap_list = [
"https://cdn.discordapp.com/attachments/1338547058402918441/1341704634544296018/IMG-20250213-WA0048.jpg", 
"https://cdn.discordapp.com/attachments/1338547058402918441/1341704510539694170/IMG-20250218-WA0173.jpg", 
"https://cdn.discordapp.com/attachments/1338547058402918441/1341704375873175603/IMG-20250219-WA0053.jpg", 
"https://cdn.discordapp.com/attachments/1338547058402918441/1341704267672584252/IMG-20250219-WA0054.jpg", 
"https://cdn.discordapp.com/attachments/1338547058402918441/1342281103892942958/IMG-20250219-WA0128.jpg", 
"https://cdn.discordapp.com/attachments/1338547058402918441/1342281210755285002/IMG-20250201-WA0231.jpg",
"https://cdn.discordapp.com/attachments/1338547058402918441/1342281308193165332/IMG-20250130-WA0022.jpg", 
"https://cdn.discordapp.com/attachments/1338547058402918441/1342281388795236453/IMG-20250129-WA0450.jpg", 
"https://cdn.discordapp.com/attachments/1338547058402918441/1342924136028307457/IMG-20250223-WA0004.jpg",    
"https://cdn.discordapp.com/attachments/1338547058402918441/1342924228227498089/IMG-20250222-WA0278.jpg"
]

# fungsi buat generate apikey random
def generate_apikey():
    return "HZL-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

@app.route("/")
def home():
    return "API pap by hazelnut - /pap"

@app.route("/pap")
def get_pap():
    pap_url = random.choice(pap_list)
    pap_encoded = base64.b64encode(pap_url.encode()).decode()
    return jsonify({
        "Name": "API pap by hazelnut",
        "Status": "Active",
        "Apikey": generate_apikey(),
        "Secret": pap_encoded
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
