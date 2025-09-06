#!/usr/bin/env python3
"""
Remove duplicate domains from blocklist while preserving structure
"""

import sys
from pathlib import Path

def remove_duplicates(file_path):
    """Remove duplicate domains while preserving comments and structure"""
    seen_domains = set()
    output_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        stripped_line = line.strip()
        
        # Keep comments and empty lines as-is
        if not stripped_line or stripped_line.startswith('#'):
            output_lines.append(line)
            continue
        
        # Check if domain is already seen
        domain_lower = stripped_line.lower()
        if domain_lower not in seen_domains:
            seen_domains.add(domain_lower)
            output_lines.append(line)
        else:
            print(f"Removed duplicate: {stripped_line}")
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    print(f"Processed {len(lines)} lines, kept {len(output_lines)} lines")
    print(f"Removed {len(lines) - len(output_lines)} duplicate domains")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 remove_duplicates.py <blocklist_file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    print(f"Removing duplicates from {file_path}...")
    remove_duplicates(file_path)
    print("✅ Duplicates removed!")

if __name__ == "__main__":
    main()