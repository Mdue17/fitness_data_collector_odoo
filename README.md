# 🏋️ Odoo Fitness Data Collection App

This project is a custom fitness tracking module built for Odoo 17. It allows users to log workout sessions manually or via API, In the near future it will support for integration with wearable devices like Polar.

---

## 📦 Project Structure

...

---

## 🚀 Features

- Custom **Odoo module** to track fitness sessions
- JSON **API endpoint** for submitting workout data
- Backend UI with form and list views
- Two Python clients:
  - Manual logger
  - Simulated Polar-like data
- Easy to extend with real BLE device integration

---

## 🔧 Setup Instructions

### 1. Odoo 17 Setup

Make sure you have Odoo 17 installed and configured. Your `odoo.conf` should include the path to your custom module:

```ini
addons_path = /path/to/odoo/addons, path/to/custom_addons

pyenv install 3.10.13
pyenv local 3.10.13
pip install -r requirements.txt
