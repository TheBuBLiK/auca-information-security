from datetime import datetime
with open('/home/bublik/email_simulated.log', 'a', encoding='utf-8') as f:
    f.write(f'Email simulation at {datetime.now().isoformat()}\n')
