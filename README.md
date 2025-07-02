# 🚌 HR Employee Transport Route Module – Odoo

This is a custom Odoo module designed to manage employee transportation within an organization. It includes features for vehicle tracking, route and stop definitions, driver assignment, and employee-seat mapping.

---

## 🚀 Features

- Define transport vehicles (capacity, driver, type)
- Create and manage service routes (start/end time, shift)
- Add route stops with custom order and location (lat/lon)
- Assign employees to specific routes
- Automatically compute seat availability
- View routes per employee or vehicle
- Support for multi-shift service logic (morning, evening, night)

---

## 🧩 Models

### `hr.transport.vehicle`
- Vehicle name, capacity, driver (linked to `hr.employee`)
  
### `hr.transport.route`
- Route name, vehicle, start/end time, shift, related employees
  
### `hr.transport.stop`
- Stop name, route reference, sequence, optional GPS coordinates

---

## 🔧 Installation

1. Clone the repository into your custom addons path:
   ```bash
   git clone https://github.com/Sonerturan/hr_employee_transport_route.git
   
2. Add the path to your odoo.conf:
  addons_path = /opt/odoo/custom_addons

4. Restart the Odoo service and activate developer mode.

6. Install the module via Odoo Apps menu.

---

## 📄 License
This project is licensed under the MIT License.

---

## 👤 Author
Developed by Soner Turan

📧 sonerturan609@gmail.com

🔗 [in/soner-turan](https://www.linkedin.com/in/soner-turan)

