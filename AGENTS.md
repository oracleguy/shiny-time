# Product Requirements
- Product requirements are located in `docs`

# Python App

- The application is located in `app`
- Run the application in the virtual python environment
- After adding any new dependencies, update the `requirements.txt` file
- Always use the latest version available of packages
- The hardware is abstracted through the `device` class
- The web application is created through `app/server.py:create_app`.
- Keep hardware construction out of module import time so the web layer can
  inject a fake device in tests.
- Use Waitress as the production WSGI server unless a later decision changes
  the deployment architecture.
- Serve the device web interface over local HTTP. Do not add device-side HTTPS
  or require certificates; remote or untrusted-network access must use a VPN
  or an HTTPS-terminating reverse proxy.

# Web App

- The application is located `web`
- It uses the Zola website generator framework
