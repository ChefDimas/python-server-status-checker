# 🌐 Server Status Checker 🌐

This Python application periodically checks the status of a list of servers and alerts if any of them are down. It utilizes the `requests` library for server checks and can send email alerts.

## 🚀 Features:

- 🖥️ **Server Status Check**: Regularly checks the status of multiple servers.
- 📈 **Response Time**: Fetches server response time.
- 🚨 **Alerts**: Sends alerts if a server is down (Print & Email alerts).

## 🛠️ Setup:

### 1. Clone the Repository:
```bash
git clone [repository-link]
```
### 2. Navigate to Project Directory:
```bash
cd path_to_directory
```
### 3. Install Dependencies:
```bash
pip install requests
```

### 4. Configure Servers & Settings:
Open `config.py` and:
  - Add servers to the `SERVERS` list.
  - Set `CHECK_INTERVAL` for how often to check the servers.
  - Configure email settings:
    - `EMAIL_LOGIN`: Your email (sender)
    - `EMAIL_PASSWORD`: Your email password
    - `EMAIL_RECEIVER`: The email recipient for alerts

⚠️ **Note**: Ensure your email and password are kept secure. Consider using environment variables or a secrets manager for better security.

### 5. Run the Application:
python main.py

## 📧 Email Alerts:

The application supports sending email alerts when a server is down. Ensure `config.py` is set up correctly for email notifications. Depending on your email provider, you might need to enable less secure apps or generate an app-specific password for authentication.

## 📝 License:

This project is open-source and available under the [MIT License](LICENSE).

## 📮 Feedback:

Suggestions or feedback? Please open an issue or submit a pull request! Contributions are welcome! 💙

