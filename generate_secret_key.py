#!/usr/bin/env python
"""
Quick script to generate a Django SECRET_KEY for production use.
Run: python generate_secret_key.py
"""
from django.core.management.utils import get_random_secret_key

if __name__ == '__main__':
    print("=" * 60)
    print("Generated SECRET_KEY for production:")
    print("=" * 60)
    print(get_random_secret_key())
    print("=" * 60)
    print("\nCopy this key and set it as SECRET_KEY environment variable")
    print("in your hosting platform's environment settings.")

