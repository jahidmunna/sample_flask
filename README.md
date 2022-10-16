# sample_flask

## Installation 
```bash
pip install -r requirements.txt 
```

## Start
```bash
python app.py
```
## Hosting
```bash
ssh -R 80:localhost:5000 nokey@localhost.run -T -n
```

## Check Host Server
```bash
grep "https://[-0-9a-z.]*.lhr.life"
```

##### *required python3.8