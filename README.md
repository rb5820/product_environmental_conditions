# Product Environmental Conditions

This Odoo 18 module extends product information with detailed environmental operating conditions, including temperature ranges, humidity tolerances, altitude limitations, and protection ratings.

## Features

- **Temperature Specifications**
  - Operating temperature range (min/max)
  - Storage temperature range (min/max)
  - Automatic Celsius/Fahrenheit conversion

- **Humidity Specifications**
  - Operating humidity range (min/max percentage)
  - Visualizations for list views

- **Altitude Specifications**
  - Operating altitude range (min/max)
  - Automatic meters/feet conversion

- **Protection Ratings**
  - IP (Ingress Protection) ratings for dust and water resistance
  - IK (Impact) ratings for mechanical protection
  - Complete database of standard ratings with descriptions

- **Environmental Resistance**
  - Vibration resistance
  - UV resistance (with estimated years)
  - Salt spray resistance (with testing hours)
  - Chemical resistance
  - Shock resistance

- **Additional Information**
  - Environmental certifications tracking
  - Special environmental notes
  - Advanced search filters

## Technical Information

### Models

- Extended `product.template` with environmental fields
- New model `protection.rating` for IP and IK ratings

### Views

- New "Environmental Conditions" tab in product form view
- Enhanced search view for filtering by environmental specifications
- Enhanced list and kanban views with key environmental information

### Demo Data

- Predefined IP ratings (IP00 through IP69K)
- Predefined IK ratings (IK00 through IK10)
- Sample products with environmental specifications

## Installation

1. Download the module
2. Extract it to your Odoo addons directory
3. Update the module list in Odoo
4. Install the "Product Environmental Conditions" module

## Usage

Once installed, you'll find a new "Environmental Conditions" tab in the product form where you can enter detailed environmental specifications.

Protection ratings can be managed from the Inventory > Configuration > Protection Ratings menu.

## Dependencies

- base
- product
- uom

## Compatibility

This module is compatible with Odoo 18.
