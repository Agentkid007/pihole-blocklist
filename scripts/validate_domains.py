#!/usr/bin/env python3
"""
Domain validation script for Pi-hole blocklist
Validates domain syntax and checks for duplicates
"""

import re
import sys
from collections import Counter
from pathlib import Path

def is_valid_domain(domain):
    """Check if a domain is valid"""
    if not domain or len(domain) > 255:
        return False
    
    # Remove any leading/trailing whitespace
    domain = domain.strip()
    
    # Basic domain regex
    domain_pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$'
    )
    
    return bool(domain_pattern.match(domain))

def validate_blocklist(file_path):
    """Validate the blocklist file"""
    errors = []
    warnings = []
    domains = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        
        # Skip comments and empty lines
        if not line or line.startswith('#'):
            continue
        
        # Check if it's a valid domain
        if not is_valid_domain(line):
            errors.append(f"Line {i}: Invalid domain format: {line}")
        else:
            domains.append(line.lower())
    
    # Check for duplicates
    domain_counts = Counter(domains)
    duplicates = {domain: count for domain, count in domain_counts.items() if count > 1}
    
    if duplicates:
        for domain, count in duplicates.items():
            warnings.append(f"Duplicate domain found {count} times: {domain}")
    
    return errors, warnings, len(domains)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate_domains.py <blocklist_file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    print(f"Validating {file_path}...")
    
    errors, warnings, domain_count = validate_blocklist(file_path)
    
    print(f"\n📊 Results:")
    print(f"Total domains: {domain_count}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    
    if errors:
        print("\n❌ Errors:")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("\n⚠️ Warnings:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("\n✅ All domains are valid!")
    
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())