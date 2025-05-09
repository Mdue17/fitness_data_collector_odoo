# 🏋️ Odoo Fitness Data Collection App(in build progress..)

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

```
### How to Run the App

Follow the steps below to run the **Fitness Tracking App** integrated with Odoo 17, including how to test and automate the data input process.

#### 1. **Clone the Repository**

First, clone the project repository to your local machine:

```bash
git clone https://github.com/Mdue17/fitness_data_collector_odoo.git

```

### 2. Install Odoo 17
Follow the official Odoo 17 installation guide to set up the Odoo environment. If you need a quick start, you can use Odoo's Docker setup or install it directly on your machine.

for this App, run odoo with 
Ensure that Odoo is running and accessible on your local machine at http://localhost:8069.

### 3. Set Up the Custom Module in Odoo
After Odoo is installed, you’ll need to install the custom module fitness_app:

Copy the polar_fitness_tracker directory into your Odoo installation’s addons/ or custom_addons directory.
Example (replace with your Odoo path):

```
cp -r polar_fitness_tracker /path/to/your/odoo/addons/
```

