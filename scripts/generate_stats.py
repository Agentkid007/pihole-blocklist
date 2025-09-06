#!/usr/bin/env python3
"""
Statistics generator for Pi-hole blocklist
Generates domain counts and category statistics
"""

import re
from pathlib import Path
from datetime import datetime

def generate_stats(file_path):
    """Generate statistics from the blocklist"""
    stats = {
        'total_lines': 0,
        'comment_lines': 0,
        'empty_lines': 0,
        'domain_lines': 0,
        'categories': {},
        'total_domains': 0
    }
    
    current_category = "Unknown"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        stats['total_lines'] += 1
        line = line.strip()
        
        if not line:
            stats['empty_lines'] += 1
            continue
        
        if line.startswith('#'):
            stats['comment_lines'] += 1
            # Check if it's a category header
            if line.startswith('## '):
                current_category = line[3:].strip()
                stats['categories'][current_category] = 0
            continue
        
        # It's a domain
        stats['domain_lines'] += 1
        stats['total_domains'] += 1
        
        if current_category in stats['categories']:
            stats['categories'][current_category] += 1
        else:
            stats['categories'][current_category] = stats['categories'].get(current_category, 0) + 1
    
    return stats

def main():
    file_path = Path("custom_blocklist.txt")
    
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist")
        return 1
    
    stats = generate_stats(file_path)
    
    print("📊 Pi-hole Blocklist Statistics")
    print("=" * 40)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print(f"📝 File Structure:")
    print(f"  Total lines: {stats['total_lines']}")
    print(f"  Comment lines: {stats['comment_lines']}")
    print(f"  Empty lines: {stats['empty_lines']}")
    print(f"  Domain lines: {stats['domain_lines']}")
    print()
    print(f"🌐 Total Domains: {stats['total_domains']}")
    print()
    print(f"📂 Categories:")
    
    # Sort categories by domain count (descending)
    sorted_categories = sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True)
    
    for category, count in sorted_categories:
        if count > 0:
            print(f"  {category}: {count} domains")
    
    # Save stats to file
    stats_file = Path("STATS.md")
    with open(stats_file, 'w', encoding='utf-8') as f:
        f.write("# Pi-hole Blocklist Statistics\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## 📊 Overview\n\n")
        f.write(f"- **Total Domains:** {stats['total_domains']}\n")
        f.write(f"- **Total Lines:** {stats['total_lines']}\n")
        f.write(f"- **Categories:** {len([c for c, count in stats['categories'].items() if count > 0])}\n\n")
        f.write(f"## 📂 Domain Categories\n\n")
        
        for category, count in sorted_categories:
            if count > 0:
                f.write(f"- **{category}:** {count} domains\n")
        
        f.write(f"\n## 📈 Growth Tracking\n\n")
        f.write(f"| Date | Total Domains | Notes |\n")
        f.write(f"|------|---------------|-------|\n")
        f.write(f"| {datetime.now().strftime('%Y-%m-%d')} | {stats['total_domains']} | Enhanced comprehensive blocklist |\n")
    
    print(f"\n📄 Statistics saved to {stats_file}")
    
    return 0

if __name__ == "__main__":
    exit(main())