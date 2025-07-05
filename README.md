# SMS Chatbot kwa kutumia Africa's Talking

Mradi huu ni chatbot ya SMS iliyojengwa kwa Python na Flask, ikitumia Africa's Talking API.

## Features
- Inajibu SMS kwa automatiska (majibu ya kawaida)
- Inatoa huduma ya “lipa kwa simu” (Airtel, jina na namba umepewa)
- Inaweza ku-hostiwa Render

## Jinsi ya kuanza

1. **Clone repo na ingia kwenye folder:**
    ```bash
    git clone <repo yako>
    cd sms-peter-bot
    ```

2. **Andaa environment variables:**
    - Copy `.env.example` na uitunze kama `.env`, kisha jaza `AT_USERNAME` na `AT_API_KEY` zako za Africa's Talking.

3. **Sakinisha dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Endesha app (local):**
    ```bash
    python main.py
    ```

5. **Deploy Render**
    - Unganisha repo yako na Render.com
    - Weka environment variables (AT_USERNAME na AT_API_KEY)
    - Port ya app ni 5000 (default Flask)
    - Hakikisha `gunicorn` imo kwenye requirements.txt kwa production

## Njia za kutumia

- Tuma SMS yenye neno “habari”, “msaada”, “nakupenda”, “lipa” au “malipo” kwenye namba yako ya Africa's Talking
- Bot itajibu kwa ujumbe unaofaa

## Malipo (Lipa kwa Simu)
```
LIPA KUPITIA LIPA KWA SIMU MITANDAO YOTE:
Mtandao: Airtel
Jina: PETER JORAM SICHILIMA
Lipa namba: 66491201
```

## Credits
Peter Joram Sichilima
