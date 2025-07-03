import os
from flask import Flask, request
import africastalking
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

AT_USERNAME = os.getenv("AT_USERNAME")
AT_API_KEY = os.getenv("AT_API_KEY")

africastalking.initialize(AT_USERNAME, AT_API_KEY)
sms = africastalking.SMS

@app.route("/", methods=["POST"])
def sms_reply():
    incoming_msg = request.values.get("text", "").lower()
    sender = request.values.get("from")

    if "habari" in incoming_msg:
        reply = "Habari yako! Karibu kwenye huduma yetu ya SMS."
    elif "nakupenda" in incoming_msg:
        reply = "Nami nakupenda zaidi! ❤️"
    elif "msaada" in incoming_msg:
        reply = "Tafadhali taja huduma unayohitaji."
    else:
        reply = "Samahani, sikuelewa. Andika 'msaada' kwa maelezo zaidi."

    sms.send(reply, [sender])
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
