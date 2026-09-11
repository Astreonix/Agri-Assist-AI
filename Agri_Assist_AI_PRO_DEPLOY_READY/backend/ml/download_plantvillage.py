"""Download PlantVillage through TensorFlow Datasets and export class folders.

Review the PlantVillage license and attribution terms before redistributing
images or trained models.
"""

import argparse
import re
from pathlib import Path

import tensorflow_datasets as tfds
from PIL import Image


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._") or "unknown"


def export_dataset(output_dir: Path, tfds_dir: Path | None = None) -> None:
    dataset, info = tfds.load(
        "plant_village",
        split="train",
        as_supervised=True,
        with_info=True,
        data_dir=str(tfds_dir) if tfds_dir else None,
    )
    class_names = info.features["label"].names
    output_dir.mkdir(parents=True, exist_ok=True)
    counts = {name: 0 for name in class_names}

    for image, label in tfds.as_numpy(dataset):
        original_name = class_names[int(label)]
        class_dir = output_dir / safe_name(original_name)
        class_dir.mkdir(exist_ok=True)
        image_path = class_dir / f"{counts[original_name]:06d}.jpg"
        Image.fromarray(image).convert("RGB").save(image_path, quality=95)
        counts[original_name] += 1

    print(f"Exported {sum(counts.values())} images to {output_dir}")
    print(f"Classes: {len(class_names)}")
    for class_name, count in counts.items():
        print(f"  {class_name}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", default="dataset")
    parser.add_argument("--tfds_dir", default=None)
    args = parser.parse_args()
    export_dataset(Path(args.output_dir), Path(args.tfds_dir) if args.tfds_dir else None)
