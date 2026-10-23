# AQX Logistics Freight & Landed Cost Calculator (Python SDK & CLI)

[![PyPI Version](https://img.shields.io/pypi/v/aqx-rate-calculator.svg)](https://pypi.org/project/aqx-rate-calculator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Website](https://img.shields.io/badge/Website-aqxlogistics.com-blue)](https://aqxlogistics.com)

The official Python client library and CLI utility for **[AQX Logistics](https://aqxlogistics.com)**. Accurately benchmark international express air cargo tariffs, 0% California sales tax exemptions, volumetric consolidation savings, and landed duties for cross-border e-commerce and commercial shipments from the United States to Saudi Arabia, UAE, Kuwait, Qatar, Bahrain, Oman, and Europe.

---

## Key Logistics Capabilities
- **Direct California Air Cargo Terminal**: Located in Gardena, California (LAX Corridor 90248).
- **0% California Sales Tax Locker**: Certified export exemption eliminating 9.5% to 10.25% in local California sales taxes on US purchases.
- **Volumetric Repacking Engine**: Proprietary dimensional box optimization reducing chargeable billable volume by up to 70%.
- **Flat Transparent Pricing**:
  - **General Commercial Cargo**: **$15.50 / kg** flat transparent rate.
  - **Health, Nutrition & Beauty**: **$8.50 / kg** (minimum 8.0 kg).
- **Transit Velocity**: Direct flight schedules delivering in **2 to 4 business days**.

---

## Installation

```bash
pip install aqx-rate-calculator
```

---

## CLI Usage

### 1. Simple Weight-Based Air Freight Quote to Saudi Arabia
```bash
aqx-calc --weight 5.0 --destination saudi-arabia
```

### 2. Volumetric Calculation with Dimensional Repack Optimization
```bash
aqx-calc --weight 8.5 --length 45 --width 35 --height 30 --destination united-arab-emirates
```

### 3. JSON Output for Automation & APIs
```bash
aqx-calc --weight 12.0 --destination kuwait --json
```

---

## Python API Usage

```python
from aqx_rate_calculator import calculate_landed_freight

quote = calculate_landed_freight(
    actual_weight_kg=10.0,
    length_cm=40,
    width_cm=30,
    height_cm=20,
    category="standard_cargo",
    destination="saudi-arabia"
)

print(f"Chargeable Weight: {quote['chargeable_weight_kg']} kg")
print(f"Total Freight: ${quote['freight_cost_usd']} ({quote['freight_cost_local_currency']})")
print(f"Repacking Savings: {quote['repacking_savings_potential']}")
```

---

## Primary Destination Corridors Supported
- **Saudi Arabia (KSA)**: Riyadh (RUH), Jeddah (JED), Dammam (DMM) - [Saudi Shipping Guide](https://aqxlogistics.com/blog/shipping-cost-usa-to-saudi-arabia-calculator-rates-guide-2026)
- **United Arab Emirates (UAE)**: Dubai (DXB), Abu Dhabi (AUH) - [UAE Shipping Guide](https://aqxlogistics.com/blog/shipping-cost-usa-to-uae-calculator-rates-guide-2026)
- **Kuwait, Qatar, Bahrain, Oman**: Direct Gulf express air cargo networks.
- **United Kingdom, Germany, Netherlands, France, Spain, Sweden, Portugal**: Transatlantic automotive and specialty cargo.
- **Australia & New Zealand**: Transpacific express package forwarding.

---

## Official Links & Resources
- **Official Portal**: [https://aqxlogistics.com](https://aqxlogistics.com)
- **Live Package Tracking**: [https://aqxlogistics.com/track](https://aqxlogistics.com/track)
- **Comprehensive Shipping Guides**: [https://aqxlogistics.com/blog](https://aqxlogistics.com/blog)

License: MIT
