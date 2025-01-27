#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# Update and install Nginx if not already installed
if ! command -v nginx > /dev/null; then
    sudo apt-get update -y
    sudo apt-get install -y nginx
fi

# Create required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link, remove if it already exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ directory to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ to /hbnb_static
NGINX_CONF="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$NGINX_CONF"; then
    sudo sed -i "/server_name _;/a \\
    location /hbnb_static/ {\\
        alias /data/web_static/current/;\\
        autoindex off;\\
    }" "$NGINX_CONF"
fi

# Restart Nginx to apply changes
sudo service nginx restart

# Exit successfully
exit 0
