#!/usr/bin/env python3
"""
Convert an LSC Official evaluation JSON export to a lightweight lsc-tasks.json.

Usage:
    python3 convert_lsc_tasks.py "LSC Official.json" lsc26-tasks.json
"""

import json
import sys
from collections import defaultdict

TYPE_MAP = {
    "LSC Known-Item Search":         "KIS",
    "LSC Ad-hoc Search":             "AVS",
    "LSC Question & Answer Text":    "QA",
}


def convert(src_path: str, dst_path: str) -> None:
    with open(src_path, encoding="utf-8") as f:
        data = json.load(f)

    template = data["template"]
    template_tasks = {t["id"]: t for t in template["tasks"]}

    # Determine which tasks actually ran and collect correct answers
    ran_ids: set[str] = set()
    gt_map: dict[str, dict] = defaultdict(lambda: {"images": [], "texts": []})

    for rt in data.get("tasks", []):
        tmpl_id = rt["templateId"]
        ran_ids.add(tmpl_id)
        seen_imgs: set[str] = set()
        seen_txts: set[str] = set()

        for sub in rt.get("submissions", []):
            for ans in sub.get("answers", []):
                if ans["status"] != "CORRECT":
                    continue
                for a in ans.get("answers", []):
                    if a.get("type") == "ITEM" and a.get("item"):
                        loc = a["item"]["location"]
                        if loc not in seen_imgs:
                            seen_imgs.add(loc)
                            gt_map[tmpl_id]["images"].append(loc)
                    elif a.get("type") == "TEXT" and a.get("text"):
                        txt = a["text"].strip()
                        if txt and txt.lower() not in seen_txts:
                            seen_txts.add(txt.lower())
                            gt_map[tmpl_id]["texts"].append(txt)

        gt_map[tmpl_id]["images"].sort()

    out = []
    for t in template["tasks"]:
        task_type = TYPE_MAP.get(t["taskType"], t["taskType"])
        hints = sorted(t.get("hints", []), key=lambda h: h.get("start", 0))
        hint_texts = [h["description"] for h in hints]
        ran = t["id"] in ran_ids
        gt = gt_map.get(t["id"], {"images": [], "texts": []})

        if task_type == "KIS":
            groundtruth = {
                "type":  "images",
                "label": "Target images",
                "items": [
                    tgt["item"]["location"]
                    for tgt in t.get("targets", [])
                    if tgt.get("type") == "MEDIA_ITEM" and "item" in tgt
                ],
            }
        elif task_type == "AVS":
            groundtruth = {
                "type":  "images",
                "label": "Correct images from pool",
                "items": gt["images"],
            }
        else:  # QA
            groundtruth = {
                "type":    "text",
                "label":   "Correct answer(s)",
                "answers": gt["texts"],
            }

        out.append({
            "id":           t["name"],
            "type":         task_type,
            "duration":     t["duration"],
            "duration_min": t["duration"] // 60,
            "ran":          ran,
            "query":        hint_texts[0] if hint_texts else "",
            "hints":        hint_texts,
            "groundtruth":  groundtruth,
        })

    out.sort(key=lambda x: x["id"])

    with open(dst_path, "w", encoding="utf-8") as f:
        json.dump({"tasks": out}, f, indent=2, ensure_ascii=False)

    n_ran  = sum(1 for t in out if t["ran"])
    n_kis  = sum(1 for t in out if t["type"] == "KIS")
    n_avs  = sum(1 for t in out if t["type"] == "AVS")
    n_qa   = sum(1 for t in out if t["type"] == "QA")
    print(f"Wrote {len(out)} tasks ({n_kis} KIS, {n_avs} AVS, {n_qa} QA) — {n_ran} ran — to {dst_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.json> <output.json>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
