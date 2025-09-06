#!/bin/bash
"""
Update script for Pi-hole blocklist
Updates timestamps and validates the blocklist
"""

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
BLOCKLIST_FILE="$ROOT_DIR/custom_blocklist.txt"

echo "🔄 Updating Pi-hole Blocklist..."

# Update timestamp in blocklist
current_date=$(date +"%Y-%m-%d")
sed -i "s/# Last updated: [0-9-]*/# Last updated: $current_date/" "$BLOCKLIST_FILE"

# Validate domains
echo "🔍 Validating domains..."
python3 "$SCRIPT_DIR/validate_domains.py" "$BLOCKLIST_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Validation passed!"
else
    echo "❌ Validation failed!"
    exit 1
fi

# Generate statistics
echo "📊 Generating statistics..."
cd "$ROOT_DIR"
python3 "$SCRIPT_DIR/generate_stats.py"

# Count domains
domain_count=$(grep -v '^#' "$BLOCKLIST_FILE" | grep -v '^$' | wc -l)
echo "📝 Updating domain count in header..."
sed -i "s/# Total domains: ~[0-9]*+/# Total domains: ~$domain_count+/" "$BLOCKLIST_FILE"

echo "✅ Update complete!"
echo "📊 Total domains: $domain_count"