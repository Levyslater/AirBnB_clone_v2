#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# Update package list and install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Allow Nginx HTTP through the firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories including parent folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a test HTML file in the releases/test directory
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create a symbolic link to the test release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Remove existing hbnb_static configuration if it exists to prevent duplicates
sudo sed -i '/location \/hbnb_static {/,/}/d' /etc/nginx/sites-enabled/default

# Update the Nginx configuration to serve the content of web_static
sudo sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

# Restart the Nginx service to apply the changes
sudo service nginx restart

