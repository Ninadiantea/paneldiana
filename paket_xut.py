import json
from api_request import send_api_request, get_family

PACKAGE_FAMILY_CODE = "08a3b1e6-8e78-4e45-a540-b40f06871cfe"

def get_package_xut(tokens: dict):
    packages = []
    
    try:
        print("Fetching package family data...")
        data = get_family(tokens, PACKAGE_FAMILY_CODE)
        
        if not data:
            print("Failed to get family data - API returned None")
            return []
        
        if "package_variants" not in data:
            print(f"Invalid data structure. Keys: {data.keys()}")
            return []
        
        package_variants = data["package_variants"]
        print(f"Found {len(package_variants)} package variants")
        
        start_number = 1
        for variant in package_variants:
            print(f"Checking variant: {variant.get('name', 'Unknown')}")
            
            if variant.get("name") == "For Xtra Combo":
                package_options = variant.get("package_options", [])
                print(f"Found {len(package_options)} package options")
                
                for option in package_options:
                    option_name = option.get("name", "").lower()
                    print(f"Checking option: {option_name}")
                    
                    if option_name in ["vidio", "iflix", "basic"]:
                        friendly_name = option.get("name", "")
                        
                        if friendly_name.lower() == "basic":
                            friendly_name = "Xtra Combo Unli Turbo Basic"
                        elif friendly_name.lower() == "vidio":
                            friendly_name = "Unli Turbo Vidio 30 Hari"
                        elif friendly_name.lower() == "iflix":
                            friendly_name = "Unli Turbo Iflix 30 Hari"
                            
                        packages.append({
                            "number": start_number,
                            "name": friendly_name,
                            "price": option.get("price", 0),
                            "code": option.get("package_option_code", "")
                        })
                        
                        print(f"Added package: {friendly_name}")
                        start_number += 1
        
        print(f"Total packages found: {len(packages)}")
        return packages
        
    except Exception as e:
        print(f"Error in get_package_xut: {str(e)}")
        return []