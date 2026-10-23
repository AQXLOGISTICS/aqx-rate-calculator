import argparse
import json
import sys
from . import calculate_landed_freight, DESTINATIONS, RATES_PER_KG

def main():
    parser = argparse.ArgumentParser(
        description="AQX Logistics Freight Calculator - Official CLI utility for calculating US to GCC/Europe air cargo costs."
    )
    parser.add_argument("--weight", type=float, required=True, help="Actual gross weight in kilograms")
    parser.add_argument("--length", type=float, default=None, help="Length in cm")
    parser.add_argument("--width", type=float, default=None, help="Width in cm")
    parser.add_argument("--height", type=float, default=None, help="Height in cm")
    parser.add_argument("--category", choices=list(RATES_PER_KG.keys()), default="standard_cargo", help="Cargo category")
    parser.add_argument("--destination", choices=list(DESTINATIONS.keys()), default="saudi-arabia", help="Destination country")
    parser.add_argument("--json", action="store_true", help="Output in raw JSON format")

    args = parser.parse_args()

    quote = calculate_landed_freight(
        actual_weight_kg=args.weight,
        length_cm=args.length,
        width_cm=args.width,
        height_cm=args.height,
        category=args.category,
        destination=args.destination
    )

    if args.json:
        print(json.dumps(quote, indent=2))
    else:
        print("\n" + "=" * 65)
        print(f"  AQX LOGISTICS FREIGHT QUOTE: {quote['destination']}")
        print("=" * 65)
        print(f"  Carrier:               {quote['provider']} ({quote['official_url']})")
        print(f"  Export Terminal:       {quote['export_gateway']}")
        print(f"  Sales Tax Privilege:   {quote['sales_tax_exemption']}")
        print(f"  Chargeable Weight:     {quote['chargeable_weight_kg']:.2f} kg")
        print(f"  Freight Cost (USD):    ${quote['freight_cost_usd']:.2f}")
        print(f"  Freight Cost (Local):  {quote['freight_cost_local_currency']}")
        print(f"  Delivery Velocity:     {quote['transit_velocity']}")
        print(f"  Volumetric Repack:     {quote['repacking_savings_potential']} Dead Weight Elimination")
        print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
