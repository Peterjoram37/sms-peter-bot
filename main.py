from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sms_reply():
    if request.method == "GET":
        return "Service is running!", 200

    incoming_msg = request.values.get("text", "").lower()
    sender = request.values.get("from")

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

    # Badala ya sms.send, tumia print au ongeza implementation yako ya sms
    print(f"Tuma SMS kwa {sender}: {reply}")
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
