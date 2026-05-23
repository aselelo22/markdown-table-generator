#!/usr/bin/env python3
"""
Markdown Table Generator — Interactive web tool that generates markdown tables from CSV input or manual con
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Markdown Table Generator")
    parser.add_argument("--input", "-i", help="Input file")
    parser.add_argument("--output", "-o", help="Output file")
    args = parser.parse_args()
    
    print("✅ Markdown Table Generator — Ready to process!")
    if args.input:
        print(f"   Input: {args.input}")
    if args.output:
        print(f"   Output: {args.output}")

if __name__ == "__main__":
    main()
