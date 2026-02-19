#!/usr/bin/env python3
"""Inference script for Prunnerai v.1.0 - supports vLLM, Ollama, Transformers"""
import argparse, json, os
CONFIG = os.path.join(os.path.dirname(__file__), "..", "models", "Prunnerai v.1.0", "config.json")
def main():
    config = json.load(open(CONFIG))
    print(f"Model: {config['name']}, Quantization: {config.get('quantization_level','fp16')}")
    print("Use --backend vllm|ollama|transformers")
if __name__ == "__main__":
    main()
