#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import argparse

def slugify(text: str) -> str:
    """Make a filesystem-safe label name."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "unknown"

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def parse_model_from_filename(fname: str) -> str:
    """Extract responder/model part from filename convention: evaluator_responder_dataset_..."""
    parts = os.path.basename(fname).split("_")
    if len(parts) > 1:
        return parts[1]  # responder is second part
    return "unknown-model"

def main():
    parser = argparse.ArgumentParser(
        description="Create per-label JSONs of low-scoring samples (<= threshold)."
    )
    parser.add_argument("--input-files", nargs="+", required=True,
                        help="Paths to merged evaluation JSON files.")
    parser.add_argument("--outdir", default=os.path.join("outputs", "flagged_by_label"),
                        help="Output directory (default: outputs/flagged_by_label)")
    parser.add_argument("--threshold", type=float, default=2.5,
                        help="Evaluation threshold (inclusive). Default: 2.5")
    args = parser.parse_args()

    ensure_dir(args.outdir)

    # Collector for global per-label results
    global_per_label = {}

    for infile in args.input_files:
        data = load_json(infile)
        if not isinstance(data, list):
            print(f"⚠️  Skipping {infile}: expected a list at top level.")
            continue

        base = os.path.splitext(os.path.basename(infile))[0]
        out_base_dir = os.path.join(args.outdir, base)
        ensure_dir(out_base_dir)

        model = parse_model_from_filename(infile)

        # Collect per label for this file
        per_label = {}

        for item in data:
            eval_val = item.get("evaluation", None)
            label = item.get("label", "unknown")

            if eval_val is None:
                continue
            try:
                eval_num = float(eval_val)
            except (ValueError, TypeError):
                continue

            if eval_num <= args.threshold:
                # copy to avoid side effects
                new_item = dict(item)
                new_item["model_answering"] = model

                per_label.setdefault(label, []).append(new_item)
                global_per_label.setdefault(label, []).append(new_item)

        # Write per-label files for this input
        for label, items in per_label.items():
            safe_label = slugify(label)
            out_path = os.path.join(out_base_dir, f"{safe_label}.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(items, f, ensure_ascii=False, indent=2)
            print(f"✅ {infile} → {out_path} ({len(items)} samples)")

    # Write global per-label files
    global_dir = os.path.join(args.outdir, "all_models")
    ensure_dir(global_dir)
    for label, items in global_per_label.items():
        safe_label = slugify(label)
        out_path = os.path.join(global_dir, f"{safe_label}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
        print(f"🌍 Global → {out_path} ({len(items)} samples across models)")

if __name__ == "__main__":
    main()
