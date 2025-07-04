import argparse, json, sys
from ._loader import load, available_ids

def list_sets() -> None:
    print("\n".join(available_ids()))

def export_set() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("set_id", help="ex: fr_21c")
    p.add_argument("-o", "--out", default="-")
    p.add_argument("--include", nargs="+")
    args = p.parse_args()

    fw = load(args.set_id)
    if args.include:
        data = sorted(fw.subset(args.include))
    else:
        data = sorted(fw.all)

    if args.out == "-":
        print("\n".join(data))
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            if args.out.endswith(".json"):
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                f.write("\n".join(data))
        sys.stderr.write(f"Wrote {len(data)} entries to {args.out}\n")
