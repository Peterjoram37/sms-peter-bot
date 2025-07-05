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
