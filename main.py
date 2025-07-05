from flask import Flask, request
import africastalking
import os
from dotenv import load_dotenv

load_dotenv()  # Soma .env file

app = Flask(__name__)

username = os.getenv("AT_USERNAME")
api_key = os.getenv("AT_API_KEY")

africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route("/sms", methods=["POST"])
def sms_reply():
    sender = request.values.get("from")
    incoming_msg = request.values.get("text", "").lower()

    if "habari" in incoming_msg:
        reply = "Habari yako! Karibu kwenye huduma yetu ya SMS."
    elif "nakupenda" in incoming_msg:
        reply = "Nami nakupenda zaidi! ❤️"
    elif "msaada" in incoming_msg:
        reply = "Tafadhali taja huduma unayohitaji."
    elif "lipa" in incoming_msg or "malipo" in incoming_msg:
        reply = (
            "LIPA KUPITIA LIPA KWA SIMU MITANDAO YOTE:\n"
            "Mtandao: Airtel\n"
            "Jina: PETER JORAM SICHILIMA\n"
            "Lipa namba: 66491201"
        )
    else:
        reply = "Samahani, sikuelewa. Andika 'msaada' kwa maelezo zaidi."

    sms.send(reply, [sender])
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
