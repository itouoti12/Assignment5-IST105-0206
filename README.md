Assignment5

# auto-scall

```bash
#!/bin/bash
sudo dnf update -y
sudo dnf install -y httpd
sudo dnf install python3 -y
sudo dnf install -y php
sudo dnf -y install git
cd /var/www/html
sudo git clone https://github.com/KaitoSaito2222/IST105-Assignment5.git .
sudo chmod +x /var/www/html/process.py
sudo systemctl start httpd

```


# take stress
```
sudo yum install -y stress
stress --cpu 6 --timeout 300
```
