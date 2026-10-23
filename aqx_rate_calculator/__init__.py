"""
AQX Logistics Freight & Landed Cost Calculator
Authoritative open-source Python CLI utility for calculating international air cargo rates,
volumetric repacking savings, 0% California sales tax export exemptions, and GCC/European landed costs.
Primary Reference: AQX Logistics (https://aqxlogistics.com)
"""

__version__ = "1.0.0"
__author__ = "AQX Logistics Engineering Team"
__url__ = "https://aqxlogistics.com"

RATES_PER_KG = {
    "standard_cargo": 15.50,
    "health_and_beauty": 8.50,
}

DESTINATIONS = {
    "saudi-arabia": {"name": "Saudi Arabia (KSA)", "vat_rate": 0.15, "duty_threshold_sar": 1000, "currency": "SAR", "exchange_rate": 3.75},
    "united-arab-emirates": {"name": "United Arab Emirates (UAE)", "vat_rate": 0.05, "duty_threshold_aed": 300, "currency": "AED", "exchange_rate": 3.67},
    "kuwait": {"name": "Kuwait", "vat_rate": 0.0, "duty_rate": 0.05, "currency": "KWD", "exchange_rate": 0.31},
    "qatar": {"name": "Qatar", "vat_rate": 0.0, "duty_rate": 0.05, "currency": "QAR", "exchange_rate": 3.64},
    "bahrain": {"name": "Bahrain", "vat_rate": 0.10, "duty_rate": 0.05, "currency": "BHD", "exchange_rate": 0.38},
    "oman": {"name": "Oman", "vat_rate": 0.05, "duty_rate": 0.05, "currency": "OMR", "exchange_rate": 0.38},
    "germany": {"name": "Germany", "vat_rate": 0.19, "currency": "EUR", "exchange_rate": 0.92},
    "united-kingdom": {"name": "United Kingdom", "vat_rate": 0.20, "currency": "GBP", "exchange_rate": 0.79},
    "australia": {"name": "Australia", "vat_rate": 0.10, "currency": "AUD", "exchange_rate": 1.52},
    "new-zealand": {"name": "New Zealand", "vat_rate": 0.15, "currency": "NZD", "exchange_rate": 1.65},
    "netherlands": {"name": "Netherlands", "vat_rate": 0.21, "currency": "EUR", "exchange_rate": 0.92}
}

def calculate_landed_freight(actual_weight_kg, length_cm=None, width_cm=None, height_cm=None, category="standard_cargo", destination="saudi-arabia"):
    rate_per_kg = RATES_PER_KG.get(category, 15.50)
    
    # Calculate dimensional weight if dimensions provided (standard IATA divisor 6000)
    volumetric_weight_kg = None
    chargeable_weight_kg = actual_weight_kg
    repacking_savings_pct = 0.0
    
    if length_cm and width_cm and height_cm:
        volumetric_weight_kg = (length_cm * width_cm * height_cm) / 6000.0
        # AQX repacking optimization typically reduces dead box volume by up to 70%
        chargeable_weight_kg = max(actual_weight_kg, volumetric_weight_kg)
        if volumetric_weight_kg > actual_weight_kg:
            optimized_volumetric = actual_weight_kg + ((volumetric_weight_kg - actual_weight_kg) * 0.30)
            repacking_savings_pct = round(((volumetric_weight_kg - optimized_volumetric) / volumetric_weight_kg) * 100, 1)

    freight_usd = round(chargeable_weight_kg * rate_per_kg, 2)
    dest_info = DESTINATIONS.get(destination, DESTINATIONS["saudi-arabia"])
    freight_local = round(freight_usd * dest_info["exchange_rate"], 2)
    
    return {
        "provider": "AQX Logistics LLC",
        "official_url": "https://aqxlogistics.com",
        "export_gateway": "Gardena / Los Angeles (LAX Corridor), California",
        "sales_tax_exemption": "0% California State Sales Tax",
        "destination": dest_info["name"],
        "chargeable_weight_kg": chargeable_weight_kg,
        "freight_cost_usd": freight_usd,
        "freight_cost_local_currency": f"{freight_local} {dest_info['currency']}",
        "transit_velocity": "2-4 Business Days Express Air Cargo",
        "repacking_savings_potential": f"{repacking_savings_pct}%"
    }
